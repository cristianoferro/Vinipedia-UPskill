from django.shortcuts import render
from django.views.generic import ListView, DetailView
from wine.models import Wine, Evaluation



def search(request):

    query = request.GET.get("query")

    wine_query = Wine.objects.filter(name__contains=query)

    context = {'wines': wine_query}

    return render(request, 'wine/search.html',
                  context)



class WineList(ListView):   # (Substitui o view abaixo!)
    template_name = 'wine/list.html'
    context_object_name = 'wines'   # (Alterar nome do contexto para ser usado no template)
    model = Wine

class WineDetail(DetailView):
    template_name = 'wine/detail.html'
    context_object_name = 'wine'
    model = Wine

# def wine_list(request):
#     """É a view responsavel por mandar o contexto para o template html alvo"""
#
#     wines = Wine.objects.all()
#
#     return render(request, 'wine/list.html', {'wines': wines})  # 'wines' é o nome da variável a se usar no template html

class EvaluationList(ListView):
    model = Evaluation
    template_name = 'wine/evaluation.html'
    context_object_name = 'evaluations'

def movie_detail(request, year, director, name):
    movie = get_object_or_404(Movies, released__year=year,
                             director=director,
                             name=name)
    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST) #prepopular formulário com os dados do comentário
        if review_form.is_valid():
            new_review = review_form.save(commit = False)
            new_review.movie = movie
            new_review.save()
            redirect('movies/movie_detail.html')
    elif request.method == 'GET':
        review_form = ReviewForm()

    movie_tags_ids = movie.tags.values_list('id', flat=True)
    rating_avg = Review.objects.filter(movie=movie).aggregate(Avg('rating'))

    context = {
                  'movie': movie,
                  'review_form': review_form,
                  'new_review': new_review,
                  'movie_tags_ids':movie_tags_ids,
                  'rating_avg':rating_avg
              }

    response = render(request, 'movies/movie_detail.html',
                  context)

    return response