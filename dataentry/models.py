from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField()

    def __str__(self):
        return self.email
    
class Customer(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField()

    def __str__(self):
        return self.email