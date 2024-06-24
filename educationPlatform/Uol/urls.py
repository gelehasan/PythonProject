from django.urls import path
from . import api, views

urlpatterns = [
    # Basic CRUD API views
    path('api/users/', api.UserList.as_view(), name='user_list_api'),
    path('api/user/<int:pk>/', api.UserDetail.as_view(), name='user_detail_api'),
    path('api/courses/', api.CourseList.as_view(), name='course_list_api'),
    path('api/course/<int:pk>/', api.CourseDetail.as_view(), name='course_detail_api'),
    path('api/enrollments/', api.EnrollmentList.as_view(), name='enrollment_list_api'),
    path('api/enrollment/<int:pk>/', api.EnrollmentDetail.as_view(), name='enrollment_detail_api'),
    path('api/reviews/', api.CourseReviewList.as_view(), name='review_list_api'),
    path('api/review/<int:pk>/', api.CourseReviewDetail.as_view(), name='review_detail_api'),

    # Complex query API views
    path('api/courses/instructor/<int:instructor_id>/', api.CoursesByInstructor.as_view(), name='courses_by_instructor'),
    path('api/enrollments/course/<int:course_id>/', api.EnrollmentsByCourse.as_view(), name='enrollments_by_course'),
    path('api/students/category/<str:category>/', api.StudentsByCourseCategory.as_view(), name='students_by_category'),
    path('api/reviews/course/<int:course_id>/', api.ReviewsByCourse.as_view(), name='reviews_by_course'),
    path('api/courses/top-rated/', api.TopRatedCourses.as_view(), name='top_rated_courses'),
    path('api/enrollments/student/<int:user_id>/', api.EnrollmentProgressByStudent.as_view(), name='enrollment_progress_by_student'),

    # Traditional view URLs
    # User URLs
    path('users/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user/add/', views.UserCreate.as_view(), name='user_add'),
    path('user/update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),

    # Course URLs
    path('courses/', views.CourseList.as_view(), name='course_list'),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('course/add/', views.CourseCreate.as_view(), name='course_add'),
    path('course/update/<int:pk>/', views.CourseUpdate.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', views.CourseDelete.as_view(), name='course_delete'),

    # Enrollment URLs
    path('enrollments/', views.EnrollmentList.as_view(), name='enrollment_list'),
    path('enrollment/<int:pk>/', views.EnrollmentDetail.as_view(), name='enrollment_detail'),
    path('enrollment/add/', views.EnrollmentCreate.as_view(), name='enrollment_add'),
    path('enrollment/update/<int:pk>/', views.EnrollmentUpdate.as_view(), name='enrollment_update'),
    path('enrollment/delete/<int:pk>/', views.EnrollmentDelete.as_view(), name='enrollment_delete'),

    # CourseReview URLs
    path('reviews/', views.CourseReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', views.CourseReviewDetail.as_view(), name='review_detail'),
    path('review/add/', views.CourseReviewCreate.as_view(), name='review_add'),
    path('review/update/<int:pk>/', views.CourseReviewUpdate.as_view(), name='review_update'),
    path('review/delete/<int:pk>/', views.CourseReviewDelete.as_view(), name='review_delete'),
]
