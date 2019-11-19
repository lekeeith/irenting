from flask import Flask
from config import create_map
from flask_sqlalchemy import SQLALCHEMY


db = SQLALCHEMY(app)


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str 配置模式名称
    :return:
    """
    app = Flask(__name__)
    config_class = create_map.get(config_name)
    app.congig.from_object(config_class)
    db.init_app(app)

    return app
