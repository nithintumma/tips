from django.db import models

# Create your models here.
class Salon (models.Model):
    name = models.CharField(max_length = 200)
    address = models.StringField()

class Stylist (models.Model):
    name = models.CharField(max_length = 200)
    salon = models.ForeignKey(Salon)

class Service (models.Model):
    type = models.CharField(max_length = 200)
    sylist = models.ForeignKey(Stylist)
    salon = models.ForeignKey(Salon)

class Reviews(models.Model):
    stylist = models.CharField(max_length = 200)
    salon = models.CharField(max_length = 200)
    service = models.CharField(max_lengt)
    
