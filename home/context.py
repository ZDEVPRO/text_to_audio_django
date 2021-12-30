from .models import Text


def audio(request):
    text = Text.objects.all().order_by('-id')[:1]
    context = {
        'text': text,
    }
    return context
