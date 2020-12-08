from django.shortcuts import render
from django.contrib.auth.models import User
from . mqtt import ReadMqtt

# Create your views here.

def index(request):
    mq_mess= ''
    mq_mess=ReadMqtt()
    
    print ('return from function')
    print (mq_mess) 
    stuff_for_frontend = {'mq_mess': mq_mess}
    return render(request,'Mess/index.html',stuff_for_frontend)
