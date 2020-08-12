from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('new', views.create_post_view, name='create_post_view'),
    path('new/new', views.create_post, name='create_post')
]