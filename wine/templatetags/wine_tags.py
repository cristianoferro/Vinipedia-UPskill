from django import template
from ..models import Evaluation

register = template.Library()

@register.inclusion_tag("wine/evaluations.html")
def show_latest_evaluations(count=5, instancia=None):
    latest_evaluations = Evaluation.objects.all()[:count]

    if instancia:
        latest_evaluations = Evaluation.objects.filter(wine=instancia)


    return {"latest_evaluations": latest_evaluations}