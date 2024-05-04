from code import searchdata
from tests import testingtools
import pytest


def expected_idf():
    return [('orange', 0.32192809488736235),
            ('coconut', 0.32192809488736235),
            ('peach', 0.5145731728297582),
            ('blueberry', 0.32192809488736235),
            ('papaya', 0.5145731728297582),
            ('kiwi', 0.32192809488736235),
            ('banana', 0.0),
            ('fig', 0.7369655941662062),
            ('apricot', 0.0),
            ('apple', 0.32192809488736235),
            ('cherry', 0.5145731728297582),
            ('lime', 0.32192809488736235),
            ('pear', 0.7369655941662062),
            ('tomato', 0.0)
            ]


@pytest.mark.parametrize('fruit, expected', expected_idf())
def test_idf(run_crawler, fruit, expected):
    result = searchdata.get_idf(fruit)
    assert testingtools.compare_doubles(result, expected)
