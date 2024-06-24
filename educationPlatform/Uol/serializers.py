from rest_framework import serializers
from .models import User, Course, Enrollment, CourseReview

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName', 'email', 'role', 'joinDate']


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'modelName', 'writtenExam', 'category', 'instructor', 'publishDate']


class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrollmentDate', 'progress', 'status']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        course_data = validated_data.pop('course')

        # Finds or creates the User
        user, created = User.objects.get_or_create(
            userName=user_data['userName'],
            defaults={
                'email': user_data['email'],
                'role': user_data['role'],
                'joinDate': user_data['joinDate']
            }
        )

        # Finds or creates the Course
        course, created = Course.objects.get_or_create(
            id=course_data['id'],
            defaults={
                'modelName': course_data['modelName'],
                'writtenExam': course_data['writtenExam'],
                'category': course_data['category'],
                'instructor': course_data['instructor'],
                'publishDate': course_data['publishDate']
            }
        )

        # Creates the Enrollment instance
        enrollment = Enrollment.objects.create(user=user, course=course, **validated_data)
        return enrollment


class CourseReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = CourseReview
        fields = ['id', 'user', 'course', 'rating', 'comment', 'ReviewDate']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        course_data = validated_data.pop('course')

        # Finds or creates the User
        user, created = User.objects.get_or_create(
            userName=user_data['userName'],
            defaults={
                'email': user_data['email'],
                'role': user_data['role'],
                'joinDate': user_data['joinDate']
            }
        )

        # Finds or creates the Course
        course, created = Course.objects.get_or_create(
            id=course_data['id'],
            defaults={
                'modelName': course_data['modelName'],
                'writtenExam': course_data['writtenExam'],
                'category': course_data['category'],
                'instructor': course_data['instructor'],
                'publishDate': course_data['publishDate']
            }
        )

        # Creates the CourseReview instance
        course_review = CourseReview.objects.create(user=user, course=course, **validated_data)
        return course_review
