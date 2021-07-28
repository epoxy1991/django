from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name #show the actual city name on the dashbaord

    class Meta: #show the plural of the city as cities instead of citys
        verbose_name_plural = 'cities'


# Create your models here.
