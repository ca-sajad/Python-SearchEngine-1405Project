from code.search_code import searchdata
from code.tests import testingtools
import pytest


def expected_idf():
    return [('peach', 0.05439229681862769),
            ('pear', 0.06039727964395631),
            ('apple', 0.06039727964395631),
            ('banana', 0.066427361738976),
            ('coconut', 0.05889368905356862),
            ('tomato', 0.0)
            ]


@pytest.mark.parametrize('fruit, expected', expected_idf())
def test_idf(run_crawler, fruit, expected):
    result = searchdata.get_idf(fruit)
    assert testingtools.compare_doubles(result, expected)
