from django.shortcuts import render,redirect
from .models import Project,Skills,Message
from .forms import ProjectForm, MessageForm
from django.contrib import messages
# Create your views here.
def home(request):
    project = Project.objects.all()
    skills = Skills.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if(form.is_valid):
            form.save()
            messages.success(request, 'Your message was successfully sent.')
    context = {'projects':project, 'skills':skills,'form':form}
    return render(request, 'base/home.html',context)

def project(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project':project}
    return render(request, 'base/project.html', context)

def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,'base/projects_form.html',context)

def editProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,'base/projects_form.html',context)

def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    context={'inbox':inbox, 'unreadCount':unreadCount}
    return render(request, 'base/inbox.html',context)

def messagePage(request,pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context={'message': message }
    return render(request, 'base/message.html',context)