include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = map_builder,
  trajectory_builder = trajectory_builder,
  map_frame = "map",
  tracking_frame = "base_link",  -- 根据机器人的坐标系修改
  published_frame = "base_link",
  odom_frame = "odom",
  provide_odom_frame = true,
  use_odometry = true,          -- 如果使用里程计则设为 true
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 1,           -- 激光雷达数量
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 0,
  lookup_transform_timeout_sec = 0.2,
  submap_publish_period_sec = 0.3,
  pose_publish_period_sec = 5e-3,
  trajectory_publish_period_sec = 30e-3,
}

MAP_BUILDER.use_trajectory_builder_2d = true
TRAJECTORY_BUILDER_2D.num_accumulated_range_data = 1
TRAJECTORY_BUILDER_2D.use_imu_data = true  -- 如果使用 IMU 则设为 true

return options