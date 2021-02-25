from django.db import models
from django.urls import reverse

# Create your models here.
GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]


class Symptom(models.Model):
    pregnancy_count = models.IntegerField(blank=False)
    plasma = models.IntegerField(blank=False)
    skin_thickness = models.IntegerField(blank=False)
    blood_pressure = models.IntegerField(blank=False)
    insulin = models.IntegerField(blank=False)
    bmi = models.FloatField(blank=False)
    pedigree = models.FloatField(blank=False)
    age = models.IntegerField(blank=False)
    prediction_result = models.BooleanField(default=False, blank=True)
    type_one_result = models.BooleanField(default=False, blank=True)
    type_two_result = models.BooleanField(default=False, blank=True)
    gestational_result = models.BooleanField(default=False, blank=True)

    def __int__(self):
        return Symptom.age


class Patient(models.Model):
    first_name = models.CharField(max_length=10, blank=False)
    middle_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    dob = models.DateField(blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, blank=False)
    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE, blank=True)

    def get_absolute_url(self):
        return reverse('patient-edit', kwargs={'pk': self.pk})



