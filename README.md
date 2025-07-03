<<<<<<< HEAD
# 这是ROS2humble版本运行下面的代码需要提前做的准备(使用RVIZ和Gazebo仿真)
## 仿真视频
https://www.bilibili.com/video/BV1tMoiYYERN/?spm_id_from=333.1387.homepage.video_card.click&vd_source=a54d7b70061d23cd9317111e80b3830b

参考鱼香ROS视频
https://www.bilibili.com/video/BV1CB19Y1Ew8?spm_id_from=333.788.videopod.sections&vd_source=a54d7b70061d23cd9317111e80b3830b

赵虚左
https://www.bilibili.com/video/BV12e4y1C7Ns/?spm_id_from=333.1387.favlist.content.click&vd_source=a54d7b70061d23cd9317111e80b3830b

```bash
1  sudo apt update
    2  sudo apt install open-vm-tools-desktop
    3  reboot
    4  gsettings set org.gnome.desktop.interface text-scaling-factor 1.5
    5  sudo apt install terminator
    6  wget http://fishros.com/install -O fishros && . fishros
    7  sudo apt-get install ros-humble-ros2-control ros-humble-ros2-controllers

	sudo apt install ros-humble-gazebo-ros2-control

    8  sudo apt install open-vm-tools open-vm-tools-desktop
    9  sudo apt-get install ros-humble-turtle-tf2-py ros-humble-tf2-tools ros-humble-tf-transformations 
   10  sudo apt install python3-pip
   11  pip3 install transforms3d
   12  pip3 show transforms3d
   13  sudo apt install ros-humble-joint-state-publisher
   14  sudo apt install ros-humble-joint-state-publisher-gui
   15  sudo apt install ros-humble-xacro
   16  sudo apt install liburdfdom-tools
   17  sudo apt install gazebo
   18  mkdir -p ~/.gazebo
   19  cd ~/.gazebo
   20  ls
   25  sudo apt install git
   26  git clone https://gitee.com/ohhuo/gazebo_models.git
   27  rm -rf ~/.gazebo/models.git
   28  cd ../
   29  sudo apt install ros-$ROS_DISTRO-gazebo-ros-pkgs
   30  sudo apt install ros-$ROS_DISTRO-joint-state-publisher
   31  sudo apt install ros-$ROS_DISTRO-robot-state-publisher
   32  sudo apt-get install ros-humble-joy
   33  sudo apt-get install ros-humble-joy-teleop
   34  sudo apt install ros-humble-slam-toolbox
   35  sudo apt install ros-humble-nav2-map-server
   36  sudo apt install ros-humble-navigation2
   37  sudo apt install ros-humble-nav2-bringup
   38  sudo apt install ros-humble-urdf-tutorial
   39  sudo apt install ros-humble-tf2-tools
   40  ssh-keygen -t ed25519 -C "dayangyouxia"
   41  cat ~/.ssh/id_ed25519.pub
   42  git clone -b master git@github.com:fullexpectation/NanoRobot.git
   43   nano ~/.bashrc 
   53# >>> fishros initialize >>>
source /opt/ros/humble/setup.bash
# <<< fishros initialize <<<
source ~/NanoRobot/install/setup.bash
```



# 这是两轮差速小车rviz和gazebo仿真代码
```bash
ros2 launch cpp06_urdf gazebo_sim.launch.py 
```
```bash
ros2 launch car_navigation2 navigation2.launch.py 
```
```bash
ros2 launch autopartol _robot autopartol.launch.py
```
---------------

打开rviz小车模型
```bash
ros2 launch cpp06_urdf display.launch.py model:=`ros2 pkg prefix --share cpp06_urdf`/urdf/xacro/car.urdf.xacro
```
---------------
使用slam_toolbox建图
```bash
sudo apt install ros-humble-slam-toolbox

```
```bash
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
```
rqt
```bash
sudo apt install ros-humble-nav2-map-server
```
保存地图
```bash
ros2 run nav2_map_server map_saver_cli -f room
```
------------------
=======
# ROS_ROBOT
>>>>>>> 1ff43fe19b84ebd979c67345ebb4d7bd63b6a635
