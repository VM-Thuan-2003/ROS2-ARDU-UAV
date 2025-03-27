from setuptools import setup

setup(
    name='common',
    version='0.0.0',
    packages=['common'],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/common']),
        ('share/common', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Albert Benjamin',
    maintainer_email='vmthuan16052003@gmail.com',
    description='Common utilities for ROS2-Ardu UAV',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

        ],
    },
)

