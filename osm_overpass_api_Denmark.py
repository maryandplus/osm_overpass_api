import requests
import json
import time
import os

#specify api
overpass_url = "http://overpass-api.de/api/interpreter"

#use time out
def offline():
    time.sleep(10)

#try downloading specific data for Denmark    
try:


    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["shop"](area.searchArea););
    out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_shops = response.json()
    print('data_shops',data_shops)

    
    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="bar"](area.searchArea););
    out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_bars = response.json()
    print('data_bars',data_bars)

    
    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="cafe"](area.searchArea););
    out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_cafes = response.json()
    print('data_cafes',data_cafes)
    
    
    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="restaurant"](area.searchArea););
    out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_restaurants = response.json()
    print('data_restaurants',data_restaurants)

    
    offline()


    
    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="pub"](area.searchArea);
    );out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_pubs = response.json()
    print('data_pubs',data_pubs)

    
    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="bank"](area.searchArea);
    );out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_banks = response.json()
    print('data_banks',data_banks)

    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="pharmacy"](area.searchArea);
    );out center;"""
    response = requests.get(overpass_url,
                            params={'data': overpass_query})
    data_pharmacies = response.json()
    print('data_pharmacies',data_pharmacies)
    
    
    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="cinema"](area.searchArea);
    );out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_cinemas = response.json()
    print('data_cinemas',data_cinemas)
    
    
    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="nightclub"](area.searchArea);
    );out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_nightclubs = response.json()
    print('data_nightclubs',data_nightclubs)
    
    
    offline()

    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["amenity"="theatre"](area.searchArea);
    );out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_theatres = response.json()
    print('data_theatres',data_theatres)
    
    
    offline()
    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["place"="square"](area.searchArea););out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_squares = response.json()
    print('data_squares',data_squares)
    
    
    offline()
    
    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["leisure"="park"](area.searchArea););out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_parks = response.json()
    print('data_parks',data_parks)
    
    
    offline()
    
    overpass_query = """[out:json];area["ISO3166-1"="DK"][admin_level=2]->.searchArea;(node["railway"="station"](area.searchArea););out center;"""
    response = requests.get(overpass_url,params={'data': overpass_query})
    data_stations = response.json()
    print('data_stations',data_stations)
    
    

except:
    print('Error downloading', overpass_query)

    
#if no error occured then create a geojson    
else:
    #create a list of downloaded data 
    dataset= [data_shops, data_bars, data_cafes, data_restaurants, data_pubs, data_banks, data_pharmacies, data_cinemas, data_nightclubs,data_theatres,data_squares,data_parks,data_stations]
    
    geojson = {}
    geojson["type"] = "FeatureCollection"
    geojson["features"] = []

    for i in range(len(dataset)):
    

        for j in range(len(dataset[i]['elements'])):

            feature = {}
            feature["type"] = "Feature"
            feature["geometry"] = {}
            feature["geometry"]["type"] = "Point"
            feature["geometry"]["coordinates"] =dataset[i]['elements'][j]['lon'],dataset[i]['elements'][j]['lat']
            feature["properties"] = {}
            feature["properties"]["ID"] = dataset[i]['elements'][j]['id']

            #check tags 
    
            if 'amenity' in dataset[i]['elements'][j]['tags']:
                feature["properties"]["type"] = dataset[i]['elements'][j]['tags']['amenity']
   
            elif 'place' in dataset[i]['elements'][j]['tags']:
                feature["properties"]["type"] = dataset[i]['elements'][j]['tags']['place']
            
            elif 'leisure' in dataset[i]['elements'][j]['tags']:
                feature["properties"]["type"] = dataset[i]['elements'][j]['tags']['leisure']
                
            elif 'railway' in dataset[i]['elements'][j]['tags']:
                feature["properties"]["type"] = dataset[i]['elements'][j]['tags']['railway']
                
            else:
                feature["properties"]["type"] = dataset[i]['elements'][j]['tags']['shop']
            


            geojson["features"].append(feature)

    #specify directory for saving geojson
    with open(os.path.join(r'C:\Users\xxxxXXXXxxxx','osm_denmark_landuse.geojson'), 'w') as fp:
        json.dump(geojson, fp)
