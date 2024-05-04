import pytest
from code.search_code import searchdata


def incoming_links_results():
    expected = []
    links = []

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-509.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-68.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-662.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-505.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-768.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-769.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-923.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-238.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-590.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-942.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-747.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-222.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-334.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-854.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-288.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-391.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-945.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-981.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-623.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-55.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-384.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-738.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-425.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-515.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-988.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-783.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-497.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-349.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-272.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-454.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-813.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-310.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-883.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-714.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-933.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-608.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-560.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-425.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-943.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-436.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-660.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-193.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-130.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-439.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-123.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-382.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-160.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-200.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-24.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-137.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-969.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html')

    expected.append(None)
    links.append('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')

    return zip(links, expected)


@pytest.mark.parametrize('url, expected', incoming_links_results())
def test_incoming_links(run_crawler, url, expected):
    result = searchdata.get_incoming_links(url)
    if expected is None:
        assert result is None
    else:
        assert set(expected) == set(result)
