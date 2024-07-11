# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import scriptingLang

# Create your views here.

def firstapp(request):
    scripting_langs = scriptingLang.objects.all()
    return render(request, 'firstapp/firstapp.html', {'scriptingLang': scripting_langs})


def detail(request, script_id):
    get_obj = get_object_or_404(scriptingLang, pk=script_id)
    return render(request, 'firstapp/detail.html', {'get_obj': get_obj})