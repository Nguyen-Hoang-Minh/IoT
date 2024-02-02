import sys
from Adafruit_IO import MQTTClient
import time
import random

AIO_FEED_ID = ["button1", "button2"]
AIO_USERNAME = "minhnguyen2810"
AIO_KEY = "aio_OtRr52oAZyTiFTJu2pSJlgr6ekeR"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
while True:
    counter = counter-1
    if counter<=0:
        counter = 10
        print("")
        print("random data is publishing....")
        temp = random.randint(10,20)
        client.publish("demo", temp)
        humi = random.randint(19,70)
        client.publish("demo1", humi)
        light = random.randint(10, 50)
        client.publish("demo2", light)
    time.sleep(1)
    pass