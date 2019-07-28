# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json
import os

from scrapy.conf import settings


class DoubanPipeline(object):
    def open_spider(self, spider):
        file_path = settings.get("FILE_PATH")
        self.file = open(file_path, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(item["json"]+"\n")
        print(item["json"])
        return item

    def close_spider(self, spider):
        try:
            self.file.flush()
        except Exception as e:
            print(e)
