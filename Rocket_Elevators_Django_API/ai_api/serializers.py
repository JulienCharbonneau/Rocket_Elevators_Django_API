from rest_framework import serializers
from .models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id","last_name","first_name","title","email","created_at","updated_at","user_id","facial_keypoints","facial_keypoints"]