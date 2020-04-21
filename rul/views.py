import re

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_registration.forms import User

from .models import Shade, Palette, UserShade


def index(request):
    return render(request, 'rul/index.html', {})


@login_required
def random_selector(request):
    shades_id = user_shades(request.user.pk)
    shades = Shade.objects.filter(id__in=shades_id).select_related('palette__seller').all().order_by('?')[:4]
    if len(shades) >= 4:
        context = {'shades_list': shades}
    else:
        context = {"error": 1}
    return render(request, 'rul/random.html', context)


@login_required
def insta_glam_selector(request):
    shades_id = user_shades(request.user.pk)
    crease = Shade.objects.select_related('palette__seller').filter(
        texture='M', darkness=3, id__in=shades_id).all().order_by('?')[:1]

    inner = Shade.objects.select_related('palette__seller').filter(
        id__in=shades_id).filter(
        Q(texture='Sh') | Q(texture='Sp') | Q(texture='G') | Q(darkness__gt=3)).all().order_by('?')[:1]

    outer_v = Shade.objects.select_related('palette__seller').filter(
        id__in=shades_id, darkness__lt=3).all().order_by('?')[:1]

    blending = Shade.objects.select_related('palette__seller').filter(
        id__in=shades_id, darkness__gt=3).all().order_by('?')[:1]

    try:
        context = {"shades_list": [crease[0], inner[0], outer_v[0], blending[0]]}
    except IndexError:
        context = {"error": 1}
    return render(request, 'rul/insta_glam_selector.html', context)


@login_required
def rainbow(request):
    colors = {}
    shades_id = user_shades(request.user.pk)
    shades = Shade.objects.select_related('palette__seller').filter(id__in=shades_id).all()
    for color in Shade.COLORS:
        colors[color[1]] = [s for s in shades if s.color == color[0]]

    return render(request, 'rul/rainbow.html', {'colors': colors})


@login_required
def user_shade(request):
    user = User.objects.get(id=request.user.pk)
    shades = Shade.objects.select_related('palette__seller').order_by('number').all()
    shades_ids = [s.id for s in shades]
    if request.method == 'POST':
        # in assumption than name of input is id of shade
        UserShade.objects.filter(user_id=user.id).delete()
        for key, value in request.POST.items():
            if value == 'on':
                _, s_id = re.split(r's', key)
                key = int(s_id)
                if key in shades_ids:
                    shade = Shade.objects.get(id=key)
                    pair = UserShade(user=user, shade=shade)
                    pair.save()
        return HttpResponseRedirect('rainbow')
    # if a GET (or any other method) we'll create a blank form
    else:
        u_shades = user_shades(request.user.pk)
        palettes = Palette.objects.select_related('seller').all()
        return render(request, 'rul/user_shade.html',
                      {
                          'palettes': palettes,
                          'shades': shades,
                          'user_shades': u_shades})


# technical function
def user_shades(user_id):
    user_shades = UserShade.objects.select_related('shade__palette__seller').filter(user_id=user_id).all()
    return [s.shade.id for s in user_shades]
