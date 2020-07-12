from django import template

register = template.Library()

@register.filter
def get_object_attribute(object, attribute):
    return getattr(object, attribute)
