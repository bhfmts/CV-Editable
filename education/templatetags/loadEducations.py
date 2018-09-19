from django import template
from education.models import Education

register = template.Library()

@register.simple_tag
def get_education_list():
    educations = Education.objects.all()
    return educations 