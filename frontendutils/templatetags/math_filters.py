import math

from django import template
from django.conf import settings


register = template.Library()

@register.filter
def multiply(value, arg):
    return int(value) * int(arg)

@register.filter
def subtract(value, arg):
    return int(value) - int(arg)

@register.filter
def divide(value, arg):
    value, arg = int(value), int(arg)
    return value / arg, value % arg

@register.filter
def ceil_divide(value, arg):
    value, arg = int(value), int(arg)
    return int(math.ceil(float(value) / arg))
