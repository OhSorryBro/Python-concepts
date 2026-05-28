from name_function import get_formatted_name

def test_first_last_name():
    """Do data for name 'Janis Joplin' are well handled?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name =='Janis Joplin'


def test_first_last_middle_name():
    """Do data for 'Wolfgang Amadeus Mozart' are handled properly?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == "Wolfgang Amadeus Mozart"