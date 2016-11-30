
import json
filename = "countries.json"
# --------------- load by Json --------------------
myfile = open(filename, mode='r', encoding='latin-1')
countries = json.load(myfile)

schengen_countries = set()
sea_countries = set()
	
for country_name, properties in countries.items():
	if properties['schengen']:
		schengen_countries.add(country_name)
	if properties['sea']:
		sea_countries.add(country_name)
		
		
print (sea_countries)
print (schengen_countries)



sea_schengen_countries = schengen_countries & sea_countries

for country_name in sea_schengen_countries:
	print(country_name, countries[country_name])


