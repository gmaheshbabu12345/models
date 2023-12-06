from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
class Emp(models.Model):
    deptno=models.ForeignKey(Dept('deptno'),on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
