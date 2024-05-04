from tests import testingtools
from code import searchdata
import pytest


def expected_tfidf():
    return [('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'peach', 0.03622045978643087),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'cherry', 0.10375537569198201),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'coconut', 0.02266030222847964),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'fig', 0.14859721830091777),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'papaya', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'blueberry', 0.02997453317184664),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'apricot', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'banana', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'kiwi', 0.02997453317184664),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'orange', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'tomato', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'peach', 0.07620758655640758),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'cherry', 0.05787647829766945),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'coconut', 0.02445006963027565),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'fig', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'papaya', 0.03908124238104001),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'blueberry', 0.054703631988055924),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'apricot', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'banana', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'kiwi', 0.02815674585715757),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'orange', 0.10363769827780657),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'tomato', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'peach', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'cherry', 0.1656555612092295),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'coconut', 0.014291714269269087),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'fig', 0.06445710476952095),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'papaya', 0.045006031726892604),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'blueberry', 0.054703631988055924),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'apricot', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'banana', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'kiwi', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'orange', 0.11672149491947882),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'tomato', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'coconut', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'fig', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'papaya', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'blueberry', 0.10363769827780657),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'apricot', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'peach', 0.045006031726892604),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'cherry', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'coconut', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'fig', 0.18271404725510207),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'papaya', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'blueberry', 0.019766560368774045),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'apricot', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'banana', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'kiwi', 0.03872609348667805),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'orange', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'tomato', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'peach', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'cherry', 0.06459482428200948),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'coconut', 0.0404119177187868),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'fig', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'papaya', 0.12401630243933787),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html', 'blueberry', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html', 'apricot', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html', 'banana', 0.0),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html', 'kiwi', 0.0)
            ]


@pytest.mark.parametrize('url, fruit, expected', expected_tfidf())
def test_tfidf(run_crawler, url, fruit, expected):
    result = searchdata.get_tf_idf(url, fruit)
    assert testingtools.compare_doubles(result, expected)
