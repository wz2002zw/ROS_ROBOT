import math

def calculate_quaternion(axis: str, angle_degrees: float) -> tuple:
    """计算绕指定轴旋转指定角度的四元数"""
    angle_radians = math.radians(angle_degrees)
    half_angle = angle_radians / 2
    
    x, y, z = 0, 0, 0
    if axis.lower() == 'x':
        x = 1
    elif axis.lower() == 'y':
        y = 1
    elif axis.lower() == 'z':
        z = 1
    else:
        raise ValueError(f"无效的旋转轴: {axis}")
    
    w = math.cos(half_angle)
    x = x * math.sin(half_angle)
    y = y * math.sin(half_angle)
    z = z * math.sin(half_angle)
    
    return (w, x, y, z)

def multiply_quaternions(q1: tuple, q2: tuple) -> tuple:
    """四元数乘法：q1 × q2"""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    
    return (w, x, y, z)

def normalize_quaternion(q: tuple) -> tuple:
    """归一化四元数"""
    w, x, y, z = q
    magnitude = math.sqrt(w**2 + x**2 + y**2 + z**2)
    
    if magnitude == 0:
        raise ValueError("零四元数无法归一化")
    
    return (w/magnitude, x/magnitude, y/magnitude, z/magnitude)

def parse_input(user_input: str) -> list:
    """解析输入的旋转序列，支持x、y、z轴任意组合，未输入的轴默认为0度"""
    if user_input.lower() == 'q':
        raise SystemExit("程序已退出")
    
    parts = user_input.strip().split()
    rotations = {'x': 0.0, 'y': 0.0, 'z': 0.0}
    
    if len(parts) % 2 != 0:
        raise ValueError("输入格式错误：旋转轴和角度必须成对出现（如：x 60 y 45）")
    
    for i in range(0, len(parts), 2):
        axis = parts[i].lower()
        if axis not in ['x', 'y', 'z']:
            raise ValueError(f"无效的旋转轴: {axis}，请输入 x, y 或 z")
        
        try:
            angle = float(parts[i+1])
        except ValueError:
            raise ValueError(f"无效的角度值: {parts[i+1]}")
        
        rotations[axis] = angle
    
    return [('x', rotations['x']), ('y', rotations['y']), ('z', rotations['z'])]

def main():
    print("==== 四元数计算器 ====")
    print("输入格式：旋转轴1 角度1 旋转轴2 角度2 ...（例如：x 60 y 60）")
    print("支持x、y、z轴任意组合，未输入的轴默认为0度旋转")
    print("输入 'q' 随时退出程序")
    
    while True:
        user_input = input("\n请输入旋转序列（或输入 'q' 退出）：").strip()
        
        if user_input.lower() == 'q':
            print("程序已退出")
            break
        
        try:
            rotations = parse_input(user_input)
            
            active_rotations = [(axis, angle) for axis, angle in rotations if abs(angle) > 1e-10]
            
            if not active_rotations:
                print("所有轴旋转角度均为0，结果为单位四元数 (1, 0, 0, 0)")
                continue
            
            combined_quaternion = (1.0, 0.0, 0.0, 0.0)
            for axis, angle in rotations:
                if abs(angle) > 1e-10:
                    current_q = calculate_quaternion(axis, angle)
                    combined_quaternion = multiply_quaternions(current_q, combined_quaternion)
            
            normalized_q = normalize_quaternion(combined_quaternion)
            
            print("\n==== 计算结果 ====")
            print(f"执行以下旋转：")
            for i, (axis, angle) in enumerate(active_rotations, 1):
                print(f"  {i}. 绕 {axis} 轴旋转 {angle}°")
            
            print("\n组合后的四元数为：")
            print(f"w = {normalized_q[0]:.6f}, x = {normalized_q[1]:.6f}, y = {normalized_q[2]:.6f}, z = {normalized_q[3]:.6f}")
            print(f"四元数形式：({normalized_q[0]:.6f}, {normalized_q[1]:.6f}i, {normalized_q[2]:.6f}j, {normalized_q[3]:.6f}k)")
            
            angle_radians = 2 * math.acos(normalized_q[0])
            angle_degrees = math.degrees(angle_radians)
            
            if abs(angle_radians) < 1e-10:
                axis_x, axis_y, axis_z = 1, 0, 0
            else:
                sin_half_angle = math.sin(angle_radians / 2)
                axis_x = normalized_q[1] / sin_half_angle
                axis_y = normalized_q[2] / sin_half_angle
                axis_z = normalized_q[3] / sin_half_angle
            
            print("\n等效的单一旋转：")
            print(f"绕轴 ({axis_x:.6f}, {axis_y:.6f}, {axis_z:.6f}) 旋转 {angle_degrees:.6f}°")
            
        except ValueError as e:
            print(f"输入错误：{e}")
            print("请使用格式：旋转轴1 角度1 旋转轴2 角度2 ...（例如：x 60 y 60）")
        except SystemExit as e:
            print(e)
            break
        except Exception as e:
            print(f"发生未知错误：{e}")

if __name__ == "__main__":
    main()