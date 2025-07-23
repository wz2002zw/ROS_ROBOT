# Api/ik_node.py
import sys, os

# 将上级目录（test_moveit_config）加入 sys.path，确保能找到 scripts 包
current_dir = os.path.dirname(__file__)  # Api/
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# 现在可以当包导入
from scripts.ik_mathematical_calculation_safe import SimpleIKTester