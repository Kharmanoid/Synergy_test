from django.conf.urls import url

from users_app.views.user_create_view import UserCreateView
from users_app.views.user_edit_view import UserEditView
from users_app.views.user_list_view import UserListView
from users_app.views.course_list_view import CourseListView

urlpatterns = [
    url(r'^$', UserListView.as_view(), name="main_page"),
    url(r'^users/', UserListView.as_view(), name="user_list"),
    url(r'user/create/$', UserCreateView.as_view(), name="user_create"),
    url(r'user/edit/$', UserEditView.as_view(), name="user_edit"),
    url(r'user/edit/(?P<id>[0-9]+)', UserEditView.as_view()),
    url(r'^courses/', CourseListView.as_view(), name="course_list")
]