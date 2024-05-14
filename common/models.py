from pathlib import Path

from django.conf import settings
from django.db import models
from django.db.models.fields.files import FileField


class FileModel(models.Model):

    class Meta:
        abstract = True

    def delete(self):
        for field in self._meta.fields:
            if isinstance(field, FileField):
                file = getattr(self, field.name)
                if file:
                    file_path = Path(file.path)
                    if file_path.is_file() and settings.MEDIA_DEFAULT not in set(file_path.parents):
                        file_path.unlink()
        super().delete()