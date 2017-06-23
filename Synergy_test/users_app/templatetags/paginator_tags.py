from django import template

register = template.Library()


@register.filter
def previous_range(page):
    if page == 1:
        return []
    start = page - 5 if page > 5 else 1
    return range(start, page)


@register.filter
def next_range(page, num_pages):
    if page == num_pages:
        return []
    start = page + 1
    stop = page + 6 if num_pages - page > 5 else num_pages + 1
    return range(start, stop)
