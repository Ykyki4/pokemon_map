from django.db import models  # noqa F401
from django.core.validators import MaxValueValidator, MinValueValidator

class Pokemon(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE
    )

    lat = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0)
        ]
    )

    lon = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0)
        ]
    )

    appered_at = models.DateTimeField()
    disappered_at = models.DateTimeField()

    level = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    health = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(500)
        ]
    )

    strength = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(350)
        ]
    )

    defence = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(250)
        ]
    )

    stamina = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300)
        ]
    )
