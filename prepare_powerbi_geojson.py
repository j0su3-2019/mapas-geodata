import json

input_path = 'deptos_coloreado_style.geojson'
output_path = 'deptos_powerbi.geojson'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

features = []
for feature in data.get('features', []):
    props = feature.get('properties', {})
    cleaned_props = {
        'shapeName': props.get('shapeName'),
        'shapeGroup': props.get('shapeGroup', 'GTM'),
        'shapeType': 'Merged Region',
        'region': props.get('region_custom', props.get('region', '')),
        'fill': props.get('region_color', props.get('fill', '#CCCCCC')),
    }

    geometry = feature.get('geometry', {})
    features.append({
        'type': 'Feature',
        'properties': cleaned_props,
        'geometry': geometry,
    })

output = {
    'type': 'FeatureCollection',
    'features': features,
}

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Features procesados: {len(features)}')
print(f'Archivo generado: {output_path}')
