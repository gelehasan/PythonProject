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