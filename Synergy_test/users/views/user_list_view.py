from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView

from users.db_access import DBConnector


class UserListView(TemplateView):
    template_name = "user_list.html"

    def get(self, request):
        search = request.GET.get("search")
        if search:
            request.session["search"] = search
        else:
            search = request.session.get("search", "")
        page = request.GET.get("page")
        if page:
            request.session["page"] = page
        else:
            page = request.session.get("page", "1")
        items_per_page = request.GET.get("items")
        if items_per_page:
            request.session["items_per_page"] = items_per_page
        else:
            items_per_page = request.session.get("items_per_page", "15")
        context = self.get_context_data(search=search, page=page, items_per_page=items_per_page)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        name = kwargs.get("search")
        page = kwargs.get("page")
        items_per_page = kwargs.get("items_per_page")
        paginator = Paginator(DBConnector().get_users(name), items_per_page)
        try:
            user_list = paginator.page(page)
        except PageNotAnInteger:
            user_list = paginator.page(1)
        except EmptyPage:
            user_list = paginator.page(paginator.num_pages)
        return {"user_list": user_list, "user_search": name}
