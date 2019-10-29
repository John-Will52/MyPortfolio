from django.shortcuts import render, redirect
from .models import Message
# from django.core.mail import send_mail

def index(request):
    return render(request, "softDev/Home.html")