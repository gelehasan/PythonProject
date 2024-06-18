from django.urls import path
from . import api

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


    # Urls for the tradition view
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

]
