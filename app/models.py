from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_name=models.CharField(max_length=100,primary_key=True)
    dept_no=models.IntegerField()

    def __str__(self):
        return self.dept_name

class Emp(models.Model)  :
    emp_no=models.IntegerField()
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    emp_name=models.CharField(max_length=100,primary_key=True)  

