from django.shortcuts import render,redirect
from doctor_profile_app.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import os

# Create your views here.

def home_page(request):
    doctors = DoctorProfile.objects.all()
    
    
    return render(request,'home.html',{'doctors':doctors})


def profile_page(request,id = None):
    
    if id:
        doctor_info = DoctorProfile.objects.get(pk = id)
    return render(request,'profile.html',{'doctor_info':doctor_info})


def edit_profile(request,id):
    doctor = DoctorProfile.objects.get(pk=id)
    
    if request.method == 'POST':
        doctor.phone = request.POST.get('phone')
        doctor.experience = request.POST.get('experience')
        doctor.clinic_address = request.POST.get('clinic_address')
        doctor.specialization = request.POST.get('specialization')
        new_image = request.FILES.get('image')

        if new_image:
            if doctor.image:
                doctor.image.delete(save=False)  # delete old file
            doctor.image = new_image

        doctor.save()
        return redirect('profile_page',id=id)
    return render(request,'edit_profile.html',{'doctor': doctor})

@login_required
def patient_reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        PatientRegister.objects.create(
            name = name,
            age = age,
            email = email,
            user = request.user
        )

        return redirect ('patient',)
    
    return render(request, 'patient_reg.html')

@login_required
def patient_list(request):
    user = request.user
    patients = PatientRegister.objects.filter(user = request.user)
    print(patients)    
    return render(request,'patient.html',{'patients':patients})

def about_us(request):
    return render(request,"about.html")

def sign_up_page(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        
        
        if User.objects.filter(username=uname).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(
            username=uname,
            password=password,
            first_name=fname,
            last_name=lname
        )
        user.save()

        DoctorProfile.objects.create(
            user=user,
            specialization=request.POST.get('specialization'),
            experience=request.POST.get('experience'),
            clinic_address=request.POST.get('clinic_address'),
            phone=request.POST.get('phone'),
            image = request.FILES.get('image')
        )
        return redirect('login')
    return render(request,"signup.html")

def login_page(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST['password']

        user = authenticate(request, username=uname, password=password)

        if user is not None:
            login(request, user)
            return redirect('patient')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')



def delete(request,id):
    patient = PatientRegister.objects.get(pk = id)
    if patient:
        patient.delete()   
        return redirect('patient')
    

    
def edit(request,id):
    patient = PatientRegister.objects.get(pk=id)
    
    if request.method == "POST":
        patient.name = request.POST.get('name')
        patient.email = request.POST.get('email')
        patient.age = request.POST.get('age')

        patient.save()
        return redirect('patient')
    return render(request,'patient_reg.html',{'patient':patient})