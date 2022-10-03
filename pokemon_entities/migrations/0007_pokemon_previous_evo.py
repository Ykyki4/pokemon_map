# Generated by Django 3.2.15 on 2022-10-01 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20221001_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evo', to='pokemon_entities.pokemon'),
        ),
    ]