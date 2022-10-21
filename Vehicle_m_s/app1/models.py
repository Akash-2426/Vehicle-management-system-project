from django.db import models

# Create your models here.
class vehicle_type(models.Model):
    two_wheeler=models.CharField(max_length=100)
    three_wheeler=models.CharField(max_length=100)
    four_wheeler=models.CharField(max_length=100)

    def __str__(self):
        return self.two_wheeler

    def __str__(self):
        return self.four_wheeler
    def __str__(self):
        return self.three_wheeler

class vehicle(models.Model):
    vehicle_no=models.CharField(max_length=100,null=False)
    vehicle_type=models.CharField(max_length=100,null=False)
    vehicle_model=models.CharField(max_length=100)
    vehicle_description=models.CharField(max_length=100)

    def __str__(self):
        return  "%s %s %s %s" %(self.vehicle_no,self.vehicle_type,self.vehicle_model,self.vehicle_description)
