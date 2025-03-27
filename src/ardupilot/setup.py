from setuptools import setup

setup(
    name='ardupilot',
    version='0.0.0',
    packages=['ardupilot', 'dronekit'],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/ardupilot']),
        ('share/ardupilot', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Albert Benjamin',
    maintainer_email='vmthuan16052003@gmail.com',
    description='ardupilot utilities for ROS2-Ardu UAV',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vehicle_status = ardupilot.vehicle_status:main',
        ],
    },
)

