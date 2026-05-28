from name_function import get_formatted_name

def test_first_last_name():
    """Do data for name 'Janis Joplin' are well handled?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name =='Janis Joplin'