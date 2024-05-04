from code.search_code import searchdata
from code.tests import testingtools
import pytest


def page_ranks():
    return [('http://people.scs.carleton.ca/~davidmckenney/fruits/N-491.html', 0.0006846574381268377),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-688.html', 0.0003924681569743304),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-228.html', 0.0011616229013485305),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-573.html', 0.0006311343629434316),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html', 0.0004062860028498095),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html', 0.00036729490832166744),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html', 0.0011909855842089775),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html', 0.0017967720969154753),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html', 0.0018231659536325636),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html', 0.0009050389132269149),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html', 0.0003686572604238432),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html', 0.00037522635102962105),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html', 0.0008944126975590715),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html', 0.001584211027949492),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 0.0006299080616626142),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 0.001172240900170708),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html', 0.0006887034328591783),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html', 0.0006423402317285988),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-987.html', 0.0004253709096453197),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html', 0.0003825605461173355),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-684.html', 0.0004134707781453321),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-967.html', 0.00039898919206508637),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html', 0.0019852203199706964),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 0.0014532933976395298),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html', 0.001472432411256313),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html', 0.0018146288291091884),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html', 0.0006412670165577172),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html', 0.0007952447178212694),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html', 0.0015598805959350262),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html', 0.0006568941019237634),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html', 0.0009591044786276534),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-968.html', 0.0006740512236715427),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html', 0.0009119469775946435),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html', 0.0007034995744286002),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html', 0.0006139497257560401),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html', 0.0006597432792956402),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html', 0.0003556173546590424),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html', 0.0018444373319700977),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html', 0.0014798151902330025),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-814.html', 0.000644553286496165),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html', 0.0009703191274896862),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-235.html', 0.0003644259449494321),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html', 0.0006853515189090121),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html', 0.00035862732370814203),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html', 0.0009286633484794791),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-999.html', 0.000659199588528232),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html', 0.0009123807647675068),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-651.html', 0.00039209013850986134),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html', 0.0006319347204956278),
            ('http://people.scs.carleton.ca/~davidmckenney/fruits/N-751.html', 0.0003927092902694676),
            ('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html', -1.0)
            ]


@pytest.mark.parametrize('url, expected', page_ranks())
def test_page_rank(run_crawler, url, expected):
    result = searchdata.get_page_rank(url)
    assert testingtools.compare_doubles(result, expected)
