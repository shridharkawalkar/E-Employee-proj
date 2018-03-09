# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

GENDER_CHOICES = (
    ('M', 'Male.'),
    ('F', 'Female'),
)
class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    dob = models.DateField()    
    joining_date = models.DateField()
    permanent_address = models.CharField(max_length=1023)
    designation = models.CharField(max_length=256)
    department = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. From 9 to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
    








