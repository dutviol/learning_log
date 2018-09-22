"""Define padrões de urls para learning_logs"""

from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Pagina incial
    path('', views.index.as_view(), name='index'),

    #Mostrar todos os assuntos
    path('topics/', views.topics.as_view(), name='topics'),
]
