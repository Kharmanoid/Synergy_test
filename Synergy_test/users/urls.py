from django.conf.urls import url

from users.views.user_list_view import UserListView

urlpatterns = [
    url(r'^users/', UserListView.as_view(), name="user_list")
]