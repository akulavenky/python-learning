from django.urls import path
from .views import post_model_list_view

urlpatterns = [
	path('', post_model_list_view, name='list'),
]
