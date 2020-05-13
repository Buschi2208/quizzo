from django.shortcuts import render

def home(request):
    return render(request,'quizzos/home.html')

def overview(request):
    return render(request,'quizzos/overview.html')