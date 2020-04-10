from django.db import models

# Create your models here.


class Agents(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name= 'Agent'
        verbose_name_plural = 'Agents'
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agents/', null=True)
    def __str__(self):
        return self.name

