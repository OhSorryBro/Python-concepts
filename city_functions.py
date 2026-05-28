def function(city_name, country_name, population ='Unknown'):
    if population != 'Unknown':
        city_data = (f"{city_name}, {country_name} - population {population}")
    else:
        city_data = (f"{city_name}, {country_name}")
    return city_data