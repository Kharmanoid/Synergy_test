import copy

from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from users_app.db_access import DBConnector
from users_app.forms.user_form import UserForm


class UserEditView(FormView):
    form_class = UserForm
    template_name = "user_edit.html"
    success_url = reverse_lazy("user_list")

    def get(self, request, **kwargs):
        context = self.get_context_data(id=kwargs.get("id"))
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.user_id = request.POST.get("id")
        course_id = request.POST.get("course")
        if course_id:
            DBConnector().add_course_to_user(self.user_id, course_id)
        form = self.get_form()
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return HttpResponseRedirect(request.get_full_path())

    def get_context_data(self, **kwargs):
        context = {}
        if not hasattr(self, "user_id"):
            self.user_id = kwargs.get("id")
        self.user = copy.deepcopy(DBConnector().get_user_by_id(self.user_id))
        if "form" in kwargs:
            context = super(UserEditView, self).get_context_data(**kwargs)
        else:
            context["form"] = self._prepare_form()
        context["available_courses"] = self._prepare_available_courses()
        context["selected_courses"] = self.user.get("courses")
        return context

    def _prepare_form(self):
        if self.user.get("status") == "Active":
            self.user["status"] = 2
        else:
            self.user["status"] = 1
        return UserForm(self.user)

    def _prepare_available_courses(self):
        selected = self.user.get("courses")
        if not selected:
            return DBConnector().get_courses()
        available = []
        for course in DBConnector().get_courses():
            if course.get("id") not in selected:
                available.append(course)
        return available

    def form_valid(self, form):
        DBConnector().update_user(form.cleaned_data)
