import redis

from utils import create_app

app = create_app()


class Config(object):
    """
    配置
    """
    DEBUG = True
    host = 'localhost'
    port = 3306
    db_username = 'root'
    db_password = '123456'
    db = 'information'
    connect_str = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(db_username, db_password, host, port, db)

    # 设置数据库连接
    app.config['SQLALCHEMY_DATABASE_URI'] = connect_str
    # 动态追踪设置
    app.config['SQLALCHEMY_TRACK_MODUFICATIONS'] = True
    # 显示原始sql
    # app.config['SQLALCHEMY_ECHO'] = True
    # 设置每次请求后自动提交数据库的改动
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session 配置
    SESSION_TYPE = 'redis'  # session保存到redis
    SESSION_USE_SINGER = True  # cookie中的session_id被加密处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # redis实例
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400  # 单位为s，session有效时间


# 开发环境
class DevelopConfig(Config):
    pass


# 生产环境
class ProductConfig(Config):
    DEBUG = False


# 测试环境
class TestingConfig(Config):
    TESTING = True


# 通过统一的字典进行配置类的访问
config_dict = {
    "develop": DevelopConfig,
    "product": ProductConfig,
    "testing": TestingConfig,
}
