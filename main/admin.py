from django.conf import settings
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Administration de %(project_name)s") % {"project_name": settings.PROJECT_NAME}
admin.site.site_title = admin.site.site_header
admin.site.empty_value_display = "-"