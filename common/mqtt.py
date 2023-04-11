from umqtt.simple import MQTTClient
from machine import Pin
import time
import wifi

ssid="sss"
passwd="lyz20200802"
client_id = "slim_id"
mserver = '192.168.0.135'
port=1883

topic_ctl = b'led_ctl'#设备订阅的主题,客户端推送消息的主题
topic_sta = b'led_sta'#客户端订阅的主题,设备推送消息的主题
client = None

    
def sub_callback(topic, msg):
    """
    收到订阅消息回调
    """
    global client
    pub_msg=''
    print((topic_ctl, msg))
    
    client.publish(topic_sta, pub_msg, retain=True)

try:
    wifi.do_connect(ssid,passwd)
    client = MQTTClient(client_id, mserver, 0)
    client.set_callback(sub_callback)
    client.connect()
    client.subscribe(topic_ctl)
    client.publish(topic_sta, 'ESP32 Device online', retain=True)
    print("Connected to %s, subscribed to %s topic" % (mserver, topic_ctl))
    while True:
        client.wait_msg()
finally:
    if client is not None:
        print('off line')
        client.disconnect()
    wifi.wlan.disconnect()
    wifi.wlan.active(False)

