from django.urls import path
from website import views


app_name = 'website'

urlpatterns = [

    path('', views.home, name='home'),

    path('services/', views.services, name='services'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),

    path('create-service/', views.ServiceCreateView.as_view(), name="create-service"),
    path('update-service/<int:pk>/', views.ServiceUpdateView.as_view(), name="update-service"),
    path('delete-service/<int:pk>/', views.ServiceDeleteView.as_view(), name="delete-service"),
    path('create-reservation/', views.ReservationCreateView.as_view(), name="create-reservation"),

    # Endpoint for an async query (AJAX)
    path('get-available-hours/', views.get_available_hours, name="get_available_hours"),
]
