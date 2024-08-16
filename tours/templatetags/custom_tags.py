from django import template

register = template.Library()

@register.filter(name='range')
def range_filter(n):
    return range(n)
