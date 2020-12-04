from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def iata(request):
    return render(request, 'iata.html')
def about(request):
    return render(request, 'about.html')
