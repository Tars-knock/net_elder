import scrapy


class HelloScrapy(scrapy.Spider):
    name = "hello"

    def start_requests(self):
        urls = [
            'http://tars-knock.cn/',
            'http://tars-knock.cn/archives/90',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 这里注意 不使用getall方法时返回值为 selector对象； getall后才是字符串数组
        titles = response.css('a.post-title::text').getall()
        links = response.css('a.post-title::attr(href)').getall()
        # zip（）方法同时遍历两个数组
        for title, link in zip(titles, links):
            # self.log(f'title:{title}, link:{link}')
            yield {
                'title': title,
                'link': link
            }
        # self.log(f'Saved file {filename}')
