from django.template import Context, loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from tips.models import Reviews

# Create your views here.
def reviews(request):
	return render(request, 'tips/reviews.html', ({}))

def process(request):
	selected_choice = p.choice

# type is from the set (salon, service, )
#def show (request, salon_name, type):
