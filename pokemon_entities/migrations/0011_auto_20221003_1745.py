# Generated by Django 2.2.24 on 2022-10-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20221003_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
    ]
