from django.db import models
from datetime import datetime

# Create your models here.
class Contacts(models.Model):
    message=models.TextField(blank=True)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    listing_id=models.IntegerField()
    contact_date=models.DateTimeField(default=datetime.now())
    name=models.CharField(max_length=200)
    user_id=models.IntegerField()
    listing_name=models.CharField(blank=True,max_length=200)
    def __str__(self):
        return self.name
