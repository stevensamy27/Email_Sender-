from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request): 
    #send_mail('','','')
    return render(request, 'send/index.html' )