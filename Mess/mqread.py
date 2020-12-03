import paho.mqtt.client as mqtt

import time
        
broker='127.0.0.1'
client=mqtt.Client("my_mqtt")

def on_connect(client, userdata,flags,rc):
    if rc==0:
        client.connected_flag=True
        print("connected")
    else:
        print("bad connection returned code",rc)

mqtt.Client.connected_flag=False

client.on_connect=on_connect

client.loop_start()
print("connecting to server",broker)
client.connect(broker)
while not client.connected_flag:
    print("in wait loop")
    time.sleep(1)
print("in main loop")

client.loop_stop()
client.disconnect()

