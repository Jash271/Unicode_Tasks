from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
# Create your views here.
def home(request):
    
    
    response=requests.get('https://api.spacexdata.com/v3/launches')
    launch=response.json()
        
   
        
        
        

    return render (request,"home.html",{'launch':launch})
      


    