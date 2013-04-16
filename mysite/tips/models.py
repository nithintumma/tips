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
    service = models.CharField(max_length = 200)
   
    # ratings, out of 5 stars
    salon_rating = model.IntegerField()
    service_rating = model.IntegerField()
    stylist_rating = model.IntegerField()
    atmosphere_rating = model.IntegerField()
    service_rating =model.IntegerField()
    wait_rating =model.IntegerField()
    personality_rating =model.IntegerField()
    talking_rating =model.IntegerField()
    expertise_rating =model.IntegerField()
    price_rating =model.IntegerField()
    quality_rating =model.IntegerField()

    # text based feedback
    salon_feedback = model.TextField()
    stylist_feedback = model.TextField()
    service_feedback = model.TextField()

