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