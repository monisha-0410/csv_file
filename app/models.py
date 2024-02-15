from django.db import models

# Create your models here.
class Bank(models.Model):
    Bank_name=models.CharField(max_length=100)

class Branch(models.Model):
    Bank_name=models.ForeignKey(Bank,on_delete=models.CASCADE)
    ifsc=models.CharField(max_length=100)
    Branch=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Contact=models.IntegerField()
    City=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    State=models.CharField(max_length=100)