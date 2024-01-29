from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        UserName = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(
            username=UserName,
            password=Password
        )
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        UserName = request.POST['username']
        First_Name = request.POST['first_name']
        Last_Name = request.POST['last_name']
        Email = request.POST['email']
        Password = request.POST['password']
        ConfirmPassword = request.POST['password1']
        if Password == ConfirmPassword:
            if User.objects.filter(username=UserName).exists():
                messages.info(request, "User Name Already Exist")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=UserName,
                    password=Password,
                    first_name=First_Name,
                    last_name=Last_Name,
                    email=Email
                )
                user.save()
                print("User Created")
                return redirect('login')
        else:
            messages.info(request, "Password Mismatch")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    # return render(request, "logout.html")
    return redirect('/')