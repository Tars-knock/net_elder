import configparser
from datetime import datetime

from pymysql import TIMESTAMP
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(200))
    title = Column(String(200))
    description = Column(String(200))
    create_time = Column('timestamp', TIMESTAMP, nullable=False, default=datetime.now())


class MysqlDriver:

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

    def test_insert(self):
        data_tars = pd.DataFrame({
            'id': [2],
            'url': ['https://tars-knock.cn'],
            'title': ['Tars blog'],
            'description': ['Tars赛博小窝']})
        data_tars.to_sql('url', self.engine, index=False)

    def test_select(self):
        DBSession = sessionmaker(self.engine)
        session = DBSession()
        # Base.to_dict = to_dict
        rows = session.query(Url).all()
        print([row.to_dict() for row in rows])
        session.close()


if __name__ == '__main__':
    connection = MysqlDriver()
    connection.test_select()
    # connection.test_insert()
