import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('nmea_navsat_driver')
    
    # Define the path to the parameter file
    params_file = os.path.join(pkg_share_dir, 'config', 'single_nmea_serial_driver.yaml')

    # Node for the primary GPS device
    gps_primary_node = Node(
        package='nmea_navsat_driver',
        executable='nmea_serial_driver',
        name='gps_primary',
        output='screen',
        emulate_tty=True,
        parameters=[params_file],
        remappings=[
            ("/fix", "gps_primary/fix"),
            ("/heading", "gps_primary/heading"),
            ("/vel", "gps_primary/vel"),
            ("/time_reference", "gps_primary/time_reference"),
            ("/gga", "gps_primary/gga"),
        ]
    )

    return LaunchDescription([
        gps_primary_node
    ])