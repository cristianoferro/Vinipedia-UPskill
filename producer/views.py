from django.views.generic import ListView, DetailView
from producer.models import Producer

class ProducerList(ListView):
    model = Producer
    template_name = 'producer/list.html'
    context_object_name = 'producers'

class ProducerDetail(DetailView):
    model = Producer
    template_name = 'producer/detail.html'
    context_object_name = 'producer'

