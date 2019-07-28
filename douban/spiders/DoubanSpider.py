# -*- coding: utf-8 -*-

import simplejson as json

import scrapy

from douban.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    host = "https://movie.douban.com"
    allowed_domains = ['douban.com']
    start = 0
    limit = 20
    max_start = 500
    start_urls = [
        "https://movie.douban.com/j/chart/top_list?type_name=剧情&type=11&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=喜剧&type=24&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=动作&type=5&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=爱情&type=13&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=科幻&type=17&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=动画&type=25&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=悬疑&type=10&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=惊悚&type=19&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=恐怖&type=20&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=纪录片&type=1&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=短片&type=23&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=情色&type=6&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=同性&type=26&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=音乐&type=14&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=歌舞&type=7&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=家庭&type=28&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=儿童&type=8&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=传记&type=2&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=历史&type=4&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=战争&type=22&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=犯罪&type=3&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=西部&type=27&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=奇幻&type=16&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=冒险&type=15&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=灾难&type=12&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=武侠&type=29&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=古装&type=30&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=运动&type=18&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit),
        "https://movie.douban.com/j/chart/top_list?type_name=黑色电影&type=31&interval_id=100:90&action=&start=%d&limit=%d" % (start, limit)]

    # start_urls = [
    #     "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=%d&limit=%d" % (
    #     start, limit)]


    def next_url(self, url, max):
        """
        截取url得到下一条请求的url
        :param url: 请求url
        :param max: 最大
        :return: 新的url
        """
        if url is None or url == "":
            return None
        start = int(url[url.find("start=") + 6:url.find("&limit")])
        limit = int(url[url.find("&limit") + 7:len(url)])
        if start < max:
            next_url = url.replace("start=" + str(start), "start=" + str(start + 20)).replace("&limit=" + str(limit),
                                                                                              "&limit=" + str(
                                                                                                  limit + 20))
            print(next_url)
            return next_url
        return None

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url=url, method='GET', callback=self.parse, encoding='utf-8')

    def parse(self, response):
        model_dict_arr = json.loads(response.text)
        for mode_dict in model_dict_arr:
            item = DoubanItem()
            item['json'] = json.dumps(mode_dict, ensure_ascii=False)
            yield item
        # 翻页
        next_url = self.next_url(response.url, self.max_start)
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)
