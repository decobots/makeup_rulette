from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_registration.forms import User

from .forms import get_user_palette_form
from .models import Shade, Palette, UserPalette


def index(request):
    return render(request, 'rul/index.html', {})


@login_required
def random_selector(request):
    shades = Shade.objects.select_related('palette__seller').all().order_by('?')[:4]
    context = {'shades_list': shades}
    return render(request, 'rul/random.html', context)


@login_required
def insta_glam_selector(request):
    crease = Shade.objects.select_related('palette__seller').filter(texture='M', darkness=3).all().order_by('?')[:1]
    inner = Shade.objects.select_related('palette__seller').filter(
        Q(texture='Sh') | Q(texture='Sp') | Q(texture='G') | Q(darkness__gt=3)).all().order_by('?')[:1]
    outer_v = Shade.objects.select_related('palette__seller').filter(darkness__lt=3).all().order_by('?')[:1]
    blending = Shade.objects.select_related('palette__seller').filter(darkness__gt=3).all().order_by('?')[:1]
    context = {"shades_list": [crease[0], inner[0], outer_v[0], blending[0]]}
    return render(request, 'rul/insta_glam_selector.html', context)


@login_required
def shade_detail(request, shade_id):
    shade = Shade.objects.get(pk=shade_id)
    return render(request, 'rul/shade_details.html', {'shade': shade})


@login_required
def rainbow(request):
    colors = {}
    user_palettes = UserPalette.objects.select_related('palette__seller').filter(user_id=request.user.pk).all()
    palettes_id = [p.palette.id for p in user_palettes]
    shades = Shade.objects.select_related('palette__seller').filter(palette_id__in=palettes_id).all()
    for color in Shade.COLORS:
        #
        # temp_colors = Shade.objects.filter(color=color[0]).all().order_by('darkness')
        colors[color[1]] = [s for s in shades if s.color == color[0]]

    return render(request, 'rul/rainbow.html', {'colors': colors})


@login_required
def user_palette(request):
    user = User.objects.get(id=request.user.pk)
    mather_form = get_user_palette_form(user_id=user.id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = mather_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            selected = request.POST.getlist('palettes')

            UserPalette.objects.filter(user_id=user.id).delete()
            for palette_id in selected:
                palette = Palette.objects.get(id=palette_id)
                pair = UserPalette(user=user, palette=palette)
                pair.save()

            return HttpResponseRedirect('user_palette_saved')
        else:
            return HttpResponseRedirect('user_palette')
    # if a GET (or any other method) we'll create a blank form
    else:

        form = mather_form()
        return render(request, 'rul/user_palette.html', {'form': form})


@login_required
def user_palette_saved(request):
    palettes = UserPalette.objects.filter(user_id=request.user.pk).select_related("palette")
    return render(request, 'rul/user_palette_saved.html', {'palettes': palettes})
