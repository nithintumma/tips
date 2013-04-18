from django.template import Context, loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from tips.models import Reviews
from tips.models import ReviewForm
from django.http import HttpResponseRedirect


# Create your views here.
def reviews(request):
	return render(request, 'tips/reviews.html', ({}))

def process(request):
	selected_choice = p.choice

def submit (request):
	if request.method == 'POST': # If the form has been submitted...
		form = ReviewForm(request.POST) # A form bound to the POST data
        form.save() 
        return HttpResponseRedirect('/')  

def search(request):
	if 'q' in request.GET and request.GET['q']: # If the form has been submitted...
		q = request.GET['q']
		results = Reviews.objects.filter(salon__icontains=q)
		labels = {  'atmosphere_rating': ['unpleasant', 'pleasant'],
					'wait_rating': ['Very fast', 'Average', 'Slow'],
					'personality_rating': ['unpleasant', 'pleasant'],
					'talking_rating': ['Too quiet', 'Average', 'Too talkative'],
					'expertise_rating': ['Unexperienced', 'Average', 'Very experienced'],
					'price_rating': ['Cheap', 'Average', 'Expensive'],
					'quality_rating': ['Terrible', 'Decent', 'Excellent']
		}				
		return render(request, 'tips/search.html', 
			{'results': results, 'query': q, 'labels': labels})
	elif request.method == 'GET':
		return render(request, 'tips/search.html', ({}))

from django import template
register = template.Library()

# type is from the set (salon, service, )
#def show (request, salon_name, type):
