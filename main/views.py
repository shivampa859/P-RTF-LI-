from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def skills(request):
    return render(request, 'skills.html')
def projects(request):
    return render(request, 'projects.html')
def experience(request):
    return render(request, 'experience.html')
def resume(request):
    return render(request, 'resume.html')
def contact(request):
    return render(request, 'contact.html') 

def contact(request):

    success = False

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
Name: {name}

Email: {email}

Message:
{message}
"""

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['shivampatel939957@gmail.com'],
            fail_silently=False,
        )

        success = True

    return render(request, 'contact.html', {'success': success})