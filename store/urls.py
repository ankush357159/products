from django.urls import path, include
from store.views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path("create/", create_view, name='create_view'),
    path("list/", list_view, name='list_view'),
    path("<pk>/", detail_view, name='detail'),
    path("<pk>/update/", update_view, name='detail'),
    path("<pk>/delete/", delete_view, name='detail'),
]
