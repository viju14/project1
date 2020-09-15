from django.db import models

# Create your models here.

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    #address=models.CharField(max_length=50)
    salary=models.FloatField()
    age=models.IntegerField()


    class Meta:
        db_table='Employee1'
#
class Address(models.Model):
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    cuntry=models.CharField(max_length=20)
    pincode=models.IntegerField()
    emp=models.ManyToManyField(Employee,unique=False,related_name='adr',null=True)
    class Meta:
        db_table='Address1'

        #Address(city='pune'



