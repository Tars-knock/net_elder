FROM python:3.7
WORKDIR ./work_dir
COPY . .
# Using douban pipy mirror
RUN pip3 install -i https://pypi.douban.com/simple/ -U pip
RUN pip3 config set global.index-url https://pypi.douban.com/simple/

RUN pip install -r ./requirements.txt
RUN mkdir ./log
RUN touch ./log/net_elder.log
CMD scrapy crawl core