from django import template

register = template.Library()

@register.filter
def get_object_attribute(object, attribute):
    return getattr(object, attribute)

@register.filter
def add_remove_day(day, add_or_remove):
    if add_or_remove == "add":
        day += 1
    elif add_or_remove == "remove":
        day -= 1
    return day

# @register.filter
# def add_day(day):
#     day += 1
#     return day
#
# @register.filter
# def remove_day(day):
#     day -= 1
#     return day
