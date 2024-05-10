from admin_ordering.admin import OrderableAdmin
from django_admin_inline_paginator.admin import TabularInlinePaginated
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Category, Screenshot, Video


class VideoInline(TabularInlinePaginated):
    exclude = ("video",)
    readonly_fields = ("video_name", "video_display",)
    extra = 0
    verbose_name = _("Video")
    verbose_name_plural = _("Videos")
    ordering_field_hide_input = True

    @admin.display(description=_("Video"))
    def video_display(self, obj):
        style = "max-width:500px; max-height:500px;"
        return mark_safe(
            f"<video style={style} controls><source src='{obj.video.video.url}' type=video/mp4></video>")

    @admin.display(description=_("Nom de la video"))
    def video_name(self, obj):
        return obj.video.name

    def has_add_permission(self, request, obj=None):
        return False

    def __str__(self):
        return self.video.name


class VideosDirectorInline(VideoInline):
    model = Video.directors.through


class VideosCategoryInline(VideoInline):
    model = Video.categories.through


class ScreenshotInline(OrderableAdmin, admin.TabularInline):
    model = Screenshot
    extra = 0
    verbose_name = _("screenshot")
    verbose_name_plural = _("screenshots")
    ordering_field_hide_input = True

    @admin.display(description=_("screenshot"))
    def screenshot_display(self, obj):
        if obj:
            style = "max-width:100px; max-height:100px;"
            return mark_safe(f"<img style={style} src='{obj.screenshot.url}'>")

    def get_readonly_fields(self, request, obj=None):
        return ["screenshot_display"]

    def has_add_permission(self, request, obj=None):
        return True


@admin.register(Video)
class VideoAdmin(OrderableAdmin, admin.ModelAdmin):
    inlines = [ScreenshotInline]
    list_editable = ("ordering",)
    list_display = ("name", "ordering")
    ordering_field_hide_input = True

    def get_fields(self, request, obj=None):
        fields = ["name_fr", "name_en", "video", "presentation_video", "directors", "categories", "description_fr",
                  "description_en"]
        if obj:
            fields.append("video_display")
            if obj.presentation_video:
                fields.append("presentation_video_display")
        return fields


    @admin.display(description=_("video"))
    def video_display(self, obj=None):
        if obj:
            style = "max-width:500px; max-height:500px;"
            return mark_safe(
                f"<video style={style} controls><source src='{obj.video.url}' type=video/mp4></video>"
            )

    @admin.display(description=_("video de présentation"))
    def presentation_video_display(self, obj=None):
        if obj and obj.presentation_video:
            style = "max-width:500px; max-height:500px;"
            return mark_safe(
                f"<video style={style} controls><source src='{obj.presentation_video.url}' type=video/mp4></video>"
            )

    def get_readonly_fields(self, request, obj=None):
        return ["video_display", "presentation_video_display"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        fields = ["name", "presentation_video"]
        if obj and obj.presentation_video:
            fields.append("presentation_video_display")
        return fields

    def get_readonly_fields(self, request, obj=None):
        return ["name", "presentation_video_display"]

    @admin.display(description=_("video de présentation"))
    def presentation_video_display(self, obj=None):
        if obj:
            style = "max-width:500px; max-height=500px;"
            return mark_safe(
                f"<video style={style} controls><source src='{obj.presentation_video.url}' type=video/mp4></video>"
            )

    def get_inlines(self, request, obj=None):
        if obj:
            return [VideosCategoryInline]
        return []

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

