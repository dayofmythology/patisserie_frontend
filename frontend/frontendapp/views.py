from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse

def index(request):
    # Make a GET request to the backend API
    response = requests.get('http://127.0.0.1:8001/api/get_response/')
    
    if response.status_code == 200:
        data = response.json()
        message = data.get('message')
    else:
        message = 'Error: Unable to get message from backend'
    
    return HttpResponse(f'Value from Backend: {message}')
