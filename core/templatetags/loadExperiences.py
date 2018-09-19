from django import template
from core.models import Experience

register = template.Library()

@register.simple_tag
def get_experience_list():
    experiences = Experience.objects.all()
    return experiences  