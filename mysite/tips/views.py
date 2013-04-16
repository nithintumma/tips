from django.http import HttpResponse
# Create your views here.
def index(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:5]
    template = loader.get_template('tips/index.html')
    context = Context({
            'latest_review_list': latest_review_list,
    })
    return HttpResponse(template.render(context))
