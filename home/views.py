from django.shortcuts import render
from .forms import TextForm
from .models import Text


def index(request):
    text_form = TextForm()
    if request.method == 'POST':
        text = request.POST.get('text', None)
        lang = request.POST.get('lang', None)
        text_form = TextForm(request.POST)
        if text_form.is_valid():
            text_form.save()
        print(request)

    return render(request, 'index.html', {'form': text_form})



