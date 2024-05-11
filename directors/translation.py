from modeltranslation.translator import register, TranslationOptions

from .models import Director
from registrations.translation import CustomUserTranslate


@register(Director)
class DirectorTranslate(CustomUserTranslate):
    pass