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


class UserDelete(DeleteView):
    model = User
    success_url = "/users/"


# Course Views
class CourseList(ListView):
    model = Course
    context_object_name = "courses"
    template_name = 'uol/course_list.html'

class CourseDetail(DetailView):
    model = Course
    context_object_name = "course"
    template_name = 'uol/course_detail.html'


class CourseCreate(CreateView):
    model = Course
    fields = ['modelName', 'writtenExam', 'category', 'instructor']
    template_name = 'uol/course_form.html'
    success_url = "/courses/"