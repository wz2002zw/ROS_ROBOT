# Install script for directory: /home/wz/Desktop/ROS_ROBOT/src/moveit2/moveit_ros/visualization

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_visualization")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/ament_cmake_symlink_install/ament_cmake_symlink_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/robot_state_rviz_plugin/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/motion_planning_rviz_plugin/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/trajectory_rviz_plugin/cmake_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/motion_planning_rviz_plugin/libmoveit_motion_planning_rviz_plugin.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/motion_planning_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_robot_interaction/lib:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/motion_planning_rviz_plugin/libmoveit_motion_planning_rviz_plugin.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/motion_planning_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_robot_interaction/lib:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/motion_planning_rviz_plugin/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_robot_interaction/lib:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/motion_planning_rviz_plugin/libmoveit_motion_planning_rviz_plugin_core.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_robot_interaction/lib:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_motion_planning_rviz_plugin_core.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin/libmoveit_planning_scene_rviz_plugin.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin/libmoveit_planning_scene_rviz_plugin.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin/libmoveit_planning_scene_rviz_plugin_core.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_planning_scene_rviz_plugin_core.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/robot_state_rviz_plugin/libmoveit_robot_state_rviz_plugin.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/robot_state_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/robot_state_rviz_plugin/libmoveit_robot_state_rviz_plugin.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/robot_state_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/robot_state_rviz_plugin/libmoveit_robot_state_rviz_plugin_core.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/robot_state_rviz_plugin/libmoveit_robot_state_rviz_plugin_core.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_robot_state_rviz_plugin_core.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools/libmoveit_rviz_plugin_render_tools.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools/libmoveit_rviz_plugin_render_tools.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_rviz_plugin_render_tools.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/trajectory_rviz_plugin/libmoveit_trajectory_rviz_plugin.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/trajectory_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/trajectory_rviz_plugin/libmoveit_trajectory_rviz_plugin.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/trajectory_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so.2.5.9"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/trajectory_rviz_plugin/libmoveit_trajectory_rviz_plugin_core.so.2.5.9")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so.2.5.9" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so.2.5.9")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so.2.5.9"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/opt/ros/humble/opt/rviz_ogre_vendor/lib:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so.2.5.9")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/trajectory_rviz_plugin/libmoveit_trajectory_rviz_plugin_core.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/planning_scene_rviz_plugin:/opt/ros/humble/opt/rviz_ogre_vendor/lib:/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/rviz_plugin_render_tools:/opt/ros/humble/lib/x86_64-linux-gnu:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_trajectory_rviz_plugin_core.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/moveit_ros_visualization/cmake/export_moveit_ros_visualizationExport.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/moveit_ros_visualization/cmake/export_moveit_ros_visualizationExport.cmake"
         "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/CMakeFiles/Export/share/moveit_ros_visualization/cmake/export_moveit_ros_visualizationExport.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/moveit_ros_visualization/cmake/export_moveit_ros_visualizationExport-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/moveit_ros_visualization/cmake/export_moveit_ros_visualizationExport.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_ros_visualization/cmake" TYPE FILE FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/CMakeFiles/Export/share/moveit_ros_visualization/cmake/export_moveit_ros_visualizationExport.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_ros_visualization/cmake" TYPE FILE FILES "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/CMakeFiles/Export/share/moveit_ros_visualization/cmake/export_moveit_ros_visualizationExport-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/wz/Desktop/ROS_ROBOT/build/moveit_ros_visualization/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
