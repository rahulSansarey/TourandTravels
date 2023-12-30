from django.db import models

# Create your models here.


class GeeksModel(models.Model):
    title=models.CharField(max_length=20)
    arrival=models.CharField(max_length=30)
    description=models.TextField()
    def __str__(self):
        return self.title
class ContactsModel(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    message=models.TextField()
    def __str__(self):
        return self.name
class LoginModel(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class PaymentsModel1(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    address=models.TextField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=10)
    nameoncard=models.CharField(max_length=20)
    cardnumber=models.CharField(max_length=16)
    expmonth=models.CharField(max_length=20)
    expyear=models.CharField(max_length=4)
    cvv=models.CharField(max_length=3)
    def __str__(self):
        return self.fullname    

