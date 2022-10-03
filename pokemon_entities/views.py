import folium

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    current_time = localtime()
    pokemon_entities = PokemonEntity.objects.filter(
        appered_at__lte=current_time,
        disappered_at__gte=current_time
    )
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(f"media/{pokemon_entity.pokemon.image}")
            )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(f"media/{pokemon.image}"),
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if requested_pokemon.previous_evo:
        previous_evolution = {
            'pokemon_id': requested_pokemon.previous_evo.id,
            'title_ru': requested_pokemon.previous_evo.title_ru,
            'img_url': requested_pokemon.previous_evo.image.url,
        }
    else:
        previous_evolution = None

    next_evo = requested_pokemon.next_evos.all().first()
    if next_evo:
        next_evolution = {
            'pokemon_id': next_evo.id,
            'title_ru': next_evo.title_ru,
            'img_url': next_evo.image.url,
        }
    else:
        next_evolution = None

    pokemon = {
        "title_ru": requested_pokemon.title_ru,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "description": requested_pokemon.description,
        "img_url": requested_pokemon.image.url,
        "previous_evolution": previous_evolution,
        "next_evolution": next_evolution
    }

    current_time = localtime()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(
        pokemon=requested_pokemon,
        appered_at__lte=current_time,
        disappered_at__gte=current_time
    )
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            f"media/{requested_pokemon.image}"
        )
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
