from django import template
from interest.models import Interest

register = template.Library()

@register.simple_tag
def get_interest_list():
    interests = Interest.objects.all()
    return interests