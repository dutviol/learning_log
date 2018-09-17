"""Define padrões de urls para learning_logs"""

from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    #Pagina incial
    url('', views.index, name='index'),
]
