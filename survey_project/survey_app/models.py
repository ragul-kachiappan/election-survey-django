from django.db import models
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
# Create your models here.
class ElectionSurveyDetails(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    PARTY_CHOICES = [('AAA', 'AAA'),
                     ('AAB', 'AAB'),
                     ('AAC', 'AAC'),
                     ('AAD', 'AAD'),
                    ]
    party_name = models.CharField(max_length=3, choices=PARTY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'dob', 'city', 'party_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
