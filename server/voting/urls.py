from django.urls import path
from .views import vulnerable_view

urlpatterns = [
    path('vulnerable/', vulnerable_view, name='vulnerable_view'),

]
