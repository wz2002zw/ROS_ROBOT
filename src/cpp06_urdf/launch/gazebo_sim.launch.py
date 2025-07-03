import launch
import launch_ros
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf_packages_path = get_package_share_directory("cpp06_urdf")
    default_xacro_path = os.path.join(urdf_packages_path, 'urdf', 'xacro', 'car.urdf.xacro')
    default_gazebo_world_path = os.path.join(urdf_packages_path, 'worlds', 'house3')
    controllers_yaml_path = os.path.join(urdf_packages_path, 'config', 'car_controller.yaml')

    # 声明参数
    declare_model_arg = DeclareLaunchArgument(
        name='model',
        default_value=default_xacro_path,
        description='Xacro/URDF 模型文件路径'
    )

    # 生成机器人描述
    robot_description_value = launch_ros.parameter_descriptions.ParameterValue(
        Command(['xacro ', LaunchConfiguration('model')]),
        value_type=str
    )

    # 启动 robot_state_publisher
    robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description_value}]
    )

    # 启动 Gazebo
    launch_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': default_gazebo_world_path}.items()
    )

    # 延迟 5 秒后，在 Gazebo 中生成机器人
    spawn_entity = TimerAction(
        period=5.0,
        actions=[
            launch_ros.actions.Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=['-entity', 'my_robot', '-topic', '/robot_description', '-x', '0.0', '-y', '0.0', '-z', '0.1'],
                output='screen'
            )
        ]
    )

    # 启动 controller_manager
    controller_manager = launch_ros.actions.Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[controllers_yaml_path],
        output="screen"
    )

    # 加载控制器
    load_joint_state_broadcaster = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', 'joint_state_broadcaster', '--set-state', 'active'],
        output='screen'
    )

    load_effort_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', 'car_effort_controller', '--set-state', 'active'],
        output='screen'
    )   

    load_diff_drive_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', 'car_diff_drive_controller', '--set-state', 'active'],
        output='screen'
    ) 

    return launch.LaunchDescription([
        declare_model_arg,
        robot_state_publisher,
        launch_gazebo,
        spawn_entity,
        controller_manager,
        TimerAction(period=3.0, actions=[load_joint_state_broadcaster]),
        TimerAction(period=6.0, actions=[load_effort_controller, load_diff_drive_controller]),
    ])
