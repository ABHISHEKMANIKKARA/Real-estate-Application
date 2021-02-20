from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from contact.models import Contacts

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is None:
            return render(request, 'login.html', {"error": "Incorrect username or password"})
        else:
            auth.login(request, user)
            return redirect('index')
    else:
     return render(request,'login.html')
def Logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')
def register(request):
 if request.method=='POST':
    user=authenticate(username=request.POST.get('username'))
    if user is None:
        if(request.POST.get('password')==request.POST.get('password2')):
            user1=User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'),email=request.POST.get('email'),
                                           first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'))
            user1.save()
            auth.login(request,user1)
            return redirect('index')
        else:
            return render(request, 'register.html', {"error": "Password and confirm password do not match"})
    else:
        return render(request,'register.html',{"error":"username already taken"})

 else:
     return render(request,'register.html')
def dashboard(request):
    id=request.user.id
    ob=Contacts.objects.filter(user_id=id)
    context={"ob":ob}
    return render(request,'dashboard.html',context)
