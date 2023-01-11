from django.shortcuts import render
from django.http import HttpResponse
import face_recognition
import json
from .models import Employee
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer

@api_view(['PUT'])
def save_facial_keypoints(request):
    image = face_recognition.load_image_file(request.data['image'])
    keypoints = face_recognition.face_landmarks(image)
    # Get the employee from the database
    employee_id = request.data['employee_id']
    employee = Employee.objects.get(id=employee_id)
    employee.facial_keypoints = json.dumps(keypoints)
    employee.save()

    return HttpResponse("Keypoints Saved!")
