from django.urls import path
from . import views


app_name = 'mathematics'

urlpatterns = [
    path('simultaneous_eqn/', views.simultaneous_eqn, name='simultaneous_eqn'),
    path('simultaneous_eqn_answer/', views.SimultaneousEqn.as_view(), name='simultaneous_eqn_answer'),
    path('simultaneous_3_eqn/', views.simultaneous_3_eqn, name='simultaneous_3_eqn'),
    path('simultaneous_3_eqn_answer/', views.SimultaneousThreeEqn.as_view(), name='simultaneous_3_eqn_answer'),
]