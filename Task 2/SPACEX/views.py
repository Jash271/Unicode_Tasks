from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
# Create your views here.
def home(request):
    dictionary=[]
    
    response=requests.get('https://api.spacexdata.com/v3/launches')
    launch=response.json()
    for launch in launch:
     date=launch['launch_date_utc'][0:10]
     time=launch['launch_date_utc'][11:22]
     date_time=date+' '+time
     date_time_obj=datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S.%f')
     launch['launch_date_utc']=datetime.strftime(date_time_obj,'%Y-%m-%d %H:%M:%S.%f')
     
     dictionary.append(launch)
   
        
        
        

    return HttpResponse(dictionary)
      


    