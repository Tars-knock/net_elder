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
        urls = response.css('a::attr(href)').getall()
        for target_url in urls:
            if not target_url.startswith('http'):
                continue
            # logger.info(f' target url:{target_url}')
            a1 = target_url.split('/')[2].split('.')
            a2 = current_url.split('/')[2].split('.')
            # 识别外链并访问
            if a1[-1] != a2[-1] or a1[-2] != a2[-2]:
                logger.info(f'next request: {target_url}')
                yield scrapy.Request(target_url, self.parse)

        # 提取当前网页信息
        title = response.css('title::text').getall()[0]
        description = response.xpath("//meta[@name='description']/@content").get()
        # logger.info(f' an item to pipeline url:{current_url} title:{title} description:{description}')
        item = NetElderItem()
        item['title'] = title
        item['locate_url'] = current_url
        item['description'] = description
        yield item

        # yield NetElderItem(
        #     locate_url=current_url,
        #     title=title,
        #     description=description
        # )
