from django.shortcuts import render


# Create your views here.
def register(request):
    if request.method == 'POST':
        UserName = request.POST['username']
        First_Name = request.POST['first_name']
        Last_Name = request.POST['last_name']
        Email = request.POST['email']
        Password = request.POST['password']
        ConfirmPassword = request.POST['password1']

    return render(request, "register.html")
