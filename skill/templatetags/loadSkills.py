from django import template
from skill.models import Skill

register = template.Library()

@register.simple_tag
def get_skill_list():
    skills = Skill.objects.all()
    return skills 