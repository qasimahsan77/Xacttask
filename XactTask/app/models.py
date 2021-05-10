"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Variable(models.Model):
    name=models.CharField(max_length=300,blank=True,null=True)
    type=models.CharField(max_length=300,blank=True,null=True)
    value=models.CharField(max_length=300,blank=True,null=True)


class BooleanValue(models.Model):
    Value=models.BooleanField(default=True)
    variable=models.ForeignKey(Variable,on_delete=models.CASCADE)

class StringValue(models.Model):
    Value=models.CharField(max_length=300,blank=True,null=True)
    variable=models.ForeignKey(Variable,on_delete=models.CASCADE)
