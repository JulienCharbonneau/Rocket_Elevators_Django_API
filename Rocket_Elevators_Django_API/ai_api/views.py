from django.http import HttpResponse, JsonResponse
import face_recognition
import json
from .models import Employee
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer
import numpy

@api_view(['PUT'])
def save_facial_keypoints(request):
    image = face_recognition.load_image_file(request.FILES['image'])
    keypoints = face_recognition.face_encodings(image)[0]
    print("intial keypoint _-____--_-", keypoints)

    # Get the employee from the database
    employee_id = request.data['employee_id']
    employee = Employee.objects.get(id=employee_id)
    # save data
    employee.facial_keypoints = json.dumps(numpy.array(keypoints).tolist())
    employee.save()

    return HttpResponse("Keypoints Saved!")

@api_view(['GET'])
def retreive_keypoints(request):
    image = face_recognition.load_image_file(request.FILES['image'])
    request_keypoints = face_recognition.face_encodings(image)[0]
    print("request keypoint======",request_keypoints )

    for employee in Employee.objects.all():
        if employee.facial_keypoints is None:
            continue
        employee_keypoints = json.loads(employee.facial_keypoints)
        print("employee keypoint======",employee_keypoints )
        if compare_keypoints(employee_keypoints, request_keypoints):
            employee_serializer = EmployeeSerializer(employee)
            return JsonResponse(employee_serializer.data)
        else :
            return HttpResponse("Keypoints do not match for any employee.")

def compare_keypoints(employee_keypoints, request_keypoints):
    employee_keypoints = numpy.array(employee_keypoints)
    results = face_recognition.compare_faces([employee_keypoints], request_keypoints)
    return results[0]
