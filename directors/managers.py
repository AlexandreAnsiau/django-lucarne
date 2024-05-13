from django.contrib.auth.models import Group
from django.contrib.auth.base_user import BaseUserManager


class DirectorManager(BaseUserManager):

    def get_queryset(self):
        return Group.objects.get(name="directors").user_set.all()