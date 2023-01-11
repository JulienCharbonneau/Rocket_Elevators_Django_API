from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
    facial_keypoints = models.JSONField()


    class Meta:
        db_table = 'employees'
        managed = False