import pytest
import sample_backend

def test_find_users_by_name_success():  
    expected = [           
        {
           '_id' : '6009dfa508f2eca30c87d56c',            
            'name': 'Macc',
            'job': 'Professor',
        },   
        {
            '_id' : '61817557d1b11d226de426dd',            
            'name': 'Mac',
            'job': 'Bartender',
        },
    ]
    
    assert sample_backend.User().find_by_name("Mac") == expected

def test_find_by_name_fail():  
    expected = []
    assert sample_backend.User().find_by_name("Jeff") == expected
