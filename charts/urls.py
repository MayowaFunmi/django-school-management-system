from django.urls import path
from . import views


app_name = 'charts'

urlpatterns = [
    path('', views.linear_graph, name='linear_graph')
]