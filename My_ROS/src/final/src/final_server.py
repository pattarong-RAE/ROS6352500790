#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy

def server_callback(req):
    print("“Hi, My name is Pattarong Sombatkaew")
    return EmptyResponse()

def trigger_server():
    rospy.init_node('trigger_server')
    s = rospy.Service('hi', Empty, server_callback)
    print("Ready to do something.")
    rospy.spin()

if __name__ == "__main__":
    trigger_server()