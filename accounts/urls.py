from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('register_new_user/', views.register_new_user, name='register_new_user'),
    path('profile/', views.profile, name='profile'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout_user/', views.logout_user, name='logout_user'),

    path('profile/edit_profile/', views.edit_profile, name='edit-profile'),
]
