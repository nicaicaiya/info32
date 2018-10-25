# 导入flask内置的模块
from flask import Flask
# 导入配置
from config import Config, config_dict
# 把session存储在redis数据库中
from flask_session import Session


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
