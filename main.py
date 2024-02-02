import sys
from Adafruit_IO import MQTTClient
import time
import random

AIO_FEED_ID = ["button1", "button2"]
AIO_USERNAME = "minhnguyen2810"
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload, "feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
sensor_type = 0
while True:
    counter = counter-1
    if counter<=0:
        counter = 10
        if(sensor_type==0):
            print("temperature data is publishing....")
            temp = random.randint(10,20)
            client.publish("demo", temp)
            sensor_type = 1
        elif(sensor_type==1): 
            print("humidity data is publishing....")
            humi = random.randint(19,70)
            client.publish("demo1", humi)
            sensor_type = 2
        elif(sensor_type==2): 
            print("light data is publishing....")
            light = random.randint(10, 50)
            client.publish("demo2", light)
            sensor_type = 0
    time.sleep(1)
    pass