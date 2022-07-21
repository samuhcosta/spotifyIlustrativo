from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def premium(request):
    return render(request, 'premium.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def baixar(request):
    return render(request, 'baixar.html')
