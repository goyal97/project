from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50, default="")
    dob = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name
