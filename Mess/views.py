from django.shortcuts import render
from django.contrib.auth.models import User
from . mqtt import ReadMqtt


# Create your views here.

def index(request):
    
    mq_mess= ''
    mq_topic=''
    
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
