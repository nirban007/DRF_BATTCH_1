from django.db import models

class user_register(models.Model):
    # GENDER_CHOICES = [
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('C', 'Custom'),
    # ]
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    sirName = models.CharField(max_length=100)
    mobileNo = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=50)
    con_password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
