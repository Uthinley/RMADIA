from django.db import models

# Create your models here.

class report(models.Model):
    Employee_Id = models.IntegerField()
    Employee_email = models.CharField(max_length= 50)

    S_name = models.CharField(max_length=30)
    s_job_pos = models.CharField(max_length=30)
    s_phone = models.IntegerField()
    s_address = models.CharField(max_length=100)

    what_wrong = models.TextField()
    who_wrong = models.TextField()
    where_wrong = models.TextField()
    enabled_wrong = models.TextField()
    solution = models.TextField()

    incident_date = models.DateField()

    documents = models.FileField(default="")

    status = models.CharField(max_length=10, default="S")


