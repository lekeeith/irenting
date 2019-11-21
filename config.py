

class Config:
    """基本配置"""
    SECRET_KRY = "nacokmvADOJ*^1wcmdcqps"

    # 数据库
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis配置
    REDIS_HOST = ""
    REDIS_PORT = ""

    # Session配置
    SESSION_TYPE = ""
    SESSION_REDIS = redis.StrictRedis(host="", port=6379)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400


class LocalConfig(Config):
    """本地开发环境"""
    DEBUG = True


class ProductConfig(Config):
    """项目正式上线配置"""
    pass


# 构建映射关系
create_map = {
    1 : "LocalConfig",
    0 : "ProductConfig"
}