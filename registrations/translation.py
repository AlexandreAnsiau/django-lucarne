from modeltranslation.translator import register, TranslationOptions

from .models import CustomUser


@register(CustomUser)
class CustomUserTranslate(TranslationOptions):
    fields = ("description", "job")