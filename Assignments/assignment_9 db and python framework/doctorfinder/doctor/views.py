from django.shortcuts import render, redirect
from doctor.models import Doctor
from django.http import JsonResponse
import json

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

from django.http import JsonResponse
import json
from .models import Doctor

def add_doctor(request):
    if request.method == 'POST':
        print("REQUEST RECEIVED")

        data = json.loads(request.body)
        print("DATA:", data)

        Doctor.objects.create(
            name=data['name'],
            specialization=data['specialization'],
            location=data['location']
        )

        return JsonResponse({'status': 'success'})

def delete_doctor(request, id):
    Doctor.objects.get(id=id).delete()
    return redirect('/')