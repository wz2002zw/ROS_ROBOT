# Install script for directory: /home/wz/Desktop/ROS_ROBOT/src/moveit2/moveit_planners/pilz_industrial_motion_planner

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/wz/Desktop/ROS_ROBOT/install/pilz_industrial_motion_planner")
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
  include("/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/ament_cmake_symlink_install/ament_cmake_symlink_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libpilz_industrial_motion_planner.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libpilz_industrial_motion_planner.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libpilz_industrial_motion_planner.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libpilz_industrial_motion_planner.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libpilz_industrial_motion_planner.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libpilz_industrial_motion_planner.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libpilz_industrial_motion_planner.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libpilz_industrial_motion_planner.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjoint_limits_common.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjoint_limits_common.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjoint_limits_common.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libjoint_limits_common.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjoint_limits_common.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjoint_limits_common.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjoint_limits_common.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjoint_limits_common.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_base.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_base.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_base.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libplanning_context_loader_base.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_base.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_base.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_base.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_base.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_ptp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_ptp.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_ptp.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libplanning_context_loader_ptp.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_ptp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_ptp.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_ptp.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_ptp.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_lin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_lin.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_lin.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libplanning_context_loader_lin.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_lin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_lin.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_lin.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_lin.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_circ.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_circ.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_circ.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libplanning_context_loader_circ.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_circ.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_circ.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_circ.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libplanning_context_loader_circ.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcommand_list_manager.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcommand_list_manager.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcommand_list_manager.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libcommand_list_manager.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcommand_list_manager.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcommand_list_manager.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcommand_list_manager.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcommand_list_manager.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsequence_capability.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsequence_capability.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsequence_capability.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libsequence_capability.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsequence_capability.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsequence_capability.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsequence_capability.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsequence_capability.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libtrajectory_generation_common.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libtrajectory_generation_common.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libtrajectory_generation_common.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/libtrajectory_generation_common.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libtrajectory_generation_common.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libtrajectory_generation_common.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libtrajectory_generation_common.so"
         OLD_RPATH "/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning_interface/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_move_group/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_warehouse/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_planning/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_ros_occupancy_map_monitor/lib:/home/wz/Desktop/ROS_ROBOT/install/moveit_core/lib:/opt/ros/humble/lib:/opt/ros/humble/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libtrajectory_generation_common.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/test/cmake_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/pilz_industrial_motion_planner/cmake/pilz_industrial_motion_plannerTargetsExport.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/pilz_industrial_motion_planner/cmake/pilz_industrial_motion_plannerTargetsExport.cmake"
         "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/CMakeFiles/Export/share/pilz_industrial_motion_planner/cmake/pilz_industrial_motion_plannerTargetsExport.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/pilz_industrial_motion_planner/cmake/pilz_industrial_motion_plannerTargetsExport-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/pilz_industrial_motion_planner/cmake/pilz_industrial_motion_plannerTargetsExport.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pilz_industrial_motion_planner/cmake" TYPE FILE FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/CMakeFiles/Export/share/pilz_industrial_motion_planner/cmake/pilz_industrial_motion_plannerTargetsExport.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pilz_industrial_motion_planner/cmake" TYPE FILE FILES "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/CMakeFiles/Export/share/pilz_industrial_motion_planner/cmake/pilz_industrial_motion_plannerTargetsExport-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/wz/Desktop/ROS_ROBOT/build/pilz_industrial_motion_planner/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
