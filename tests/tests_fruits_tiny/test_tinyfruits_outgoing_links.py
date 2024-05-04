from code import searchdata
import pytest


def outgoing_links_results():
    expected = []
    links = []

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html',
                     'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')

    expected.append(None)
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')

    return zip(links, expected)


@pytest.mark.parametrize('url, expected', outgoing_links_results())
def test_outgoing_links(run_crawler, url, expected):
    result = searchdata.get_outgoing_links(url)
    if expected is None:
        assert result is None
    else:
        assert set(expected) == set(result)
