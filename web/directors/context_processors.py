from .forms import EmailForm
from .models import CustomUser


def base_context(request):
    context = {}
    context["directors"] = CustomUser.objects.all()[:4]
    context["email_form"] = EmailForm
    return context
