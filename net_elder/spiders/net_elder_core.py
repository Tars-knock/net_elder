import logging

import scrapy

from net_elder.items import NetElderItem

logger = logging.getLogger('spider_logger')


class NetElderCore(scrapy.Spider):
    name = "core"

    def start_requests(self):
        # 起点url选择导航站之类 外链比较多的网站
        origin_url = [
            'https://hao.qq.com/',
            'https://hao123-hao123.com/',
            'https://www.foreverblog.cn/blogs.html?year=2020',
            'https://tars-knock.cn'
        ]

        for url in origin_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        current_url = response.url
        urls = response.css('a.attr(href)').getall()
        for target_url in urls:
            a1 = target_url.split('/')[2].split('.')
            a2 = current_url.split('/')[2].split('.')
            # 识别外链并访问
            if a1[-1] == a2[-1] & a1[-2] == a2[-1]:
                logger.info(f'next request: {target_url}')
                yield response.follow(target_url, self.parse)

            title = response.css('title::text').getall()[0]
            description = None
            metas = response.css('meta')
            for meta in metas:
                if meta.attrib['name'] == 'description':
                    description = meta.attrib['content']

            logger.info(f'an item to pipeline url:{target_url}')
            yield NetElderItem(
                locate_url=current_url,
                title=title,
                description=description
            )
