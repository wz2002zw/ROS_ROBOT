import math

def calculate_quaternion(axis: str, angle_degrees: float) -> tuple:
    """计算绕指定轴旋转指定角度的四元数"""
    # 将角度转换为弧度
    angle_radians = math.radians(angle_degrees)
    half_angle = angle_radians / 2
    
    # 初始化旋转轴的单位向量
    x, y, z = 0, 0, 0
    if axis.lower() == 'x':
        x = 1
    elif axis.lower() == 'y':
        y = 1
    elif axis.lower() == 'z':
        z = 1
    else:
        raise ValueError(f"无效的旋转轴: {axis}，请输入 x, y 或 z")
    
    # 计算四元数分量
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

def main():
    print("==== 四元数计算器 ====")
    print("输入格式：旋转轴 角度（例如：x 90 表示绕x轴旋转90度）")
    print("输入空行结束，程序将计算所有旋转的组合四元数")
    
    rotations = []
    while True:
        user_input = input("\n请输入旋转轴和角度（或空行结束）：").strip()
        
        if not user_input:
            break
        
        try:
            axis, angle_str = user_input.split()
            angle = float(angle_str)
            rotations.append((axis, angle))
            
            # 计算并显示当前旋转的四元数
            q = calculate_quaternion(axis, angle)
            print(f"绕 {axis} 轴旋转 {angle}° 的四元数：")
            print(f"w = {q[0]:.6f}, x = {q[1]:.6f}, y = {q[2]:.6f}, z = {q[3]:.6f}")
            print(f"四元数形式：({q[0]:.6f}, {q[1]:.6f}i, {q[2]:.6f}j, {q[3]:.6f}k)")
            
        except ValueError as e:
            print(f"输入错误：{e}")
            print("请使用格式：旋转轴 角度（例如：x 90）")
    
    if not rotations:
        print("未输入任何旋转，程序退出")
        return
    
    # 计算组合四元数
    combined_quaternion = (1.0, 0.0, 0.0, 0.0)  # 初始化为单位四元数
    for axis, angle in rotations:
        current_q = calculate_quaternion(axis, angle)
        combined_quaternion = multiply_quaternions(current_q, combined_quaternion)
    
    # 归一化结果（防止浮点数误差）
    normalized_q = normalize_quaternion(combined_quaternion)
    
    # 显示最终结果
    print("\n==== 计算结果 ====")
    print(f"连续执行以下旋转：")
    for axis, angle in rotations:
        print(f"  1. 绕 {axis} 轴旋转 {angle}°")
    
    print("\n组合后的四元数为：")
    print(f"w = {normalized_q[0]:.6f}, x = {normalized_q[1]:.6f}, y = {normalized_q[2]:.6f}, z = {normalized_q[3]:.6f}")
    print(f"四元数形式：({normalized_q[0]:.6f}, {normalized_q[1]:.6f}i, {normalized_q[2]:.6f}j, {normalized_q[3]:.6f}k)")
    
    # 计算等效的旋转轴和角度
    angle_radians = 2 * math.acos(normalized_q[0])
    angle_degrees = math.degrees(angle_radians)
    
    # 处理角度接近0的情况（避免除以零）
    if abs(angle_radians) < 1e-10:
        axis_x, axis_y, axis_z = 1, 0, 0  # 任意轴
    else:
        sin_half_angle = math.sin(angle_radians / 2)
        axis_x = normalized_q[1] / sin_half_angle
        axis_y = normalized_q[2] / sin_half_angle
        axis_z = normalized_q[3] / sin_half_angle
    
    print("\n等效的单一旋转：")
    print(f"绕轴 ({axis_x:.6f}, {axis_y:.6f}, {axis_z:.6f}) 旋转 {angle_degrees:.6f}°")

if __name__ == "__main__":
    main()