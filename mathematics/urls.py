from django.urls import path
from . import views


app_name = 'mathematics'

urlpatterns = [
    path('simultaneous_eqn/', views.simultaneous_eqn, name='simultaneous_eqn'),
    path('simultaneous_eqn_answer/', views.SimultaneousEqn.as_view(), name='simultaneous_eqn_answer'),
    path('simultaneous_3_eqn/', views.simultaneous_3_eqn, name='simultaneous_3_eqn'),
    path('simultaneous_3_eqn_answer/', views.SimultaneousThreeEqn.as_view(), name='simultaneous_3_eqn_answer'),
    path('quadratic_eqn/', views.quadratic_eqn, name='quadratic_eqn'),
    path('quadratic_eqn_answer/', views.QuadraticEqn.as_view(), name='quadratic_eqn_answer'),
    path('from_base_10/', views.from_base_10, name='from_base_10'),
    path('from_base_10_answer/', views.FromBase10.as_view(), name='from_base_10_answer'),
    path('to_base_10/', views.to_base_10, name='to_base_10'),
    path('to_base_10_answer/', views.ToBase10.as_view(), name='to_base_10_answer'),
    path('add_bases/', views.add_bases, name='add_bases'),
    path('add_bases_answer/', views.AddBases.as_view(), name='add_bases_answer'),
]