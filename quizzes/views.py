from django.shortcuts import render

def home(request):
    return render(request,'quizzes/home.html')

def overview(request):
    return render(request,'quizzes/overview.html')