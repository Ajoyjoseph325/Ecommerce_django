from django.shortcuts import render

from email import message
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.template import RequestContext
def register(request):
    
    if request.method == 'POST':
        
        username=request.POST['uname']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("register")
            
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save();
                print("user created")
                return redirect('/')
            
            
        else:
            print("password not match")
            return redirect('register')
        
    else:
        return render(request,"register.html")

        
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['passwd']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            request.session['login'] = 'login'
            request.session['user'] = username
            return redirect('/')
        else:
            messages.info(request,"invalid credantials")
            return redirect('login')
    else:
        return render(request,"login.html")      
        
def logout(request):
    auth.logout(request)
    print("Loged out.......")
    return redirect('/')


    
