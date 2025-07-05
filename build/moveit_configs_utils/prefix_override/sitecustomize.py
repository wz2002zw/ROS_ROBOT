import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wz/Desktop/ROS_ROBOT/install/moveit_configs_utils'
