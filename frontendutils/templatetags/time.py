from django import template
from django.conf import settings
from django.template.defaultfilters import date
from django.utils.timezone import localtime

register = template.Library()

@register.inclusion_tag('utils/tags/show_time.html')
def show_time(time, time_display=None, pubdate=False, itemprop=None):
    context = {'time': time, 'pubdate':pubdate}
    if time_display:
        context['time_display'] = time_display
    else:
        context['time_display'] = date(localtime(time), settings.DATETIME_FORMAT) if time else ""
    context['itemprop'] = itemprop
    return context