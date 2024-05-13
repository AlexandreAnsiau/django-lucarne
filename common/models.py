from pathlib import Path

from django.db import models
from django.db.models.fields.files import FileField


class FileModel(models.Model):

    class Meta:
        abstract = True

    def delete(self):
        for field in self._meta.fields:
            if isinstance(field, FileField):
                file = getattr(self, field.name)
                Path(file.path).unlink()
        super().delete()

