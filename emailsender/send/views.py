from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request): 
    send_mail('Hello this is a subject',
    'Hello this is the automated message etc ..... ',
    'steven.zaki@booking.com',
    ['stevensivo27@gmail.com'] ,fail_silently=False)
    return render(request, 'send/index.html' )