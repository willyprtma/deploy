from django.shortcuts import render, redirect
from .models import About, Project, Contact
from .forms import FormContact

def index(request):
    about, created = About.objects.get_or_create(id=1, defaults={'nama': 'Willy Erfan P', 'pekerjaan': 'Pelajar', 'foto': 'ngetest.jpg', 'tentang': 'Jawa'})
    projects = Project.objects.all()
    
    context = {
    'about': about,
    'projects': projects,
    'form': FormContact()
    }
    return render (request, "index.html", context)

def send_contact(request):
    if request.POST:
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/#contact')
        return redirect('/#contact')

