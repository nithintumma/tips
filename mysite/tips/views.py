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

# type is from the set (salon, service, )
#def show (request, salon_name, type):
