# Generated by Django 2.2.24 on 2022-10-05 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20221003_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemons', to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
    ]
