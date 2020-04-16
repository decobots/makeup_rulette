from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from .models import Shade


def index(request):
    return render(request, 'rul/index.html', {})


@login_required
def random_selector(request):
    shades = Shade.objects.all().order_by('?')[:4]
    context = {'shades_list': shades}
    return render(request, 'rul/random.html', context)


@login_required
def insta_glam_selector(request):
    crease = Shade.objects.filter(texture='M', darkness=3).all().order_by('?')[:1]
    inner = Shade.objects.filter(Q(texture='Sh') | Q(texture='Sp') | Q(texture='G') | Q(darkness__gt=3)).all().order_by(
        '?')[:1]
    outer_v = Shade.objects.filter(darkness__lt=3).all().order_by('?')[:1]
    blending = Shade.objects.filter(darkness__gt=3).all().order_by('?')[:1]
    context = {"shades_list": [crease[0], inner[0], outer_v[0], blending[0]]}
    return render(request, 'rul/insta_glam_selector.html', context)


@login_required
def shade_detail(request, shade_id):
    shade = Shade.objects.get(pk=shade_id)
    return render(request, 'rul/shade_details.html', {'shade': shade})


@login_required
def rainbow(request):
    colors = {}
    for color in Shade.COLORS:
        temp_colors = Shade.objects.filter(color=color[0]).all().order_by('darkness')
        colors[color[1]] = temp_colors

    return render(request, 'rul/rainbow.html', {'colors': colors})
