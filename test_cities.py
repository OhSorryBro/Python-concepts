from city_functions import function

def test_city_country():
    """Do funtion deliver proper result for test scenario "NY, USA" """
    formatted_name = function('NY', 'USA')
    assert formatted_name == "NY, USA"

def test_city_country_population():
    """Do funtion deliver proper result for test scenario "NY, USA - population 100" """
    formatted_name = function("NY", "USA", "100")
    assert formatted_name == "NY, USA - population 100"