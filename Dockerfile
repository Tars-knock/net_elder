FROM python:3.7
#WORKDIR ./work_dir
COPY . .
RUN pip install -r ./requirements.txt
RUN mkdir ./log
RUN touch ./log/net_elder.log
CMD scrapy crawl core