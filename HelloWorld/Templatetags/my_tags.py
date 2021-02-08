from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def radio_gender_filter(v1, v2):
    if (not v1 or v1 == 'male') and v2 == 'male':
        return 'checked'
    elif v1 == 'female' and v2 == 'female':
        return 'checked'
    else:
        return ''


@register.filter
def my_filter(v1):
    return v1 + v1


@register.simple_tag
def my_tags(v1, v2, v3):
    return v1 + str(v2) + str(v3)


@register.simple_tag
def my_html(v1, v2):
    temp_html = '<input type="text" id="%s" value="%s"/>' % (
        v1, v2)
    return mark_safe(temp_html)
