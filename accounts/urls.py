from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('change_profile_settings',views.change_profile_settings, name='change_profile_settings'),
    path('follow',views.follow,name='follow'),
    path('unfollow',views.unfollow,name='unfollow'),


]