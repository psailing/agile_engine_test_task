import pytest

from functions import is_column_sorted


@pytest.mark.parametrize('column, reverse', [
    (0, False),
    (5, True),
    (6, True)
])
def test_column_sorting(column, reverse):
    assert is_column_sorted(column, reverse), 'Incorrect sorting order'
