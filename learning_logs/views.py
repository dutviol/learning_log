from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """A pagina incial do learning log """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos. """
    topics = Topic.objects.order_by('date_added')
    contex = {'topics':topics}
    return render(request, 'learning_logs/topics.html')
