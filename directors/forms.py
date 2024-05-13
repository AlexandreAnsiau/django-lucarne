
from .models import Director
from registrations.forms import UserCreationForm


class DirectorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Director
