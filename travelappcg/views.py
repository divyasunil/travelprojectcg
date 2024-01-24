from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import Team


# Create your views here.
def demo(request):
    # name = "India"
    # return render(request, "home.html", {'obj': name})
    # return HttpResponse("Hello World") #httpview
    # return render(request,"index.html")  # render
    obj = Place.objects.all()
    teamobj = Team.objects.all()
    return render(request, 'index.html', {'result': obj, 'team': teamobj})

# def addition(request):
#     number1 = int(request.GET['num1'])
#     number2 = int(request.GET['num2'])
#     res = number1 + number2
#     return render(request, "result.html", {'result': res})  # render

# def about(request):
#     return render(request,"about.html")  # render
#
# def contact(request):
#     return HttpResponse("Hello Contact Page")
