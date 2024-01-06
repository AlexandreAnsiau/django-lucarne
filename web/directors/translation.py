from modeltranslation.translator import register, TranslationOptions

from .models import CustomUser, Video


@register(CustomUser)
class CustomUserTranslate(TranslationOptions):
    fields = ("description", "job")


@register(Video)
class VideoTranslate(TranslationOptions):
    fields = ("description", "name")
