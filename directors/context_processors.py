from .models import Director


def directors(request):
    context = {}
    context["directors"] = Director.objects.all()
    return context