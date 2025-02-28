from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
# Create your views here.

# Create your views here.
""" from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my blog!") """

def register(request):
    
    if request.method == 'GET':
        print("Do nothing")
        # data={'welcome':"Welcome Samir!Register your data"}
        return render(request,'user/register.html')
         # return HttpResponse("Get method called")
    
    else:
        print(request.POST)
        print("Do Register")
        # data={'welcome':"Welcome Samir! Login your data"}
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_password=request.POST.get('password')
        user=User.objects.create(name=user_name,email=user_email,password=user_password)
        return redirect('/user/login/')
    
def login(request):
    if request.method == 'GET':
        # data={'welcome':"Welcome Samir! Login your data"}
        return render(request,'user/login.html')
    
    else:
        print(request.POST)
        user_email=request.POST.get('email')
        user_password=request.POST.get('password')
        try:
            user=User.objects.get(email= user_email,password=user_password)
            request.session['useremail']=user_email
            request.session['username']=user.name
            return redirect('/task/crud/')
        
        except:
            print("not available")
            return HttpResponse("Login Failed")
    
        return HttpResponse("Login Successful")
    
        # return render(request,'user/login.html',data)
        #return HttpResponse("Post method called")
        