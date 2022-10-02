from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    email=models.CharField(max_length=255)
    content=models.CharField(max_length=255)
