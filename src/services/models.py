from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=30)
    details = models.TextField()
    icon = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title