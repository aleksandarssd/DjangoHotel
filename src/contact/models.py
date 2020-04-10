from django.db import models

# Create your models here.


class ContactDetails(models.Model):
    location = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.email
