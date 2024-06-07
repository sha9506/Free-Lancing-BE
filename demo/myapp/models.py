from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10)
    
class jobs(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=10)
    job_category = models.CharField(max_length=10)
    job_description = models.CharField(max_length=200)
    job_requirement = models.CharField(max_length=200)
    job_salary = models.IntegerField()
    job_icon = models.ImageField()
    job_provider_id = models.ForeignKey(user, on_delete=models.CASCADE)
    job_status = models.CharField(max_length=10)
    
class payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    job_id = models.ForeignKey(jobs, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20)
    amount = models.IntegerField()
    
    
