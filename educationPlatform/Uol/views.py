from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User, Course, Enrollment, CourseReview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return HttpResponseRedirect('/users/')


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
    template_name = 'uol/user_form.html'
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

class CourseUpdate(UpdateView):
    model = Course
    fields = ['modelName', 'writtenExam', 'category', 'instructor']
    template_name = 'uol/course_form.html'
    success_url = "/courses/"

class CourseDelete(DeleteView):
    model = Course
    success_url = "/courses/"

# Enrollment Views
class EnrollmentList(ListView):
    model = Enrollment
    context_object_name = "enrollments"
    template_name = 'uol/enrollment_list.html'

class EnrollmentDetail(DetailView):
    model = Enrollment
    context_object_name = "enrollment"
    template_name = 'uol/enrollment_detail.html'

class EnrollmentCreate(CreateView):
    model = Enrollment
    fields = ['user', 'course', 'progress', 'status']
    template_name = 'uol/enrollment_form.html'
    success_url = "/enrollments/"

class EnrollmentUpdate(UpdateView):
    model = Enrollment
    fields = ['user', 'course', 'progress', 'status']
    template_name = 'uol/enrollment_form.html'
    success_url = "/enrollments/"

class EnrollmentDelete(DeleteView):
    model = Enrollment
    success_url = "/enrollments/"

# CourseReview Views
class CourseReviewList(ListView):
    model = CourseReview
    context_object_name = "reviews"
    template_name = 'uol/review_list.html'

class CourseReviewDetail(DetailView):
    model = CourseReview
    context_object_name = "review"
    template_name = 'uol/review_detail.html'

class CourseReviewCreate(CreateView):
    model = CourseReview
    fields = ['user', 'course', 'rating', 'comment']
    template_name = 'uol/review_form.html'
    success_url = "/reviews/"

class CourseReviewUpdate(UpdateView):
    model = CourseReview
    fields = ['user', 'course', 'rating', 'comment']
    template_name = 'uol/review_form.html'
    success_url = "/reviews/"

class CourseReviewDelete(DeleteView):
    model = CourseReview
    success_url = "/reviews/"
