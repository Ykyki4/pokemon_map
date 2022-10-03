from django.db import models  # noqa F401
from django.core.validators import MaxValueValidator, MinValueValidator

class Pokemon(models.Model):
    title_ru = models.CharField(verbose_name='Имя на русском', max_length=50)
    title_en = models.CharField(verbose_name='Имя на английском', max_length=50, blank=True)
    title_jp = models.CharField(verbose_name='Имя на японском', max_length=50, blank=True)
    description = models.TextField(verbose_name='Описание покемона', blank=True)
    image = models.ImageField(verbose_name='Изображение покемона', upload_to='images/')

    previous_evo = models.ForeignKey(
        "self",
        verbose_name='Предыдущая эволюция покемона',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="next_evos"
    )
    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        on_delete=models.CASCADE,
        related_name="pokemon"
    )

    lat = models.FloatField(
        verbose_name='Широта',
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(90.0)
        ]
    )

    lon = models.FloatField(
        verbose_name='Долгота',
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(180.0)
        ]
    )

    appered_at = models.DateTimeField(verbose_name='Время появления', null=True, blank=True)
    disappered_at = models.DateTimeField(verbose_name='Время исчезновения', null=True, blank=True)

    level = models.IntegerField(
        verbose_name='Уровень покемона',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    health = models.IntegerField(
        verbose_name='Очки жизни покемона',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(500)
        ],
        null=True,
        blank=True
    )

    strength = models.IntegerField(
        verbose_name='Очки силы покемона',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(350)
        ],
        null=True,
        blank=True
    )

    defence = models.IntegerField(
        verbose_name='Очки защиты покемона',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(250)
        ],
        null=True,
        blank=True
    )

    stamina = models.IntegerField(
        verbose_name='Очки выносливости покемона',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300)
        ],
        null=True,
        blank=True
    )
