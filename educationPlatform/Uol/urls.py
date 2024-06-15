from django.urls import path
from . import api

urlpatterns = [
    # User API URLs
    path('api/users/', api.UserList.as_view(), name='user_list_api'),
    path('api/user/<int:pk>/', api.UserDetail.as_view(), name='user_detail_api'),

    # Course API URLs
    path('api/courses/', api.CourseList.as_view(), name='course_list_api'),
    path('api/course/<int:pk>/', api.CourseDetail.as_view(), name='course_detail_api'),

    # Enrollment API URLs
    path('api/enrollments/', api.EnrollmentList.as_view(), name='enrollment_list_api'),
    path('api/enrollment/<int:pk>/', api.EnrollmentDetail.as_view(), name='enrollment_detail_api'),

    # CourseReview API URLs
    path('api/reviews/', api.CourseReviewList.as_view(), name='review_list_api'),
    path('api/review/<int:pk>/', api.CourseReviewDetail.as_view(), name='review_detail_api'),
]