from code import searchdata
from tests import testingtools
import pytest


def page_ranks():
    return [('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 0.0819555328928385),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 0.11896585666418055),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 0.047437705789256435),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 0.11939323868209492),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 0.04626363024816037),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 0.04626363024816037),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 0.32242792521306995),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 0.12476521976591842),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 0.04626363024816037),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 0.04626363024816037),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html', -1.0)
            ]


@pytest.mark.parametrize('url, expected', page_ranks())
def test_page_rank(run_crawler, url, expected):
    result = searchdata.get_page_rank(url)
    assert testingtools.compare_doubles(result, expected)
