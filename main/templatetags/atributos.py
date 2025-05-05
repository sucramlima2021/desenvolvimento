from django import template

register = template.Library()

@register.filter
def attr(obj, nome):
    return getattr(obj, nome, '')
