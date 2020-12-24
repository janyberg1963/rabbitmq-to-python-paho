from django.shortcuts import render
from django.contrib.auth.models import User
from . mqtt import ReadMqtt
from .mqread import Mq_temp


# Create your views here.

def index(request):
    
    
    
    #values=[]
     
    
    #mq_mess=ReadMqtt()
    values=ReadMqtt()
    print ('return from function')
    #print (mq_topic)
    #print (mq_mess) 
    #mq_mess2 = mq_mess[0]
    #mq_mess1 = mq_mess[1] 
    print (values)
    stuff_for_frontend = {'mq_values':values}
    return render(request,'Mess/index.html',stuff_for_frontend)


def Temp(request):
    v_topic ="Rasp_temp"
    v_Broker = "192.168.1.70"
    view_temp=Mq_temp()
    print ('return from function')
    print (view_temp)
    stuff_for_frontend = {'view_temp': view_temp}
   




    return render(request,'Mess/mq_temp.html',stuff_for_frontend)

