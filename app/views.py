from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
import csv

def insert_Bank(self):
    with open('C:\\Users\\Monisha\\Desktop\\djangoProjects\\monisha\\Scripts\\project38\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(Bank_name=bn)
            BO.save()
    return HttpResponse('bank data is inserted successfully')

def insert_Branch(self):
    with open('C:\\Users\\Monisha\\Desktop\\djangoProjects\\monisha\\Scripts\\project38\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(Bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                d=i[6]
                s=i[7]
            BRO=Branch(Bank_name=BO[0],ifsc=ifs,Branch=br,Address=ad,Contact=co,City=ci,District=d,State=s)
            BRO.save()
    return HttpResponse('Branch data is inserted successfully')


