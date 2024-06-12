# forms.py
from django import forms
from .models import *

class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instructor'].queryset = User.objects.filter(role='Teacher')


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the user queryset to only include students
        self.fields['user'].queryset = User.objects.filter(role='Student')