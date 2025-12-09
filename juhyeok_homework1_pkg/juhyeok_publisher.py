import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class JuhyeokPublisher(Node):
    def __init__(self):
        super().__init__('JuhyeokPublisher')
        self.publisher_ = self.create_publisher(String, 'JuhyeokTopic', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"string: hello | integer: {self.count} | float64: {float(self.count) + 0.1}"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = JuhyeokPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
