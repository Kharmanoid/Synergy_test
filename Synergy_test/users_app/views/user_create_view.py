from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView

from users_app.db_access import DBConnector
from users_app.forms.user_form import UserForm


class UserCreateView(FormView):
    form_class = UserForm
    template_name = "user_create.html"
    success_url = reverse_lazy("user_list")

    def get(self, request, **kwargs):
        context = {"form": UserForm()}
        if kwargs.get("success"):
            context["result_success"] = True
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.form_valid(form)
            url = request.get_full_path()
            if request.POST.get("create"):
                url += "/success"
        else:
            return self.form_invalid(form)
        return HttpResponseRedirect(url)

    def form_valid(self, form):
        DBConnector().add_new_user(form.cleaned_data)
