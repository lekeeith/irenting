
from flask import Flask
from flask_sqlalchemy import SQLALCHEMY
from flask_session import Session
from flask_wtf import CSRFProtect

import redis

app = Flask(__name__)

class Config:
    DEBUG = True
    SECRET_KRY = "nacokmvADOJ*^1wcmdcqps"

    # 数据库
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis配置
    REDIS_HOST = ""
    REDIS_PORT = ""

    SESSION_TYPE = ""
    SESSION_REDIS = redis.StrictRedis(host="", port=6379)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400

app.congig.from_object(Config)

db = SQLALCHEMY(app)

redis_store = redis.StrictRedis()

#
Session(app)

CSRFProtect(app)

@app.route("/index")
def index():
    return "index page"

if __name__ == "__main__":
    app.run