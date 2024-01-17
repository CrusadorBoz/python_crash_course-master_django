from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    """ The home page for master. """
    return render(request, 'master/index.html')


def topics(request):
    """ Show all topics . """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'master/topics.html', context)


def pizza(request):
    """ The home page for Pizza:
    This was an example for how to create a seprate page """
    return render(request, 'pizza/index.html')
