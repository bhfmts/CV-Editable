from django import template
from award.models import Award

register = template.Library()

@register.simple_tag
def get_award_list():
    awards = Award.objects.all()
    return awards