from django import template
import datetime

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().month(format_string)