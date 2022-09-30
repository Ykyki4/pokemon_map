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

    appered_at = models.DateTimeField(null=True, blank=True)
    disappered_at = models.DateTimeField(null=True, blank=True)

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
        ],
        null=True,
        blank=True
    )

    strength = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(350)
        ],
        null=True,
        blank=True
    )

    defence = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(250)
        ],
        null=True,
        blank=True
    )

    stamina = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300)
        ],
        null=True,
        blank=True
    )
