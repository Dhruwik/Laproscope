import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro


def generate_launch_description():
    pkg_name = 'capstone'  # your package name
    xacro_file = os.path.join(
        get_package_share_directory(pkg_name),
        'description',
        'capstone.urdf.xacro'  # your URDF XACRO file
    )

    # Process the XACRO file to URDF
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # Robot state publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}]
    )

    # Joint state publisher GUI node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # RViz node (if you have an RViz config)
    rviz_config_file = os.path.join(
        get_package_share_directory(pkg_name),
        'view.rviz'  # or whatever your RViz config is named
    )
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
