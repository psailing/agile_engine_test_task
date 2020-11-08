from functions import get_oldest_building


def test_oldest_building():
    assert get_oldest_building() == 'Empire State Building', 'Incorrect name of oldest building'
