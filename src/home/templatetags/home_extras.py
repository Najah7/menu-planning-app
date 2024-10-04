from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(value, arg):
    return value.split(arg)


@register.filter
def doEnumerate(sequence):
    return enumerate(sequence)


@register.filter
def add(value, arg):
    return value + arg
