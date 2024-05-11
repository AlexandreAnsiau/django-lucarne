from modeltranslation.translator import register, TranslationOptions

from .models import Video


@register(Video)
class VideoTranslate(TranslationOptions):
    fields = ("description", "name")