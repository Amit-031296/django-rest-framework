from django.db import models

class employees(models.Model):
    firstname=models.CharField(max_length=800)
    lastname=models.CharField(max_length=800)
    emp_id=models.IntegerField()
    
    def __str__(self):
        return self.firstname
