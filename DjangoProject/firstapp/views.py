# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import scriptingLang, ScriptsStore
from .forms import ScriptVarietyForm 
# Create your views here.

def firstapp(request):
    scripting_langs = scriptingLang.objects.all()
    return render(request, 'firstapp/firstapp.html', {'scriptingLang': scripting_langs})


def detail(request, script_id):
    get_obj = get_object_or_404(scriptingLang, pk=script_id)
    return render(request, 'firstapp/detail.html', {'get_obj': get_obj})


def order(request):
    return render(request, 'firstapp/order.html')

def script_store_view(request):
    stores =None
    if request.method =="POST":
        form = ScriptVarietyForm(request.POST)
        if  form.is_valid():
            script_variety = form.cleaned_data['script_variety'] # from.py link
            stores =ScriptsStore.objects.filter(script_varieties=script_variety)
    else:
        form = ScriptVarietyForm()
    return render(request, 'firstapp/script_stores.html',{'stores':stores,'form':form})