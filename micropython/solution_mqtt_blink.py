from machine import Pin
from umqtt.simple import MQTTClient,MQTTException

LED_GPIO_2 = Pin(2, Pin.OUT)    # create output pin on LED_GPIO_2

mqtt_client_id='myId'
mqtt_broker=''
assert mqtt_broker!='', 'Oh no! mqtt_broker is not set (specify name/ip of server)'
mqtt_user=''
assert mqtt_user!='', 'Oh no! mqtt_user is not set (mqtt user name is requred)'
mqtt_password=''
assert mqtt_password!='', "Oh no! mqtt_password is not set(mqtt user's password is requred)"
mqtt_topic=b''
assert mqtt_topic!=b'', "Oh no! mqtt_topic is not set(mqtt Topic (listening chanel is requred))"

#Led is controlled by messages
def callback_routine(feed, msg):
    print('Received Data from: feed={}, msg={}'.format(feed, msg))
    if( msg==b'ON'):
        LED_GPIO_2.off()
    else:
        LED_GPIO_2.on()     

print('Trying to connect to mqtt broker.')
client = MQTTClient(mqtt_client_id, mqtt_broker, user=mqtt_user,
                    password=mqtt_password,port=8883, ssl=True )
#set client callback
client.set_callback(callback_routine)
#connect to mqtt_broker
client.connect()
print("Connected to {}".format(mqtt_broker))
t = mqtt_topic 
client.subscribe(t)
print("Subscribed to %s topic" % t)
try:
    while(True):
        client.wait_msg()

except :
    client.disconnect()

