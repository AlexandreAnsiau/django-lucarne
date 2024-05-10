from registrations.forms import UserCreationForm


class DirectorCreationForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_director = True
        if commit:
            user.save()
        return user
