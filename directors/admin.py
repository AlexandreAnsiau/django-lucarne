from admin_ordering.admin import OrderableAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .forms import DirectorCreationForm
from .models import Director


@admin.register(Director)
class DirectorAdmin(OrderableAdmin, BaseUserAdmin):
    add_form = DirectorCreationForm
    exclude = ("last_login",)
    ordering = ("email",)
    list_filter = []
    search_fields = []
    list_editable = ("ordering",)
    list_display = ("email", "representation", "ordering")
    ordering_field_hide_input = True

    @admin.display(description=_("realisateur"))
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