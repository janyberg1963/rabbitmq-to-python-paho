from django.shortcuts import render
from django.contrib.auth.models import User
from . mqtt import ReadMqtt

# Create your views here.

def index(request):
    mq_mess= ''
    mq_mess=ReadMqtt()
    
    print ('return from function')
    print (mq_mess) 
    mq_mess2 = mq_mess.decode('utf-8')
      
    stuff_for_frontend = {'mq_mess2': mq_mess2}
    
    return render(request,'Mess/index.html',stuff_for_frontend)
