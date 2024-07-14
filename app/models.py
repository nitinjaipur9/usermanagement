from django.db import models

# Create your models here.
class appUser(models.Model):
    patient = 'patient'
    doctor = 'doctor'
    USER_TYPE = [
        (patient, 'Patient'),
        (doctor, 'Doctor')
    ]
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=28)
    address = models.CharField(max_length=500)
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    def __str__(self):
        return self.username
