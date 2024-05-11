from registrations.forms import UserCreationForm


class DirectorCreationForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_director = True
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
