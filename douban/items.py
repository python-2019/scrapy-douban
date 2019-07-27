# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    """
        [
    {
        "rating": [
            "9.7",
            "50"
        ],
        "rank": 1,
        "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg",
        "is_playable": true,
        "id": "1292052",
        "types": [
            "犯罪",
            "剧情"
        ],
        "regions": [
            "美国"
        ],
        "title": "肖申克的救赎",
        "url": "https://movie.douban.com/subject/1292052/",
        "release_date": "1994-09-10",
        "actor_count": 25,
        "vote_count": 1507927,
        "score": "9.7",
        "actors": [
            "蒂姆·罗宾斯",
            "摩根·弗里曼"
        ],
        "is_watched": false
    }
]

    """
    # rating = scrapy.Field()
    # rank = scrapy.Field()
    # cover_url = scrapy.Field()
    # is_playable = scrapy.Field()
    # id = scrapy.Field()
    # types = scrapy.Field()
    # regions = scrapy.Field()
    # title = scrapy.Field()
    # url = scrapy.Field()
    # release_date = scrapy.Field()
    # actor_count = scrapy.Field()
    # vote_count = scrapy.Field()
    # score = scrapy.Field()
    # actors = scrapy.Field()
    # is_watched = scrapy.Field()
    json = scrapy.Field()
