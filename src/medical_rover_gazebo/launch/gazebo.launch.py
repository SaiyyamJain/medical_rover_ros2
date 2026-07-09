from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
from launch.actions import TimerAction

import os


def generate_launch_description():

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"),
                "launch",
                "gazebo.launch.py"
            )
        )
    )

    pkg_path = get_package_share_directory("medical_rover_description")

    robot_file = os.path.join(
        pkg_path,
        "urdf",
        "medical_rover.urdf.xacro"
    )

    robot_description = ParameterValue(
        Command(["xacro"," ", robot_file]),
        value_type=str
    )

    robot_state_publisher = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    parameters=[
        {"robot_description": robot_description}
    ]
    )

    spawn_entity = Node(
    package="gazebo_ros",
    executable="spawn_entity.py",
    arguments=[
        "-topic", "robot_description",
        "-entity", "medical_rover"
    ],
    output="screen"
    )

    delayed_spawn = TimerAction(
    period=5.0,
    actions=[spawn_entity]
    )


    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        delayed_spawn
])
