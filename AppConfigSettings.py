from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import redis
from flask_wtf import CSRFProtect

app = Flask(__name__)


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


app.config.from_object(Config)
# 数据库要和 app关联
db = SQLAlchemy(app)
# csrf保护
CSRFProtect(app)
# 设置session保存指定位置
Session(app)
