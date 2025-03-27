import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy

from dronekit import Vehicle, connect

class VehicleStatusViewer(Node):

    def __init__(self):
        super().__init__('vehicle_status_viewer')
        
        self.qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1
        )
        
        self.drone = connect('/dev/ttyACM0', baud=115200, wait_ready=True)
        self.drone.wait_ready('autopilot_version')
        fps = 100
        self.create_timer(1.0/fps, self.status_callback)
        
    def status_callback(self):
        self.get_logger().info(f'Arming State: {self.drone.armed}')
        self.get_logger().info(f'Attitude: {self.drone.attitude}')
        self.get_logger().info(f'Velocity: {self.drone.velocity}')
        
def main(args=None):
    rclpy.init(args=args)
    vehicle_status_viewer = VehicleStatusViewer()
    try:
        while True:
            rclpy.spin_once(vehicle_status_viewer)
    except KeyboardInterrupt:
        pass
    vehicle_status_viewer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

