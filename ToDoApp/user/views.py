from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Register view
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    else:
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        hashed_password = make_password(user_password)

        user = User.objects.create(
            name=user_name,
            email=user_email,
            password=hashed_password
        )
        return redirect('/user/login/')

# Login view
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

    else:
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        try:
            user = User.objects.get(email=user_email)
            if check_password(user_password, user.password):
                request.session['useremail'] = user.email
                request.session['username'] = user.name
                return redirect('/task/crud/')
            else:
                return HttpResponse("Invalid password")

        except User.DoesNotExist:
            return HttpResponse("User does not exist")
