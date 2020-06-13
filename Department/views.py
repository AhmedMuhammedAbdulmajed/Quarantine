from django.shortcuts import render
from .models import Department
# Create your views here.
def Deparment_List(requset):
    Deparment_List = Department.objects.all()
    template = 'Department/Department.html'
    context={
        'Deparment_List' : Deparment_List
    }
    return render(requset,template,context)

def Deparment_detial(requset,id):
    Deparment_detial = Department.objects.get(id=id)
    template = 'Department/Deparmentdetial.html'
    context={
        'Deparment_detial' : Deparment_detial
    }
    return render(requset,template,context)