from django.shortcuts import render
from .api_config import API_URL
import requests
from django.http import HttpResponse

def index(request):
    
    # Make a GET request to the backend API
    response = requests.get(f'{API_URL}')
    
    try:
        if response.status_code == 200:
            data = response.json()
            message = data.get('message')
        else:
            message = 'Error: Unable to get message from backend'
    except requests.exceptions.RequestException as e:
        message = f"Exception: {str(e)}"
            
    return HttpResponse(f'Response from Backend: {message}')
