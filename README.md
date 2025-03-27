# ROS2-ARDU-UAV

## ROS 2 Launch with Virtual Environment Support

This guide explains how to configure and use a **ROS 2 launch file** that automatically runs nodes inside a virtual environment.

### **1. Setting Up the Virtual Environment**
Before launching the ROS 2 nodes, you must create and activate a virtual environment.

Run the following command in your workspace root:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### **2. Launching the ROS 2 Launch File**
To make sure ROS 2 nodes run inside the virtual environment, we modify the launch file.

Step 1: Create a ROS 2 Launch File

Create a file launch.py inside the launch directory of your ROS 2 package:

```python
import os
from launch import LaunchDescription
from launch_ros.actions import Node

# Define the virtual environment path
venv_path = os.path.join(os.getcwd(), "venv")

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_ardu_uav',
            executable='node_name',
            output='screen',
            env={'VIRTUAL_ENV': venv_path, 'PATH': f"{venv_path}/bin:" + os.environ['PATH']},
        )
    ])
```

Step 2: Build the ROS 2 Package

Navigate to your ROS 2 workspace and build the package:

```bash
colcon build --symlink-install
```

Then, source the setup file:

```bash
source install/setup.bash
```

Step 3: Launch the ROS 2 Launch File

```bash
ros2 launch ros2_ardu_uav launch.py
```

