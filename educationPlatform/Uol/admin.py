from django.contrib import admin
from .models import User, Course, Enrollment, CourseReview
from .forms import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('userName', 'email', 'role', 'joinDate')

class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('modelName', 'writtenExam', 'category', 'instructor', 'publishDate')

class EnrollmentAdmin(admin.ModelAdmin):
    form = EnrollmentForm
    list_display = ('user', 'course', 'enrollmentDate', 'progress', 'status')
  
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'comment', 'ReviewDate')

admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(CourseReview, CourseReviewAdmin)