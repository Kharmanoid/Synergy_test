from django.conf.urls import url

from users.views.user_list_view import UserListView
from users.views.course_list_view import CourseListView

urlpatterns = [
    url(r'^$', UserListView.as_view(), name="main_page"),
    url(r'^users/', UserListView.as_view(), name="user_list"),
    url(r'^courses/', CourseListView.as_view(), name="course_list")
]