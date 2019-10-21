from django.shortcuts import render, redirect
from .models import Message
# from django.core.mail import send_mail

def index(request):
    return render(request, "softDev/Home.html")

def about(request):
    return render(request, "softDev/AboutMe.html")

def resume(request):
    return render(request, "softDev/Resume.html")

def workshop(request):
    return render(request, "softDev/Workshop.html")

# def contact(request):
#     if request.method == 'GET':
#         return render(request, "softDev/Contact.html")

#     if request.method == 'POST':
#         Message.objects.create(name = request.POST['Name'], email = request.POST['Email'], message = request.POST['Message'])
#         return redirect("/contact")
        
# def masterEntry(request):
#     context = {
#         "allMessages": Message.objects.all()
#     }
#     return render(request, "softDev/BackDoor.html", context)
        
#         send_mail('{name}',
#          '{message}',
#          '{email}',
#          ['johnwill52is@gmail.com'],
#          fail_silently=False)
#          return redirect("/contact")