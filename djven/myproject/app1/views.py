from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import BookingContacts 

# Create your views here.
# def index(request):
#     return HttpResponse("<b>hello, world</b>")

# def index(request):
#     person={
#         'name': 'Jasim',
#         'age':'21',
#         'place': 'calicut'
#     }
#     return render(request,'index.html',person)

# def index(request):
#     person={
#         'num1':5
#     }
#     return render(request,'index.html',person)
# def index(request):
#     person={
#         'num1':[0,4,5,8,7]
#     }
#     return render(request,'index.html',person)

def index (request):
    return render(request,'index.html')
def teachers (request):
    teachers_details={
        "teachers":Teachers.objects.all(),
    }
    return render(request,'teachers.html',teachers_details)
def courses (request):
    course_details={
        "detail":Details.objects.all() 
    }
    return render(request,'courses.html',course_details)
def about (request):
    return render(request,'about.html')
def contacts (request):
    if request.method=='POST':
        form = BookingContacts(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'submit-contact.html')
    form = BookingContacts
    forms={
        'form':form
        }
    return render(request,'contacts.html',forms)
def base (request):
    return render(request,'base.html')
