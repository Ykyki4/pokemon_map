from django.db import models  # noqa F401
from django.core.validators import MaxValueValidator, MinValueValidator

class Pokemon(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(100.0)])
    lon = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(100.0)])
