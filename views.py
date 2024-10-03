# views.py
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def send_email(request):
    send_mail(
        'Welcome Party - reg.',  # Subject
        'Greetings!!! Welcome to the Department of Information Technology.',  # Email content
        settings.EMAIL_HOST_USER,  # From email
        ['dhiya262005@gmail.com'],  # To email(s)
        fail_silently=False,
    )
    return render(request, 'send_email.html')  # Render success message
