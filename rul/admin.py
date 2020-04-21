from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from image_cropping import ImageCroppingMixin

from .models import Palette, Shade, Seller, UserShade


class ShadeInline(ImageCroppingMixin, admin.TabularInline):
    model = Shade
    extra = 3


class PaletteAdmin(ModelAdmin):

    def image_tag(self, obj):
        try:
            result = format_html('<img src="{}" height="100px" />'.format(obj.photo.url))
        except ValueError:
            result = ''
        return result

    image_tag.short_description = 'Image'

    list_display = ['name', 'image_tag', ]
    readonly_fields = ['image_tag']
    inlines = [ShadeInline]


class ShadeAdmin(ImageCroppingMixin, ModelAdmin):

    def crop(self, obj):
        return format_html('<img src="{}" height="40px" />'.format(obj.crop()))

    list_display = ['name', 'crop']


admin.site.register(Seller)
admin.site.register(Palette, PaletteAdmin)
admin.site.register(Shade, ShadeAdmin)
admin.site.register(UserShade)
