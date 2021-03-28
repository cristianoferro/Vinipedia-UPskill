from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView
from wine.models import Wine, Evaluation
from taggit.models import Tag
from django.db.models import Q


def search(request):

    query = request.GET.get("query")
    wine_query = Wine.objects.filter(
        (Q(name__contains=query) | Q(type__name__contains=query) | Q(producer__name__contains=query))
    )
    print('TESTING##################################################################################', wine_query)
    context = {'wines': wine_query}

    return render(request, 'wine/search.html',
                  context)



class WineList(ListView):   # (Substitui o view abaixo!)
    template_name = 'wine/list.html'
    context_object_name = 'wines'   # (Alterar nome do contexto para ser usado no template)
    model = Wine
    def get_queryset(self):
        try:
            tag = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))

            if tag:
                # Filtrar tag ou lista
                return get_list_or_404(Wine, type__in=[tag])
        except:
            return get_list_or_404(Wine)

class WineDetail(DetailView):
    template_name = 'wine/detail.html'
    context_object_name = 'wine'
    model = Wine

class EvaluationList(ListView):
    model = Evaluation
    template_name = 'wine/evaluation.html'
    context_object_name = 'evaluations'
