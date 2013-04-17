from django.db import models
from django.forms import ModelForm



# Create your models here.
#class Salon (models.Model):
#    name = models.CharField(max_length = 200)
#    address = models.StringField()
#
#class Stylist (models.Model):
#    name = models.CharField(max_length = 200)
#    salon = models.ForeignKey(Salon)
#
#class Service (models.Model):
#    type = models.CharField(max_length = 200)
#    sylist = models.ForeignKey(Stylist)
#    salon = models.ForeignKey(Salon)

class Reviews(models.Model):
    stylist = models.CharField(max_length = 200)
    salon = models.CharField(max_length = 200)
    service = models.CharField(max_length = 200)
   
    # ratings, out of 5 stars
    salon_rating = models.IntegerField()
    service_rating = models.IntegerField()
    stylist_rating = models.IntegerField()
    atmosphere_rating = models.IntegerField()
    service_rating =models.IntegerField()
    wait_rating =models.IntegerField()
    personality_rating =models.IntegerField()
    talking_rating =models.IntegerField()
    expertise_rating =models.IntegerField()
    price_rating =models.IntegerField()
    quality_rating =models.IntegerField()

    # text based feedback
    salon_feedback = models.CharField(max_length = 2000)
    stylist_feedback = models.CharField(max_length = 2000)
    service_feedback = models.CharField(max_length = 2000)

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews

