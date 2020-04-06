from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from .models import Palette, Shade, Seller


class PaletteAdmin(ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" height="100px" />'.format(obj.photo.url))

    image_tag.short_description = 'Image'

    list_display = ['name', 'image_tag', ]
    readonly_fields = ['image_tag']


admin.site.register(Seller)
admin.site.register(Palette, PaletteAdmin)
admin.site.register(Shade)
