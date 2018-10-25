# 导入flask内置的模块
from flask import session
# 从news/__init__文件中导入蓝图对象
from . import news_blue


@news_blue.route('/')
def index():
    # 状态保持
    session['itcast'] = '2018'
    return 'hello world'
