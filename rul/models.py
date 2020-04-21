import easy_thumbnails
from django.db import models
from django_registration.forms import User
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend

from .storage import CustomStorage


class Seller(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Palette(models.Model):
    name = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='palettes')

    # seller = models.DateTimeField('date published')
    def __str__(self):
        return f'{self.name} by {self.seller}.'


custom_store = CustomStorage()


class Shade(models.Model):
    COLORS = [('P', 'Pink'),
              ('L', 'Lilac'),
              ('C', 'Corall'),
              ('R', 'Red'),
              ('O', 'Orange'),
              ('Y', 'Yellow'),
              ('G', 'Green'),
              ('B', 'Blue'),
              ('Pu', 'Purple'),
              ('Bk', 'Black'),
              ('Br', 'Brown'),
              ('Be', 'Beige'),
              ('Gr', 'Gray'),
              ('W', 'White'),
              ('S', 'Silver'),
              ('Co', 'Cooper'),
              ('Go', 'Gold'), ]
    TEXTURES = [('M', 'Matte'),
                ('Sh', 'Shimmer'),
                ('Sp', 'Sparkle'),
                ('G', 'Glitter'),
                ('T', 'Topper'),
                ('F', 'Foil'),
                ]
    DARKNES = [('1', 'Blackl'),
               ('2', 'dark'),
               ('3', 'medium'),
               ('4', 'light'),
               ('5', 'white'),
               ]
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    color = models.CharField(max_length=200, choices=COLORS)
    second_color = models.CharField(blank=True, max_length=200, choices=COLORS)
    darkness = models.CharField(max_length=200, choices=DARKNES)
    texture = models.CharField(max_length=200, choices=TEXTURES)
    photo = models.ImageField(blank=True, storage=custom_store, upload_to='shades')
    cropping = ImageRatioField('photo', '40x40')

    def __str__(self):
        return f'{self.palette.name} - {self.name}.'

    def crop(self):
        try:
            thumbnail_url = get_backend().get_thumbnail_url(
                self.photo,
                {
                    'size': (430, 360),
                    'box': self.cropping,
                    'crop': True,
                    'detail': True,
                }
            )
        except easy_thumbnails.exceptions.InvalidImageFormatError:
            thumbnail_url = ''
        return thumbnail_url


class UserShade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shade = models.ForeignKey(Shade, on_delete=models.CASCADE)


class PaletteRequest(models.Model):
    name = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    photo_URL = models.CharField(max_length=600, blank=True)
    number_of_colors = models.IntegerField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    processed = models.BooleanField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.seller}.'
