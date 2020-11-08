from functions import get_most_common


def test_country_with_most_count_of_towers():
    assert get_most_common(4) == 'China', 'Most buildings are located in China'
