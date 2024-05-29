from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView,View,CreateView,UpdateView,DeleteView
from .models import Post

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class LoginView(LoginView):
   

    form_class = AuthenticationError
    authentication_form = None
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    extra_context = None



class PostList(ListView):
    model=Post
    context_object_name="post"
    template_name="blog/postlist.html"