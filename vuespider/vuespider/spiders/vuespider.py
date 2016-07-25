#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import html2text

xpath_str = '/html/body/div[@id="main"]/div[@class="content guide with-sidebar"]/div[@class="guide-links"]/span[@style="float:right"]/a/@href'
index = 00
class VueSpider(scrapy.Spider):
    name = 'vue-spider'
    allowed_domains = ['cn.vuejs.org']
    start_urls = [
        "http://cn.vuejs.org/guide/installation.html"
    ]

    def parse(self,response):
        global index
        index_str = str(index)
        print html2text.html2text('ooooooooooooooooook')
        filename = response.url.split('/')[-1].split('.')[0]
        content = response.css('.content').extract()[0]
        urls = response.xpath(xpath_str).extract()
        mdcontent = html2text.html2text(content)
        with open('.\\md\\' + index_str + '-' + filename + '.md','wb') as f:
            f.write(mdcontent.encode('utf-8'))
            f.close()
        for url in urls:
            index += 1
            url = 'http://cn.vuejs.org/' + url.encode('utf-8')
            yield scrapy.Request(url, callback=self.parse)