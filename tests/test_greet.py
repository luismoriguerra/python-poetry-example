from greet.location import greet

def test_greet():
    result = greet()
    assert "New York!" in result