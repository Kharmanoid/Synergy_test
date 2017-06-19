from django import template

register = template.Library()

@register.filter
def navigate_page(current_url, page):
    if '?' in current_url:
        return current_url + ";page=" + str(page)
    return current_url + "?page=" + str(page)