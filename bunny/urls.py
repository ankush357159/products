from django.urls import path
from bunny.views import home, myPetCreateView


urlpatterns = [
    path('home/', home, name='home'),
    path('create-pet/', myPetCreateView, name='create-my-pet'),
]