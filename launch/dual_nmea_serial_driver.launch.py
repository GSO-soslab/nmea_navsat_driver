import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('nmea_navsat_driver')
    
    # Define the path to the parameter file
    params_file = os.path.join(pkg_share_dir, 'config', 'dual_nmea_serial_driver.yaml')

    # Node for the primary GPS device
    gps_primary_node = Node(
        package='nmea_navsat_driver',
        executable='nmea_serial_driver',
        name='gps_primary',
        output='screen',
        emulate_tty=True,
        parameters=[params_file],
        remappings=[
            ("/fix", "primary/fix"),
            ("/heading", "primary/heading"),
            ("/vel", "primary/vel"),
            ("/time_reference", "primary/time_reference"),
        ]
    )

    # Node for the secondary GPS device
    gps_secondary_node = Node(
        package='nmea_navsat_driver',
        executable='nmea_serial_driver',
        name='gps_secondary',
        output='screen',
        emulate_tty=True,
        parameters=[params_file],
        remappings=[
            ("/fix", "secondary/fix"),
            ("/heading", "secondary/heading"),
            ("/vel", "secondary/vel"),
            ("/time_reference", "secondary/time_reference"),
        ]
    )

    return LaunchDescription([
        gps_primary_node,
        gps_secondary_node
    ])