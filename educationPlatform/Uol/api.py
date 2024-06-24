from rest_framework import generics, mixins
from .models import User, Course, Enrollment, CourseReview
from .serializers import *

# Basic CRUD views
class UserDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseDetail(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentDetail(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class EnrollmentList(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class CourseReviewDetail(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CourseReviewList(generics.ListCreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer


# Complex query API views
class CoursesByInstructor(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        instructor_id = self.kwargs['instructor_id']
        return Course.objects.filter(instructor__id=instructor_id)


class EnrollmentsByCourse(generics.ListAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Enrollment.objects.filter(course__id=course_id)


class StudentsByCourseCategory(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return User.objects.filter(enrollment__course__category=category).distinct()


class ReviewsByCourse(generics.ListAPIView):
    serializer_class = CourseReviewSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return CourseReview.objects.filter(course__id=course_id)


class TopRatedCourses(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.annotate(avg_rating=Avg('coursereview__rating')).order_by('-avg_rating')[:10]


class EnrollmentProgressByStudent(generics.ListAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Enrollment.objects.filter(user__id=user_id)
