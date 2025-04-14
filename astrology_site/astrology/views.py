from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sign(request):
    return render(request, 'sign.html')

def house(request):
    return render(request, 'house.html')

def planet(request):
    return render(request, 'planet.html')

def chart(request):
    return render(request, 'chart.html')