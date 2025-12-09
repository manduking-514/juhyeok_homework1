import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class JuhyeokSubscriber(Node):
    def __init__(self):
        super().__init__('JuhyeokSubscriber')
        self.subscription = self.create_subscription(
            String,
            'JuhyeokTopic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = JuhyeokSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
