from meball.lib import get_response,print_response, RESPONSES

def test_get_response():
    assert type(get_response()) == str
    
def test_print_response():
    assert print_response() is None
    
def test_responses():
    assert len(RESPONSES['msgs']) == 20