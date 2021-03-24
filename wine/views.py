from django.shortcuts import render
from django.views.generic import ListView

from wine.models import Wine

class WineList(ListView):   # (Substitui o view abaixo!)
    template_name = 'wine/list.html'
    context_object_name = 'wines'
    model = Wine


# def wine_list(request):
#     """É a view responsavel por mandar o contexto para o template html alvo"""
#
#     wines = Wine.objects.all()
#
#     return render(request, 'wine/list.html', {'wines': wines})  # 'wines' é o nome da variável a se usar no template html
