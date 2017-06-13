from django.views.generic.base import TemplateView

from users.db_access import DBConnector


class CourseListView(TemplateView):
    template_name = "course_list.html"

    def get_context_data(self, **kwargs):
        return {"course_list": DBConnector().get_courses()}