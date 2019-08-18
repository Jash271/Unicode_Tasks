from django.db import models
from datetime import datetime

# Create your models here.
class Launches(models.Model):
    Mission_name=models.TextField(null=True)
    Flight_Number=models.IntegerField()
    Flight_date=models.DateTimeField()
    Rocket_Name=models.TextField()
    Rocket_Id=models.TextField()
    Mission_Patch_Link=models.URLField(null=True)
    Mission_Video_Link=models.URLField(null=True)

    def __int__(self):
        return Launches.Flight_Number

    
