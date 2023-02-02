import configparser
import datetime

from sqlalchemy import String, create_engine, select
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }


class Url(Base):
    __tablename__ = "url"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(200))
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(200))
    # Column('timestamp', TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, default=datetime.datetime.now())

    def __repr__(self) -> str:
        return f"Url(id={self.id!r}, title={self.title!r}, createTime={self.create_time}, url={self.url!r})"


class Driver:
    def __init__(self):
        config = configparser.ConfigParser()
        # 从配置文件读取数据库相关设置
        config.read("../mysql-config.ini", encoding="utf-8")
        config.sections()
        config.options("mysql")
        # 初始化数据库连接
        # 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
        self.engine = create_engine(
            "mysql+pymysql://{}:{}@{}:{}/{}".format(config.get("mysql", "name"), config.get("mysql", "passwd"),
                                                    config.get("mysql", "host"), config.get("mysql", "port"),
                                                    config.get("mysql", "dbname")))
        print(self.engine.url)

    def test_select(self):
        session = Session(self.engine)
        # urls = select(Url).where(Url.id.__eq__(1))
        urls = select(Url)
        # for url in session.scalar(urls):
        #     print(url)
        print(session.scalar(urls))


if __name__ == '__main__':
    driver = Driver()
    driver.test_select()
