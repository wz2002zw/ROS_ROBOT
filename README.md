# 机械臂仿真

## 安装ubunto 22.04

### 下载ubbuntu光盘安装即可，网上资源很多

## 安装ros2 

### 确认 Ubuntu 版本

``` bash
lsb_release -a  
```

需为 22.04 (Jammy) 或 20.04 (Focal)
Humble 支持 Ubuntu 22.04 (Jammy) 和 20.04 (Focal)
若为其他版本，可参考 ROS 2 官方安装指南 选择对应版本

### 设置 locale（确保 UTF-8 编码）

``` bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

## 配置软件源

### 添加 ROS 2 apt 仓库

``` bash
sudo apt update && sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

### 添加源列表

``` bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

## 安装 ROS 2

### 更新软件包索引

``` bash
sudo apt update
```

### 安装桌面完整版（推荐）

``` bash
sudo apt install ros-humble-desktop-full
```

#### 包含：ROS 2 核心、RViz、 Gazebo、开发工具等

## 环境配置

### 设置环境变量

### 每次启动终端需手动加载环境：

``` bash
source /opt/ros/humble/setup.bash
```

### 或添加到 .bashrc 自动加载：

``` bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 安装 ROS 2 开发工具

``` bash
sudo apt install python3-argcomplete python3-colcon-common-extensions
```

## 验证安装

### 运行 talker/listener 示例

 终端 1：启动 talker（发布消息）

``` bash
ros2 run demo_nodes_cpp talker
```

终端 2：启动 listener（订阅消息）

``` bash
ros2 run demo_nodes_py listener
```

若看到终端 2 显示 "I heard: [Hello World: X]"，说明通信正常

## 安装完成后，你可以尝试创建自己的 ROS 2 包：

``` bash
source /opt/ros/humble/setup.bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake my_first_pkg --dependencies rclcpp
cd ~/ros2_ws
colcon build --packages-select my_first_pkg
source install/setup.bash
```

## 安装 vscode

### 下载 vscode

网站：https://code.visualstudio.com/docs/?dv=linux64_deb
下载对应版本（注意需要下载后缀为.deb的文件）

### 运行安装程序 使用 dpkg 命令安装

``` bash
sudo dpkg -i ~/Downloads/code_1.101.2-1750797935_amd64.deb #code_1.101.2-1750797935_amd64.deb 替换为下载的安装包名称
#Downloads 下载文件储存的位置
```

#### 解决依赖问题（如果有）

如果安装时提示依赖缺失，执行：

```bash
sudo apt --fix-broken install
```

#### 验证vscode安装

打开终端启动 VS Code

```bash
code .
```

#### 检查vscode版本

```bash
code --version
```

#### 安装vscode插件

快捷键 ctrl+shift+x打开插件商店
搜索插件名称，安装插件
插件名称：chinese - Simplified Chinese（看自己需要，可以让vscode显示为中文,但在虚拟机里不能打中文，虚拟机要设置成英文，代码里除了注释，必须全部为英文）
插件名称：C/C++，cmake,cmake-tools(如果你要用c语言写这是最基础的c语言插件）
插件名称：python(直接在插件商店搜python下载第一个，里面自带三个python插件)
插件名称：ros2(两个一个圆形图标，一个方形的都要下载)，urdf,XML,YAML

## 安装 moveit2

### 安装 MoveIt 2 核心包

#### 更新系统软件包

```bash
sudo apt update && sudo apt upgrade -y
```

#### 安装 MoveIt 2 官方包

```bash
sudo apt install ros-humble-moveit
```

### 从源码安装 moveit_py(后续调用python接口时需要,我的文件里已经全部下载了，这些可以省略，你自己建立工作空间的话，看需求下载)

### 你可以通过以下步骤将 moveit_py 添加到你的 ROS 2 工作区中并编译使用

#### 下载 moveit2_tutorials（其中包含 moveit_py）

```bash
cd ~/Desktop/ROS_ROBOT/src

# 克隆 MoveIt tutorials（包含 moveit_py 示例）
git clone -b humble https://github.com/ros-planning/moveit2_tutorials.git

# 克隆依赖的 Python API
git clone -b humble https://github.com/ros-planning/moveit2.git
```

### 下载rosdep

``` bash
sudo apt update
sudo apt install python3-rosdep
```

### 初始化 rosdep(每次要用rosdep必须初始化)

``` bash
sudo rosdep init
rosdep update
```

### 安装依赖

``` bash
cd ~/Desktop/ROS_ROBOT
rosdep install -r --from-paths src --ignore-src -y
```

## 编译工作空间

``` bash
cd Desktop/ROS_ROBOT
source /opt/ros/humble/setup.bash
rm -rf build install log  # 删除旧的构建、安装和日志目录
colcon build --symlink-install
source install/setup.bash
```

第一次编译需要15-30分钟左右

## 运行我写的demo文件

### cd到demo文件目录(这一步是为了测试urdf文件是否有损坏，使用rviz来可视化) 

``` bash
cd Desktop/ROS_ROBOT
source install/setup.bash
cd ~/Desktop/ROS_ROBOT/src/cpp06_urdf/launch
clear
ros2 launch display_robot.launch.py 
```

运行成功后，会打开一个rviz界面，这时候里面没有机器人，别担心很正常，点击左下角的add按钮，往下翻到最后选择RobotModel，点击Ok，接下来导入模型文件，先解决报错，在Global Options下的Fixed Frame选择bash_link,接下来导入urdf文件，点击RobotModel左边的小三角，选择Description Source将Topic换成File，下面选择Description File点击最后的...，退到cpp06_urdf目录下，进入urdr/urdf选择arm_BRTIRUS0805A_SLDASM.urdf点击open打开，现在可以看到机械臂模型了，只能看，不能动，但这不是一定动不了的，打开一个新的终端运行下面代码

```bash
source /opt/ros/humble/setup.bash
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

滑动滑块控制各个关节的旋转角度

### 接下来调用moveit的python接口通过输入末端坐标值，机器人自动规划路径移动

打开一个新终端，输入以下命令

``` bash
cd Desktop/ROS_ROBOT
source install/setup.bash
cd ~/Desktop/ROS_ROBOT/src/test_moveit_config/launch
clear
ros2 launch test_moveit_config demo.launch.py 
```

打开一个新终端，输入以下命令

``` bash
cd Desktop/ROS_ROBOT
source install/setup.bash
cd ~/Desktop/ROS_ROBOT/src/test_moveit_config/scripts
clear
python3 moveit_ik_demo.py
```

确保第一个终端的命令完全启动后再运行第二个终端的命令，我写的代码需要在第一个终端命令运行后，才能调用moveit的接口，如果启动过早会卡在withing，关闭重新等第一个rvie页面加载出来再运行第二个终端的命令运行后终端会打印机械臂起始坐标值，转到rviz页面查看,机械臂就开始规划运动了

### moveit_ik_input.py的介绍使用

moveit_ik_input作为moveit_ik_demo.py升级版本，我在其中加入了可交互命令，现在使用者可以在终端连续输入坐标值就可以进行运动学规划，可以在rviz中查看运动轨迹


打开一个新终端，输入以下命令

``` bash
cd Desktop/ROS_ROBOT
source install/setup.bash
cd ~/Desktop/ROS_ROBOT/src/test_moveit_config/launch
clear
ros2 launch test_moveit_config demo.launch.py 
```

打开一个新终端，输入以下命令

``` bash
cd Desktop/ROS_ROBOT
source install/setup.bash
cd ~/Desktop/ROS_ROBOT/src/test_moveit_config/scripts
clear
python3 moveit_ik_input.py
```

确保第一个终端的命令完全启动后再运行第二个终端的命令，我写的代码需要在第一个终端命令运行后，才能调用moveit的接口，如果启动过早会卡在withing，关闭重新等第一个rvie页面加载出来再运行第二个终端的命令运行后终端会打印机械臂起始坐标值，转到rviz页面查看,机械臂就开始规划运动了

### 封装成Api接口以便于在windows下调用

下载依赖

```.bash
source /opt/ros/humble/setup.bash 
#如果提示 pip3: command not found，先安装 pip：
sudo apt update && sudo apt install python3-pip
pip3 install pydantic
```

安装成功后，终端会显示类似信息
Successfully installed pydantic-2.4.2 ...

```.bash
pip3 install fastapi uvicorn
```

### Api代码结构讲解

```.tree
├── Api/
│   ├── __init__.py   ✅ 空文件
│   ├── ik_Api.py
│   ├── ik_node.py    ✅  封装 ROS 2 Node 与 IK 服务调用
│   ├── models.py     ✅  定义输入数据结构（Pydantic 模型）
```

除了我上面特别注释的三个文件之外，其他文件都是封装的代码，具体请看代码
ik_Api.py单独封装了一个调用逆运动学的代码
运行指令
需要到ROS_ROBOT/src/test_moveit_config这个路径下
于此同时需要先启动 ros2 launch test_moveit_config demo.launch.py（具体启动步骤看上面）

```.bash
uvicorn Api.ik_Api:app --reload --host 0.0.0.0 --port 8000
```

运行成功后，在主机上打开浏览器访问 http://<你的虚拟机IP>:8000可以看到接口文档

⚠️ 主机必须和虚拟机在同一个网段下才可以访问

| 代码名     | 作用  | 描述       |
| :------- | :---: | ---------: |
| moveit_ik_demo     | 简单的运动学测试可视化代码    | 需要结合demo.launch来进行可视化，会有报错，不影响，这个只是测试代码为了看效果罢了       |
| moveit_ik_input     | 连续输入坐标值进行运动学规划可视化    | 需要结合demo.launch来使用，因为基于moveit_ik_demo编写的存在问题，但是不会报错       |
| maker_test    | 生成一个小方块在rviz空间中显示       | 上需要结合moveit_rviz.launch使用       |
| joint_start_end_point_test    | 机械臂的起点和终点的可视化    | 需要结合demo.launch来使用       |
| joint_end_point     | 机械臂的终点可视化    | 需要结合demo.launch来使用       |
| ik_mathematical_calculation     | 机械臂调用moveit里函数进行逆运动学计算    | 直接运行即可       |
| ik_mathematical_calculation_safe     | 机械臂调用moveit里函数进行逆运动学计算不可修改计算出的关节角度值，调用更安全    | 直接运行即可       |
| ik_path_paining_test     | 使用直接定义的弧度值来规划路径测试   | 需要结合demo.launch来使用       |
| ik_path_paining_test     | 机械臂调用moveit里函数进行路径规划可视化调用了ik_mathematical_calculation_safe的逆运动学计算结果    | 需要结合demo.launch来使用       |
| tcp_client_node      | 网络传输文本数据的测试版    | 需要结合网络调试助手进行测试      |
| send_joint_angles_over_the_network      | 网络传输josn文本数据    | 调用了ik_mathematical_calculation_safe的逆运动学计算结果里的角度值，需要结合网络调试助手进行测试      |
quaternion_mathematical_calculation_test      | 计算四元数测试代码    | 四元数用来表示机械臂末端的转动角度，直接输入x加角度即可，测试版，一次只能计算绕一个轴旋转的四元数，示例输入 x 45    |
| quaternion_mathematical_calculation      | 计算四元数代码可计算多个轴旋转的四元数    | 四元数用来表示机械臂末端的转动角度，计算多个轴旋转的角度，输入示例x 60 y 60 z轴可输入也可不输入，不输入默认为零，x,y同理    |
| ik_quaternion_combined      | 计算四元数代码并解算角度   | 先输入坐标点，接下来输入需要绕多个轴旋转的角度，直接输入角度即可，不转输入0，后续会进行自动计算，并打印在终端   |

## 需要了解的知识

### python结构知识

__init__.py 是一个特殊文件，用于告诉 Python 运行时，这个目录下的所有文件都是模块。
它本身是一个空文件，规范代码的时候很有必要

### 四元数

四元数（Quaternion）是一种数学工具，主要用于高效表示和计算 3D 空间中的旋转，在机器人学、计算机图形学、航空航天等领域被广泛应用（代码中用它表示机械臂末端的朝向）。 

四元数是复数的扩展。它包含 1 个实部和 3 个虚部，数学表达式为：q=w+xi+yj+zk

w是实部；x,y,z是虚部；i,j,k是虚数单位，且满足特殊的乘法规则：i²=j²=k²=−1，
ij=k,ji=−k,jk=i,kj=−i,ki=j,ik=−j。

w 是四元数的实部，有明确的物理意义，它与旋转角度直接相关。假设一个旋转是 “绕单位向量 (a, b, c) 旋转 θ 角度”，那么对应的四元数分量为：

```bash
w = cos(θ/2)  
x = a · sin(θ/2)  
y = b · sin(θ/2)  
z = c · sin(θ/2)
```

#### 例如绕x和y轴旋转60° 的四元数分量为：（注意：前提先绕x轴旋转60°再绕y轴旋转60°，顺序不同会导致旋转结果不同）

绕 x 轴旋转 60° 的四元数（记为 Qₓ）
旋转轴为 x 轴，单位向量为(1, 0, 0)，
角度 θ=60°，θ/2=30°，
计算分量：

```bash
wₓ = cos(30°) = √3/2 ≈ 0.866  
xₓ = 1·sin(30°) = 1·0.5 = 0.5  
yₓ = 0·sin(30°) = 0  
zₓ = 0·sin(30°) = 0  
```

所以 Qₓ = (√3/2, 0.5, 0, 0)

绕 y 轴旋转 60° 的四元数（记为 Qᵧ）
旋转轴为 y 轴，单位向量为(0, 1, 0)，
角度 θ=60°，θ/2=30°，
计算分量：

```bash
wᵧ = cos(30°) = √3/2 ≈ 0.866  
xᵧ = 0·sin(30°) = 0  
yᵧ = 1·sin(30°) = 0.5  
zᵧ = 0·sin(30°) = 0  
```

所以 Qᵧ = (√3/2, 0, 0.5, 0)

#### 计算组合旋转的四元数（Q = Qᵧ × Qₓ）

旋转顺序是 “先绕 x 轴转 60°，再绕 y 轴转 60°”，则组合四元数 Q 为：Q = Qᵧ × Qₓ（后旋转的 Qᵧ放在左边，先旋转的 Qₓ放在右边）。

四元数乘法公式(涉及到了向量叉乘计算，不懂的自己找相关资料)

两个四元数Qa = (wₐ, xₐ, yₐ, zₐ)和Qb = (wᵦ, xᵦ, yᵦ, zᵦ)的乘积为：

```bash
w = wₐwᵦ - xₐxᵦ - yₐyᵦ - zₐzᵦ  
x = wₐxᵦ + xₐwᵦ + yₐzᵦ - zₐyᵦ  
y = wₐyᵦ - xₐzᵦ + yₐwᵦ + zₐxᵦ  
z = wₐzᵦ + xₐyᵦ - yₐxᵦ + zₐwᵦ  
```

代入 Qᵧ和 Qₓ计算 Q

Qᵧ = (√3/2, 0, 0.5, 0)，Qₓ = (√3/2, 0.5, 0, 0)，代入公式：

w 分量：

```bash
w = (√3/2)(√3/2) - (0)(0.5) - (0.5)(0) - (0)(0) = (3/4) - 0 - 0 - 0 = 3/4 = 0.75
```

x 分量：

```bash
x = (√3/2)(0.5) + (0)(√3/2) + (0.5)(0) - (0)(0) = (√3/4) + 0 + 0 - 0 = √3/4 ≈ 0.433
```

y 分量：

```bash
y = (√3/2)(0) - (0)(0) + (0.5)(√3/2) + (0)(0.5) = 0 - 0 + (√3/4) + 0 = √3/4 ≈ 0.433
```

z 分量：

```bash
z = (√3/2)(0) + (0)(0) - (0.5)(0.5) + (0)(√3/2) = 0 + 0 - 0.25 + 0 = -0.25
```

#### 最终结果

绕 x 轴旋转 60° 后再绕 y 轴旋转 60° 的四元数为：

(w, x, y, z) = (0.75, √3/4, √3/4, -0.25)

(数值近似：(0.75, 0.433, 0.433, -0.25))