from django import template
from ..models import Evaluation, Wine

register = template.Library()


@register.inclusion_tag("wine/evaluations.html")
def show_latest_evaluations(count=4, instance=None):
    latest_evaluations = Evaluation.objects.all()[:count]

    if instance:
        latest_evaluations = Evaluation.objects.filter(wine=instance)

    return {"latest_evaluations": latest_evaluations}


@register.inclusion_tag("wine/trending.html")
def get_trending_wines(count=4):
    trending_wines = Wine.objects.all()
    trending_wines = trending_wines.order_by("-pageviews")[:count]
    return {"trending_wines": trending_wines}


@register.inclusion_tag("wine/attribution.html")
def show_attribution(model):
    picture_author = model.img_author
    return {"picture_author": picture_author}
