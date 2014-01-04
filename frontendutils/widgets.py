from django import forms
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.forms.util import flatatt
from django.utils.html import escape, conditional_escape


class DateTimePicker(forms.DateTimeInput):
    def __init__(self, attrs=None, format=None):
        default_attrs = {'class':'date-time'}
        if attrs:
            default_attrs.update(attrs)
        super(DateTimePicker, self).__init__(default_attrs, format)
    def render(self, *args, **kwargs):
        ret = super(DateTimePicker, self).render(*args, **kwargs)
        return mark_safe(u"""<div class="input-group"><span class="input-group-addon"><i class="icon-time"></i></span>{0}</div>""".format(ret))

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js',
              '//ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js',
              'js/lib/jquery-ui-timepicker-addon.js',)
        css = {'all': ('css/jqueryui.css',)}

class TagInput(forms.TextInput):
    suggestions = []
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        tag_class = u" ".join((final_attrs.get('class', ""), 'tag-list'))
        ini_element = '<div class="tag-data">%s</div>' % force_text(value) if value else ""
        return mark_safe(u"""<i class="icon-tags pull-left" style="position:relative;bottom:-5px;"></i><div data-id="%s" class="%s" data-suggestions="%s" >%s<div class="tags"></div></div>
        <input type='hidden'%s />""" % (final_attrs['id'], tag_class, u",".join(self.suggestions), ini_element, flatatt(final_attrs)))
    class Media:
        js = ('bootstrap/js/bootstrap-tags.js', )