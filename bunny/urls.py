from django.urls import path
from bunny.views import home


urlpatterns = [
    path('home/', home, name='home'),
]