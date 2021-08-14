from django.urls import path

from website import views

app_name = 'website'

urlpatterns = [
    # path('',views.test, name='test'),
    path('', views.home, name='home'),
    # path('services', views.services, name="services"),
    # path('reservation', views.reservation, name='reservation'),
    # path('contact', views.contact, name='contack'),
    # path('about', views.about,name='about'),
    # path('gallery', views.gallery, name='gallery'),

]