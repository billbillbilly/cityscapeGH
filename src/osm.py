import argparse
import json
import os
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--work_dir', 
                    type=str, 
                    default='', 
                    help='where to save files')
parser.add_argument('--MAX_LAT', 
                    type=float, 
                    default=42.280616, 
                    help='bbox to retrieve OSM data - MAXIMUM LATITUDE')
parser.add_argument('--MIN_LAT', 
                    type=float, 
                    default=42.278965, 
                    help='bbox to retrieve OSM data - MINIMUM LATITUDE')
parser.add_argument('--MAX_LON', 
                    type=float, 
                    default=-83.742242, 
                    help='bbox to retrieve OSM data - MAXIMUM LONGITUDE')
parser.add_argument('--MIN_LON', 
                    type=float, 
                    default=-83.746062, 
                    help='bbox to retrieve OSM data - MINIMUM LONGITUDE')
args = parser.parse_args()

# set current working directory
os.chdir(args.work_dir)

bbox = f'{args.MAX_LAT},{args.MAX_LON},{args.MIN_LAT},{args.MIN_LON}'

coordinates = [
    (args.MIN_LAT, args.MIN_LON),
    (args.MAX_LAT, args.MAX_LON)
]

url = "https://overpass-api.de/api/interpreter"
query = f"""
    [bbox:{bbox}]
    [out:json]
    [timeout:9999]
    ;
    (   
        way["building"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
        relation["building"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
        way["highway"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
        relation["highway"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
        way["landuse"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
        relation["landuse"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
        way["leisure"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
        relation["leisure"~"."]({coordinates[0][0]},{coordinates[0][1]},{coordinates[1][0]},{coordinates[1][1]});
    );
    out geom;
"""

payload = "data=" + requests.utils.quote(query)

response = requests.post(url, data=payload)
result = response.json()

# Extract building polygons and information
buildings = []
for element in result.get('elements', []):
    if 'tags' in element and 'building' in element['tags']:
        building_info = {
            'geometry': element.get('geometry'),
            'estimated_height': int(element['tags'].get('building:levels'))*4.3 if element['tags'].get('building:levels') != None else 4.3,
        }
        buildings.append(building_info)

# Extract road lines and information
roads = []
for element in result.get('elements', []):
    if 'tags' in element and 'highway' in element['tags']:
        road_info = {
            'type': element['tags']['highway'],
            'geometry': element['geometry']
        }
        roads.append(road_info)

# Extract greenspace and information
# Extract other land and information
greens = []
lands = []
greenspaces = [
    "forest", "vineyard", "plant_nursery", "orchard", "greenfield", 
    "recreation_ground", "allotments", "meadow", "village_green",
    "flowerbed", "grass", "farmland", "garden", "dog_park", 
    "nature_reserve", "park", 
]
for element in result.get('elements', []):
    if 'tags' in element:
        if 'landuse' in element['tags'] or 'leisure' in element['tags']:
            tags = element['tags']['landuse'] if 'landuse' in element['tags'] else element['tags']['leisure']
            if tags in greenspaces:
                green_info = {
                    'geometry': element.get('geometry'),
                    'type': tags
                }
                greens.append(green_info)
            else:
                land_info = {
                    'geometry': element.get('geometry'),
                    'type': tags
                }
                lands.append(land_info)


# export 
with open('temp/buildings.json', 'w') as outfile:
    json.dump(buildings, outfile, indent=4)

with open('temp/roads.json', 'w') as outfile:
    json.dump(roads, outfile, indent=4)

with open('temp/greens.json', 'w') as outfile:
    json.dump(greens, outfile, indent=4)

with open('temp/lands.json', 'w') as outfile:
    json.dump(lands, outfile, indent=4)
