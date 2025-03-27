import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy

from dronekit import Vehicle, connect

class VehicleMain(Node):

    def __init__(self):
        super().__init__('vehicle_main')
        
        self.qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1
        )
        
        self.drone = connect('/dev/ttyUSB0', baud=921600, wait_ready=True)
        self.drone.wait_ready('autopilot_version')
        fps = 100
        self.create_timer(1.0/fps, self.status_callback)
        
    def status_callback(self):
        self.get_logger().info(f'Arming State: {self.drone.armed}')
        self.get_logger().info(f'Attitude: {self.drone.attitude}')
        self.get_logger().info(f'Velocity: {self.drone.velocity}')
        
def main(args=None):
    rclpy.init(args=args)
    vehicle_main = VehicleMain()
    try:
        while True:
            rclpy.spin_once(vehicle_main)
    except KeyboardInterrupt:
        pass
    vehicle_main.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

