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

except:
    print('Error downloading', overpass_query)

    
#if no error occured then create a geojson    
else:
    #create a list of downloaded data 
    dataset= [data_shops, data_bars, data_cafes, data_restaurants, data_pubs, data_banks, data_pharmacies, data_cinemas, data_nightclubs,data_theatres]
    
    geojson = {}
    geojson["type"] = "FeatureCollection"
    geojson["features"] = []

    for i in range(len(dataset)):
    

        for j in range(len(dataset[i]['elements'])):

            feature = {}
            feature["geometry"] = {}
            feature["geometry"]["type"] = "Point"
            feature["geometry"]["coordinates"] =dataset[i]['elements'][j]['lon'],dataset[i]['elements'][j]['lat']
            feature["properties"] = {}
            feature["properties"]["ID"] = dataset[i]['elements'][j]['id']

            #check if shop or amenity tag 
            if 'amenity' in dataset[i]['elements'][j]['tags']:
                feature["properties"]["type"] = dataset[i]['elements'][j]['tags']['amenity']
   
            else:
                feature["properties"]["type"] = dataset[i]['elements'][j]['tags']['shop']
            

            if 'name' in dataset[i]['elements'][j]['tags']:

                feature["properties"]["name"] = dataset[i]['elements'][j]['tags']['name']
  
            else:
                feature["properties"]["name"] = 'No_Name'

            geojson["features"].append(feature)

    #specify directory for saving geojson
    with open(os.path.join(r'C:\Users\xxxxXXXXxxxx','osm_denmark_retail.geojson'), 'w') as fp:
        json.dump(geojson, fp)
