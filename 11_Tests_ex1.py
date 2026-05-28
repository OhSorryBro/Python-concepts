# 11.1. City, Country. 
# Write a function that accepts two parameters: a city name and a country name. 
# The function should return a single string in the format City, Country, for example Santiago, Chile. Place the finished function in a module called city_functions.py. 
# Save this file in a new directory so that pytest doesn't try to run the tests defined in the earlier part of the chapter.
# Create a file called test_cities.py designed to test the function you just wrote. 
# In test_cities.py, define a function called test_city_country() responsible for checking whether calling the function created in the previous exercise — for example with the values 'santiago' and 'chile' — produces the expected string.
#  Run test_cities.py and make sure the test_city_country() test passes.




# 11.2. Population. 
# Modify the function you wrote earlier so that it requires a third argument — the population (population). 
# The function should now return a string in the format City, Country - population xxx, for example Santiago, Chile - population 5000000. Run the tests again. 
# Make sure that this time the test defined in test_city_country() fails.
# Modify the function so that the population parameter is optional. Run the tests again and make sure that now the test defined in test_city_country() passes as well.
# Create a second test called test_city_country_population() that checks whether the function can be called with the values 'santiago', 'chile', and 'population=5000000'. 
# Run the tests once more and make sure the new test passes.



