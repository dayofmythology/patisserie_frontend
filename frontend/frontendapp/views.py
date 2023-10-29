from django.shortcuts import render
import requests
from django.http import HttpResponse
import os

def index(request):
    
    hostname = os.environ.get('API_HOSTNAME')
    port = os.environ.get('API_PORT')
    if hostname !=None and port!=None:        
        HOST= f"http://{hostname}:{port}/api/get_response"
        print (f"The URL is {HOST}")
        # Make a GET request to the backend API
        response = requests.get(f'{HOST}')
        try:
            if response.status_code == 200:
                data = response.json()
                message = f"<b>{data.get('message')}</b>"
            else:
                message = '<b>Error: Unable to get message from backend</b>'
        except requests.exceptions.RequestException as e:
            message = f"Exception: {str(e)}"
    else:
        message = '<b>API URL is invalid</b>'
            
    return HttpResponse(f'Response from Backend: {message}')
