#!/usr/bin/env python3
 
import rclpy  # Import the ROS 2 client library for Python
from rclpy.node import Node  # Import the Node class
from std_msgs.msg import String  # Import the String message type

class Carico_Publisher_Subscriber(Node):

    def __init__(self):
        # set node's name
        super().__init__('carico_publisher_subscriber')

        self.textv3 = 0

        # set up the subscriber
        self.subscriber_1 = self.create_subscription(
            String,
            '/marco_polo',
            self.listener_callback,
            10)
 
        # set up the publisher
        self.publisher_1 = self.create_publisher(String, '/carico', 10)
 
        # timer for messages delay
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)
 
    def listener_callback(self, msg):

        text = len(msg.data) * 40
        textv2 = text / 35
        self.textv3 = int(textv2)
 
    def timer_callback(self):
        # message type
        msg = String()

        msg.data = self.textv3
 
        # puslish message on the topic
        self.publisher_1.publish(msg)
 
        # log the published data
        self.get_logger().info('Number: "%s"' % msg.data)
 
def main(args=None):
    # initialize ros2 communication
    rclpy.init(args=args)
 
    # Create the single combined node
    carico_node = Carico_Publisher_Subscriber()
 
    # Spin the single node (this handles both the timer and subscription events)
    rclpy.spin(carico_node)
 
    # Clean cleanup
    carico_node.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()