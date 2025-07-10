# Create your models here.
from django.db import models

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class EmergencyType(models.Model):  # Renamed from 'type' to 'EmergencyType'
    emergency_category = models.CharField(max_length=100)
    emergency_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emergency_category} {self.emergency_type}"

class Case(models.Model):
    STATUS_CHOICES = [
        ('Reported', 'Reported'),
        ('Resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=10)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Reported')
    latitude = models.FloatField()
    longitude = models.FloatField()
    picture = models.ImageField(upload_to='case_pictures/')
    reported_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(auto_now=True)
    reported_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='reported_cases')

    def __str__(self):
        return self.title