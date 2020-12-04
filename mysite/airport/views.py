from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')
def iata(request):
    if request.method == 'post':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        '''fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'iata.html')'''
def about(request):
    return render(request, 'about.html')

