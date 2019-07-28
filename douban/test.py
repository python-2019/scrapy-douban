import simplejson as json

from douban.items import DoubanItem


def m1():
    item = DoubanItem()
    item['url'] = "aaa"
    dumps = json.dumps(item)
    print(dumps)


def next_url(url, max):
    if url is None or url == "":
        return None
    start = int(url[url.find("start=") + 6:url.find("&limit")])
    limit = int(url[url.find("&limit") + 7:len(url)])
    if start < max:
        next_url = url.replace("start=" + str(start), "start=" + str(start + 20)).replace("&limit=" + str(limit),
                                                                                          "&limit=" + str(limit + 20))
        print(next_url)
        return next_url
    return None


if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list?type_name=剧情&type=11&interval_id=100:90&action=&start=0&limit=20"
    for i in range(10):
        url = next_url(url, 100)
