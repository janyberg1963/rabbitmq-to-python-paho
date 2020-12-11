import paho.mqtt.client as mqtt

import time
class Mqmess:
    def __init__(self,Tname,Tvalue):
        self.Tname = Tname
        self.Tvalue = Tvalue

    def G_data(self):
        return f'{self.Tname},{self.Tvalue}'





theList=['topic']
values=[]
dmess=Mqmess('topic','tvalues')

def ReadMqtt():
          
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
        client.subscribe([("sensors/drone01/altitude",0),('sensors/drone01/Airspeed',0)])

       



       
        


        def on_message(client,userdata,msg):
           # print(msg.topic)
           # print(msg.payload)
            A_mess = msg.payload
            ATopic=msg.topic
            

            Payload(A_mess,ATopic)
                    

        def Payload(A_mess,ATopic):
            
            print('in the function')
            print(A_mess)
            print(ATopic)
                      
            global theValue
            global theTopic
            global values
            
            global Mqmess
           
            theTopic=ATopic
            theValue=A_mess
               
            b=Mqmess(theTopic,theValue)  
            c=(b.G_data())
            print(c)
            values.append(c)
            
            #print(theList)

           

        client.on_message=on_message
        
            

        time.sleep(1)

        client.loop_stop()
        client.disconnect()
        #print(messages)
        #print (theTopic)

       

              

       
        
       

        #print(theList)
        print(values)
        #print (theValue)
        return (values)