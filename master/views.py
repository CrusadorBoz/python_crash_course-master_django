from django.shortcuts import render

# Create your views here.
def index(request):
    """ The home page for master. """
    return render(request, 'master/index.html')
