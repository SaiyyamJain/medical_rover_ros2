from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os

def generate_launch_description():

    pkg_path = get_package_share_directory(
        "medical_rover_bringup"
    )

    slam_params = os.path.join(
        pkg_path,
        "config",
        "slam.yaml"
    )

    slam = Node(
        package="slam_toolbox",
        executable="async_slam_toolbox_node",
        output="screen",
        parameters=[
            slam_params,
            {"use_sim_time": True}
        ]
    )

    return LaunchDescription([
        slam
    ])