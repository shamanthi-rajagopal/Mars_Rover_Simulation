import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_name',
            default_value='mars_rover',
            description='Name of the robot'
        ),
        Node(
            package='mars_rover',  # ROS 2 package name
            executable='rover_simulation',  # Script or executable name
            name='mars_rover_simulation',
            output='screen'
        )
    ])
