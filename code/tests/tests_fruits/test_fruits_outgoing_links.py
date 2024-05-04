from code.search_code import searchdata
import pytest


def outgoing_links_results():
    expected = []
    links = []

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-145.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-933.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-221.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-2.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-154.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-707.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-663.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-763.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-246.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-407.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-661.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-984.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-836.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-824.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-764.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-295.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-251.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-817.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-643.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-422.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-992.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-401.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-746.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-562.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-458.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-403.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-598.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-455.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-272.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-324.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-477.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-655.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-907.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-205.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-753.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-407.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-974.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-605.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-349.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-832.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-850.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-884.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-115.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html')

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

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-25.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-202.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-216.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-635.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-881.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-89.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-900.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-455.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-403.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-789.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-983.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-292.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-560.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-999.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-290.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-595.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-213.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-429.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-330.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-278.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-865.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-617.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-659.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-883.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-189.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-409.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-538.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-741.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-135.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-865.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-957.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-202.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-842.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-209.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html',
                     'http://people.scs.carleton.ca/~davidmckenney/fruits/N-817.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html')

    expected.append(['http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html'])
    links.append('http://people.scs.carleton.ca/~davidmckenney/fruits/N-156.html')

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
