from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

from users.db_access import DBConnector


class UserListView(TemplateView):
    template_name = "user_list.html"

    def get(self, request):
        search = request.GET.get("search")
        context = self.get_context_data(search=search)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        name = kwargs.get("search", "")
        return {"user_list": DBConnector().get_users(name)}
