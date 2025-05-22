from django.urls import path

from . import views

urlpatterns = [
    
path('courses-list/', views.CourseListView.as_view(), name='courses-list'),

path('home/', views.HomeListView.as_view(), name='home'),

path('instructor-course-detail/<str:uuid>/', views.InstructorCoursesDetailView.as_view(), name='instructor-course-detail'),

path('instructor-course-delete/<str:uuid>/', views.InstructorCoursesDeleteView.as_view(), name='instructor-course-delete'),

path('instructor-course-update/<str:uuid>/', views.InstructorCoursesUpdateView.as_view(), name='instructor-course-update'),

path('instructor-courses-list/', views.InstructorCourseListView.as_view(), name='instructor-courses-list'),

path('course-create/',views.CourseCreateView.as_view(), name= 'course-create')

]
