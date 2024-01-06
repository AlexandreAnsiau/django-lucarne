from admin_ordering.admin import InlineModelAdmin, OrderableAdmin
from django_admin_inline_paginator.admin import TabularInlinePaginated
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationBaseModelAdmin

from .forms import UserCreationForm
# from .models import Category, Contact, CustomUser, Foto, Screenshot, Video
from .models import Category, Contact, CustomUser, Screenshot, Video

# admin.site.site_header = f"Administration de {settings.PROJECT_NAME}"
admin.site.site_header = _("Administration de %(project_name)s") % {"project_name": settings.PROJECT_NAME}
admin.site.site_title = admin.site.site_header
admin.site.empty_value_disaplay = "-"


# class FotoInline(TabularInlinePaginated):
#     readonly_fields = ("foto_name", "foto_display")
#     exclude = ("foto",)
#     per_page = 2
#     extra = 0
#     ordering = ["-id"]
#     verbose_name = _("Photo")
#     verbose_name_plural = _("Photos")
#
#     def foto_display(self, obj):
#         style = "max-width:300px; max-height:300px;"
#         return mark_safe(
#             f"<img style={style} src='{obj.foto.foto.url}'>")
#
#     def foto_name(self, obj):
#         return obj.foto.name
#
#     def has_add_permission(self, request, obj=None):
#         return False
#
#     foto_name.short_description = "Nom de la photo"
#     foto_display.short_description = "Photo"


# class FotosDirectorInline(FotoInline):
#     model = Foto.directors.through
#
#
# class FotosCategoryInline(FotoInline):
#     model = Foto.categories.through


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


@admin.register(CustomUser)
class CustomUserAdmin(OrderableAdmin, BaseUserAdmin, TranslationAdmin):
    add_form = UserCreationForm
    exclude = ("last_login",)
    ordering = ("email",)
    list_filter = []
    search_fields = []
    list_editable = ("ordering",)
    list_display = ("email", "representation", "ordering")
    ordering_field_hide_input = True

    @admin.display(description=_("utilisateur"))
    def representation(self, obj=None):
        return obj.__str__()

    def get_fieldsets(self, request, obj=None):
        if obj:
            profil = {}
            profil["fields"] = ["email", "first_name", "last_name",
                                "phone_number", "description_fr",
                                "description_en", "job_fr", "job_en"]
            if obj and obj.id == request.user.id:
                profil["fields"].extend(["profil_image"])
            if obj and obj.profil_image:
                profil["fields"].append("profil_image_display")
            return (("Profil", profil),)
        else:
            return (
                ("Authentification", {
                    'fields': ('email', "first_name", "last_name", 'password1', 'password2',),
                }),
            )

    def get_inlines(self, request, obj=None):
        if obj and obj.id:
            # return [VideosDirectorInline, FotosDirectorInline]
            return [VideosDirectorInline]
        else:
            return []

    def get_readonly_fields(self, request, obj=None):
        return ["profil_image_display"]

    @admin.display(description=_("photo de profil"))
    def profil_image_display(self, obj=None):
        if obj:
            return mark_safe(f"<img src={obj.profil_image.url} style='max-width:500px; max-height:500px;'>")

    def has_change_permission(self, request, obj=None):
        if (obj and obj.id == request.user.id) or obj is None:
            return True
        else:
            return False


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

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "categories":
    #         kwargs["queryset"] = Category.objects.exclude(name="photo")
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)

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


# @admin.register(Foto)
# class FotoAdmin(admin.ModelAdmin):
#
#     def get_fields(self, request, obj=None):
#         fields = ["name", "directors", "foto"]
#         if obj:
#             fields.append("foto_display")
#         return fields
#
#     def foto_display(self, obj=None):
#         style = "max-width:300px; max-height:300px;"
#         if obj:
#             return mark_safe(f"<img style={style} src='{obj.foto.url}'>")
#
#     def get_readonly_fields(self, request, obj=None):
#         return ["foto_display"]
#
#     foto_display.short_description = _("Photo")


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
        # if obj and obj.name == "photo":
        #     return [FotosCategoryInline]
        # else:
        #     return [VideosCategoryInline]
        # return [FotosCategoryInlines]
        if obj:
            return [VideosCategoryInline]
        return []

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#
#     def get_fields(self, request, obj=None):
#         fields = ["name", "url", "logo"]
#         if obj and obj.logo:
#             fields.append("logo_display")
#         return fields
#
#     def get_readonly_fields(self, request, obj=None):
#         return ["logo_display"]
#
#     def logo_display(self, obj):
#         style = "max-width:300px; max-height=300px;"
#         return mark_safe(f"<img style={style} src='{settings.STATIC_URL}{obj.logo.url}'>")

admin.site.unregister(Group)
