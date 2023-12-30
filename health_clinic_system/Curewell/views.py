from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
#workon finalenv
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from Curewell.models import Doctors, Department, Patient


def alldoctors(request, slug_c=None):
    page_c = None
    doctors = None
    if slug_c != None:
        page_c = get_object_or_404(Department, slug=slug_c)
        doctors = Doctors.objects.all().filter(department=page_c)

    else:
        doctors= Doctors.objects.all().filter(available=True)

    return render(request, 'home.html', {'department': page_c, 'doctors': doctors})


def aboutus(request):
    return render(request,'aboutus.html')

def booking(request,slug_c=None):
    departments = None
    departments = Department.objects.all().filter
    page_c=None
    doctors=None
    if slug_c != None:
        page_c = get_object_or_404(Department, slug=slug_c)
        doctors = Doctors.objects.all().filter(department=page_c)

    else:
        doctors= Doctors.objects.all().filter(available=True)
    return render(request,'booking.html',{'departments':departments, 'doctors':doctors})
def contactus(request):
    return render(request,'contactus.html')
def ourdoctors(request):
    doctors = None
    doctors = Doctors.objects.all().filter
    return render(request, 'ourdoctors.html', {'doctors':doctors})

def patient(request):
    return render(request, 'patient.html')

def record(request):
    return render(request,'record.html')

def patient_record(request):
    patient = None
    patient = Patient.objects.all().filter(id=patient.id)
    return render(request,'patient_record.html',{'patient':patient})
@csrf_protect
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        hname=request.POST['hname']
        po=request.POST['po']
        age=request.POST['age']
        phonenumber=request.POST['phonenumber']
        password1=request.POST['password1']
        password2=request.POST['password2']

        myuser=User.objects.create_user(username,password1)
        myuser.firstname= fname
        myuser.lastname= lname

        myuser.save()
        return redirect('signin')
    return render(request,'register.html')

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']

        user=authenticate(username=username, password=password1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, 'record.html', {'fname': fname})
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('alldoctors')
    else:
        error_message=None

    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('alldoctors')