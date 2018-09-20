from about.models import About

def image_dict(request):
    ctx = {}
    abouts = About.objects.all()
    for about in abouts:
        ctx[about.name] = about.image
    return ctx
