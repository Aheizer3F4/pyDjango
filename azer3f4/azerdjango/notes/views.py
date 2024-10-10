from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def note_list(request):
    return render(request, 'note_list.html')

def about(request):
    return render(request, 'about.html')
