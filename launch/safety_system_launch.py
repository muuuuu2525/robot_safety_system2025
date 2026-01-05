from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_safety_system',
            executable='sensor',
            output='screen'
        ),
        Node(
            package='robot_safety_system',
            executable='brake',
            output='screen'
        ),
    ])
