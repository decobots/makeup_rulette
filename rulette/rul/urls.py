from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random', views.random_selector, name='random'),
    path('shade_detail/<int:shade_id>', views.shade_detail, name='shade_detail'),
    path('insta_glam_selector', views.insta_glam_selector, name='insta_glam'),

    # ex: /polls/5/results/
]
