from django.urls import path, re_path
from .views import (
    post_model_detail_view,
    post_model_list_view
    )

urlpatterns = [
	path('', post_model_list_view, name='list'),
	re_path(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'),
]
