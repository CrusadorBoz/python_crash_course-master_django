from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

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

def topic(request, topic_id):
    """ Show a single topic and all its entries """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'master/topic.html', context)

def new_topic(request):
    """ Add a new topic. """
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('master:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'master/new_topic.html', context)

def new_entry(request, topic_id):
    """ Add a new entry for a particular topic. """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('master:topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'master/new_entry.html', context)
