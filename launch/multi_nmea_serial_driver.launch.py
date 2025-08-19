import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('nmea_navsat_driver')
    
    # Define the path to the parameter file
    params_file = os.path.join(pkg_share_dir, 'config', 'multi_nmea_serial_driver.yaml')

    # Node for the ublox GPS device
    gps_ublox_node = Node(
        package='nmea_navsat_driver',
        executable='nmea_serial_driver',
        name='gps_ublox',
        output='screen',
        emulate_tty=True,
        parameters=[params_file],
        remappings=[
            ("/fix", "gps_ublox/fix"),
            ("/heading", "gps_ublox/heading"),
            ("/vel", "gps_ublox/vel"),
            ("/time_reference", "gps_ublox/time_reference"),
            ("/gga", "gps_ublox/gga"),
        ]
    )

    # Node for the gps_rise GPS device
    gps_rise_node = Node(
        package='nmea_navsat_driver',
        executable='nmea_serial_driver',
        name='gps_rise',
        output='screen',
        emulate_tty=True,
        parameters=[params_file],
        remappings=[
            ("/fix", "gps_rise/fix"),
            ("/heading", "gps_rise/heading"),
            ("/vel", "gps_rise/vel"),
            ("/time_reference", "gps_rise/time_reference"),
            ("/gga", "gps_rise/gga"),
        ]
    )

    # Node for the gps_rise GPS device
    gps_img_node = Node(
        package='nmea_navsat_driver',
        executable='nmea_serial_driver',
        name='gps_img',
        output='screen',
        emulate_tty=True,
        parameters=[params_file],
        remappings=[
            ("/fix", "gps_img/fix"),
            ("/heading", "gps_img/heading"),
            ("/vel", "gps_img/vel"),
            ("/time_reference", "gps_img/time_reference"),
            ("/gga", "gps_img/gga"),
        ]
    )

    return LaunchDescription([
        gps_ublox_node,
        gps_rise_node,
        gps_img_node
    ])