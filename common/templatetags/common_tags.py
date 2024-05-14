from itertools import zip_longest

from django import template
from django.conf import settings
from django.utils.translation import activate, get_language
from django.urls import resolve, reverse

register = template.Library()


@register.filter
def add_css_class(form_field, args):
    return form_field.as_widget(attrs={"class": args})


@register.simple_tag(takes_context=True)
def change_lang(context, language_code):
    resolver_match_instance = resolve(context["request"].path)
    current_language = get_language()
    activate(language_code)
    url = reverse(resolver_match_instance.view_name,
                  kwargs=resolver_match_instance.kwargs)
    activate(current_language)

    return url


@register.filter
def zip_longest_iterable(iterable_1, iterable_2):
    iterables = [
        range(iterable) if isinstance(iterable, int) else iterable
        for iterable in [iterable_1, iterable_2]
    ]
    return zip_longest(*iterables)


@register.simple_tag(name="setting")
def get_setting(setting):
    return getattr(settings, setting)
