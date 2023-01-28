import configparser

from sqlalchemy import create_engine


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