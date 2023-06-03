from django.db import models

# Create your models here.

class studeninfo(models.Model):
    stu_id          = models.IntegerField(unique=True)
    stu_name        = models.CharField(max_length=100)
    stu_dob         = models.DateField(max_length=15)
    stu_address     = models.CharField(max_length=200)
    stu_phone       = models.CharField(max_length=20)
    stu_em_phone    = models.CharField(max_length=20)
    stu_class       = models.CharField(max_length=20)