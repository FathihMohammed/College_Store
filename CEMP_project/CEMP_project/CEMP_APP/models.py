from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "c_store_app_department"
class course(models.Model):
    c_name=models.CharField(max_length=100)
    d_name=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.c_name
    class Meta:
        db_table = "c_store_app_course"
class detailsclass(models.Model):
    s_name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    phno=models.DecimalField(max_digits=12,decimal_places=2)
    email=models.EmailField()
    address=models.TextField()
    def __str__(self):
        return self.s_name