from flask import Flask
from config import create_map
from flask_sqlalchemy import SQLALCHEMY
from flask_session import Session
from flask_wtf import CSRFProtect


import redis

db = SQLALCHEMY(app)


redis_store = redis.StrictRedis(host="", port="")

# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str 配置模式名称
    :return:
    """
    app = Flask(__name__)
    config_class = create_map.get(config_name)
    app.config.from_object(config_class)
    db.init_app(app)

    redis_store = redis.StrictRedis(host="", port="")

    #
    Session(app)

    CSRFProtect(app)

    return app
