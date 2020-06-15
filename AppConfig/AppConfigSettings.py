from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from AppConfig.config import Config
from utils import create_app

app = create_app()
app.config.from_object(Config)

# 设置session保存指定位置
Session(app)

# csrf保护
CSRFProtect(app)

# 数据库
db = SQLAlchemy(app)
