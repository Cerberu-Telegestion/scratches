import requests

# URL de la API de Strapi
STRAPI_URL = 'https://mighty-frogs-714884b697.strapiapp.com/api/'
STRAPI_URL_ZONES = STRAPI_URL + 'long-stays-zones'
TOKEN = '314a31883a08474cbccde0846259dab31631d80f49c7029d6aafb14470ef5bacb9924c0a82eb468cfd46c45b1b3b0eba796d860f54175c642c79cdae812d3d1a1d452d5bc2af7ce6b64123d414ca75dc4bd5fac2b7abf6c45097446918367f52f5012494fbdbb0ca19596d1b075234c0cd39f162452d69e1136a6b44886291b2'

def get_all_zones(url, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    all_zones = []
    page = 1
    while True:
        response = requests.get(f'{url}?pagination[page]={page}&pagination[pageSize]=100', headers=headers)
        if response.status_code != 200:
            print(f'Error en la solicitud: {response.status_code} - {response.text}')
            return None
        try:
            data = response.json()
            if not data['data']:
                break
            all_zones.extend(data['data'])
            page += 1
        except json.JSONDecodeError:
            print('Error al decodificar la respuesta JSON:')
            print(response.text)
            return None
    return {'data': all_zones}

def update_zone(url, zone_id, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'data': {
            'servicedApartments': True
        }
    }
    response = requests.put(f'{url}/{zone_id}', json=data, headers=headers)
    if response.status_code != 200:
        print(f'Error en la solicitud: {response.status_code} - {response.text}')
        return None
    try:
        return response.json()
    except json.JSONDecodeError:
        print('Error al decodificar la respuesta JSON:')
        print(response.text)
        return None

# Obtener todos los elementos de long-stays-zones
zones = get_all_zones(STRAPI_URL_ZONES, TOKEN)
if zones and 'data' in zones:
    for zone in zones['data']:
        zone_id = zone['id']
        update_response = update_zone(STRAPI_URL_ZONES, zone_id, TOKEN)
        if update_response:
            print(f'Zona actualizada con éxito: ID {zone_id}')
        else:
            print(f'Error al actualizar la zona: ID {zone_id}')
else:
    print('Error al obtener las zonas')