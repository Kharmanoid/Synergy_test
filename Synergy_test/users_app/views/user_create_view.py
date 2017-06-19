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
        return self.render_to_response({"form": UserForm()})

    def form_valid(self, form):
        DBConnector().add_new_user(form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
