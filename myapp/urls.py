from django.urls import re_path
from .views import discipline_detail, discipline_list_published, student_list, student_detail, student_list_published, teacher_list
from . import views

urlpatterns = [
    re_path(r'^api/$', views.index, name='index'),
    re_path(r'^api/myapp/(?P<pk>[0-9]+)$', discipline_detail),
    re_path(r'^api/myapp/published$', discipline_list_published),
    re_path(r'^api/students$', views.students, name='students'),
    re_path(r'^api/students/(?P<pk>[0-9]+)$', student_detail),
    re_path(r'^api/students/published$', student_list_published),
    re_path(r'^api/teacher/', student_detail),
]
