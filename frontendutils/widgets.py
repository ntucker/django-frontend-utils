from django import forms
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode


class DateTimePicker(forms.DateTimeInput):
    def __init__(self, attrs=None):
        default_attrs = {'class':'date-time'}
        if attrs:
            default_attrs.update(attrs)
        super(DateTimePicker, self).__init__(default_attrs)
    def render(self, *args, **kwargs):
        ret = super(DateTimePicker, self).render(*args, **kwargs)
        return mark_safe(u"""<div class="input-prepend"><span class="add-on"><i class="icon-time"></i></span>{0}</div>""".format(ret))

    class Media:
        js = ('js/jquery-ui-timepicker-addon.js',) 

class TagInput(forms.TextInput):
    suggestions = []
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        tag_class = u" ".join((final_attrs.get('class', ""), 'tag-list'))
        ini_element = '<div class="tag-data">%s</div>' % force_unicode(value) if value else ""
        return mark_safe(u"""<i class="icon-tags pull-left" style="position:relative;bottom:-5px;"></i><div data-id="%s" class="%s" data-suggestions="%s" >%s<div class="tags"></div></div>
        <input type='hidden'%s />""" % (final_attrs['id'], tag_class, u",".join(self.suggestions), ini_element, flatatt(final_attrs)))
    class Media:
        js = ('bootstrap/js/bootstrap-tags.js', )