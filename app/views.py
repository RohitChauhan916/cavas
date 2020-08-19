from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.base import ContentFile
from .forms import canvasForm
from .models import Canvas
import base64
# Create your views here.
from django.core.files.base import ContentFile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created : {username}")
            login(request, user)
            messages.info(request, f"You are Now logged in : {username}")
            return redirect("/home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def logout_req(request):
    logout(request)
    messages.info(request, "Logout successful")
    return redirect("/")

def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in : {username}")
                return redirect("/home")
            else:
                messages.error(request, "Invalid username and password")
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})

def updesign(request):
    form = canvasForm()
    if request.method == 'POST':
        form = canvasForm(request.POST, request.FILES)
        if form.is_valid():
            image_b64 = request.POST.get('design_image')
            format, imgstr = image_b64.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            customer = request.POST['customer']
            if request.user.is_authenticated:
                customer = request.user
                form, created = Canvas.objects.get_or_create(customer=str(customer), design_image=data)
            form.save()        
    else:
        form = canvasForm()
    context = {'form':form}
    return render(request, 'homepage.html', context)