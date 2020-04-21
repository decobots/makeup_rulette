from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random', views.random_selector, name='random'),
    path('rainbow', views.rainbow, name='rainbow'),
    path('insta_glam_selector', views.insta_glam_selector, name='insta_glam'),
    path('user_shade', views.user_shade, name='user_shade'),

    # ex: /polls/5/results/
]
