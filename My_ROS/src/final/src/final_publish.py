#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
def talker():
    pub = rospy.Publisher('std_id', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        my_id = 6352500790
        rospy.loginfo(my_id)
        pub.publish(my_id)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass