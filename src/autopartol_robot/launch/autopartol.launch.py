import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # 获取与拼接默认路径
    autopartol_robot_dir = get_package_share_directory(
        'autopartol_robot')
    partol_config_path = os.path.join(
        autopartol_robot_dir, 'config', 'partol_config.yaml')
    
    action_node_turtle_control = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='partol_node',
        output = 'screen',
        parameters=[partol_config_path]
    )
    action_node_partol_client = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='speaker',
        output = 'screen'
    )

    return launch.LaunchDescription([
        action_node_turtle_control,
        action_node_partol_client,
    ])