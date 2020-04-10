from django.db import models

# Create your models here.

property_type = (
    ('sale', "sale"),
    ('rent', "rent")
)

class Property(models.Model):
    class Meta:
        verbose_name= 'Property'
        verbose_name_plural = 'Properties'

    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    location = models.CharField(max_length=100)
    property_type = models.CharField(choices=property_type, max_length=20)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2, max_digits=5)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', null=True)
    

    def __str__(self):
        return self.category_name   

    class Meta:
        verbose_name= 'Category'
        verbose_name_plural = 'Categories'





class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    Notes = models.TextField()
    def __str__(self):
        return self.name 


