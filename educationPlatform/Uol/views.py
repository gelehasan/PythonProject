from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User, Course, Enrollment, CourseReview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
