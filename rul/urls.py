from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random', views.random_selector, name='random'),
    path('rainbow', views.rainbow, name='rainbow'),
    path('insta_glam_selector', views.insta_glam_selector, name='insta_glam'),
    path('user_shade', views.user_shade, name='user_shade'),
    path('palette_request', views.palette_request, name='palette_request'),
    path('thanks',  TemplateView.as_view(template_name="rul/thanks.html"), name='thanks'),

]
