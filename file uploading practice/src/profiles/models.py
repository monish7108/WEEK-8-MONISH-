from django.db import models

class profile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name=models.CharField(max_length=20)
    disp_pic=models.FileField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name

class myprofile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name=models.CharField(max_length=20)
    disp_pic=models.FileField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name