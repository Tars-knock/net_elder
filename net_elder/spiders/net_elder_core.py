import scrapy

from net_elder.items import NetElderItem


class NetElderCore(scrapy.Spider):
    name = "core"

    def start_requests(self):
        # 起点url选择导航站之类 外链比较多的网站
        origin_url = [
            'https://hao123-hao123.com/',
            'https://hao.qq.com/',
            'https://www.foreverblog.cn/blogs.html?year=2020',
            'https"//tars-knock.cn'
        ]

    def parse(self, response, **kwargs):
        current_url = response.url
        urls = response.css('a.attr(href)').getall()
        for target_url in urls:
            a1 = target_url.split('/')[2].split('.')
            a2 = current_url.split('/')[2].split('.')
            # 识别外链并访问
            if a1[-1] == a2[-1] & a1[-2] == a2[-1]:
                yield response.follow(target_url, self.parse)

            title = response.css('title::text').getall()[0]
            description = None
            metas = response.css('meta')
            for meta in metas:
                if meta.attrib['name'] == 'description':
                    description = meta.attrib['content']

            yield NetElderItem(
                locate_url=current_url,
                title=title,
                description=description
            )
