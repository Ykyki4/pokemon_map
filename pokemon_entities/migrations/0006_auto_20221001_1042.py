# Generated by Django 3.2.15 on 2022-10-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20220930_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='title_ru',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]