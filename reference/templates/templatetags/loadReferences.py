from django import template
from reference.models import Reference

register = template.Library()

@register.simple_tag
def get_reference_list():
    references = Reference.objects.all()
    return references