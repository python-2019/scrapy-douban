import simplejson as json

from douban.items import DoubanItem

if __name__ == '__main__':
    item = DoubanItem()
    item['url'] = "aaa"
    dumps = json.dumps(item)
    print(dumps)