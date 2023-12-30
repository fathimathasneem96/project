from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description =models.TextField(blank=True)
    image = models.ImageField(upload_to='Departments',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def get_url(self):
        return reverse('doctors_by_department', args=[ self.slug])

    def __str__(self):
        return '{}' .format(self.name)
class Doctors(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Doctors', blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return '{}' .format(self.name)

class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    age =models.IntegerField(unique=True)
    gender = models.CharField(max_length=6)
    house_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(unique=True)
    description = models.TextField( unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def get_url(self):
        return reverse('record', args=[ self.slug])

    def __str__(self):
        return '{}' .format(self.name)