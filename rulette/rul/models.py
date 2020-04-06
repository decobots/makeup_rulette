from django.db import models


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


class Shade(models.Model):
    COLORS = [('R', 'Red'),
              ('O', 'Orange'),
              ('Y', 'Yellow'),
              ('G', 'Green'),
              ('B', 'Blue'),
              ('C', 'Cyan'),
              ('V', 'Violet'),
              ('B', 'Black'),
              ('Br', 'Brown'),
              ('W', 'White'),
              ('S', 'Silver'),
              ('Go', 'Gold'), ]
    TEXTURES = [('M', 'Matte'),
                ('Sh', 'Shimmer'),
                ('Sp', 'Sparkle'),
                ('G', 'Glitter'),
                ('T', 'Topper'),
                ('F', 'Foil'),
                ]
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=COLORS)
    texture = models.CharField(max_length=200, choices=TEXTURES)
    photo = models.ImageField(blank=True, upload_to='shades')

    def __str__(self):
        return f'{self.name} - {self.color}:{self.texture}.'
