from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User, Course, Enrollment, CourseReview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

# User Views
class UserList(ListView):
    model = User
    context_object_name = "users"
    template_name = 'uol/user_list.html'


class UserDetail(DetailView):
    model = User
    context_object_name = "user"
    template_name = 'uol/user_detail.html'


class UserCreate(CreateView):
    model = User
    fields = ['userName', 'email', 'role']
    template_name = 'uol/user_form.html'
    success_url = "/users/"

class UserUpdate(UpdateView):
    model = User
    fields = ['userName', 'email', 'role']
    template_name_suffix = '_update_form'
    success_url = "/users/"