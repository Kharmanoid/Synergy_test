from django.views.generic.base import TemplateView


class UserListView(TemplateView):
    template_name = "user_list.html"

    def get_context_data(self, **kwargs):
        return {"data": ["ONE", "TWO", "THREE"]}
