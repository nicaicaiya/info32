# 导入flask内置的模块
from flask import Flask, session
# 把session存储在redis数据库中
from flask_session import Session

# 导入脚本管理器
from flask_script import Manager

# 导入配置
from comfig import Config

app = Flask(__name__)

# 使用配置类
app.comfig.from_object(Config)

# 实例化SESSION
Session(app)

# 实例化管理器对象
manage = Manager(app)


@app.route('/')
def index():
    # 状态保持
    session['itcast'] = '2018'
    return 'hello world'

if __name__ == '__main__':
    # app.run()
    manage.run()