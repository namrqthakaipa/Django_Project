from django.shortcuts import render


# my_app/views.py
'''
from django.http import HttpResponse

def custom_message(request):
    return render(request, 'my_app/home.html')
'''

# my_app/views.py
from django.http import HttpResponse

def custom_message(request):
    return HttpResponse("This is my first Django project")

