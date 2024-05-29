from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
app_name="blog"
urlpatterns = [
   
    path('', views.index, name='index'),
    # Other URL patterns here...

    path('postlist/',views.PostList.as_view(), name='listpost'),


    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='/login/'), name="logout"),
    

]