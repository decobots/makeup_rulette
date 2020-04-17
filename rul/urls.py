from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random', views.random_selector, name='random'),
    path('shade_detail/<int:shade_id>', views.shade_detail, name='shade_detail'),
    path('rainbow', views.rainbow, name='rainbow'),
    path('insta_glam_selector', views.insta_glam_selector, name='insta_glam'),
    path('user_palette', views.user_palette, name='user_palette'),
    path('user_palette_saved', views.user_palette_saved, name='user_palette_saved'),

    # ex: /polls/5/results/
]
