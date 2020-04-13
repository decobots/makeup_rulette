from django.db.models import Q
from django.shortcuts import render

from .models import Shade


def index(request):
    return render(request, 'rul/base.html', {})


def random_selector(request):
    shades = Shade.objects.all().order_by('?')[:5]
    context = {'shades_list': shades,
               'eye_parts': ['Inner', 'Crease', 'Outer V', 'Blending']}
    return render(request, 'rul/random.html', context)


# <img src="media/eye_template/IMG_0579.PNG"/>
def insta_glam_selector(request):
    crease = Shade.objects.filter(texture='M', darkness=3).all().order_by('?')[:1]
    inner = Shade.objects.filter(Q(texture='Sh') | Q(texture='Sp') | Q(texture='G') | Q(darkness__gt=3)).all().order_by(
        '?')[:1]
    outer_v = Shade.objects.filter(darkness__lt=3).all().order_by('?')[:1]
    blending = Shade.objects.filter(darkness__gt=3).all().order_by('?')[:1]
    context = {"crease": crease[0], 'inner': inner[0], 'outer_v': outer_v[0], 'blending': blending[0]}
    return render(request, 'rul/insta_glam_selector.html', context)


def shade_detail(request, shade_id):
    shade = Shade.objects.get(pk=shade_id)
    return render(request, 'rul/shade_details.html', {'shade': shade})
