
import json
filename = "countries.txt"
myfile = open(filename, mode='w' , encoding='latin-1')

countries = {
	#'Cuba': data_about_Cuba,
	'Thailand': {'sea': True, 
				'schengen': False, 
				'average_temperature': 30, 
				'currency_rate': 1.8},
	'Hungary': {'sea': False, 
				'schengen': True, 
				'average_temperature': 10, 
				'currency_rate': 0.3},
	'Germany': {'sea': True, 
				'schengen': True, 
				'average_temperature': 5, 
				'currency_rate': 80},
	'Japan': {'sea': True, 
				'schengen': False, 
				'average_temperature': 15, 
				'currency_rate': 0.61},
	}
	
# ---------------Save in JSON----------------------

json.dump(countries, myfile)
myfile.close


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


