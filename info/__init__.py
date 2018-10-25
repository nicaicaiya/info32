# 导入flask内置的模块
from flask import Flask
# 导入配置
from config import Config, config_dict
# 把session存储在redis数据库中
from flask_session import Session
# 使用标准日志模块
import logging
from logging.handlers import RotatingFileHandler

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)


# 封装函数，用来创建程序示例app，
# 让app根据函数的调用来生产不同环境下的app
# config_name=development会创建一个开发模式的app，debug=True
# config_name=production会创建一个生产模式的app，debug=False


def create_app(config_name):
    app = Flask(__name__)

    # 使用配置类
    app.config.from_object(config_dict[config_name])

    # 实例化SESSION
    Session(app)

    # 导入蓝图
    from info.modules.news import news_blue
    app.register_blueprint(news_blue)

    return app
