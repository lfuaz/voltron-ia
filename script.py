 
import json
  
# Opening JSON file
f = open('tracksgeo.json')
  
# returns JSON object as 
# a dictionary
jsonfile = json.load(f)

# print(data)

# data = json.load(data['features'])
  
# Iterating through the json
# list
# print(data['features'])
for data in jsonfile['features']:
    for coord in i['geometry']['coordinates']:
        print(coord[0])
  
# Closing file
f.close()