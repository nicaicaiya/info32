# 导入flask内置的模块
from flask import Flask, session
# 把session存储在redis数据库中
from flask_session import Session
# 导入redis实例
from redis import StrictRedis

app = Flask(__name__)
# 开启调试模式
app.config['DEBUG'] = True
# 设置秘钥
app.config['SECRET_KEY'] = 'AD5V1H4u4AaYdsd6ux0YtrbTv+LrFgPTj8ywq6wKNvSxhg62xoKkJfwcdZs1'
# 制定session信息存储的位置
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = StrictRedis(host='127.0.0.1', port=6379)
app.config['SESSION_USE_SINGER'] = True  # 对session信息进行签名
app.config['PERMANENT_SESSION_LIFETIME'] = 86400  # flask框架再带的配置session有效期


# 实例化SESSION
Session(app)


@app.route('/')
def index():
    # 状态保持
    session['itcast'] = '2018'
    return 'hello world'

if __name__ == '__main__':
    app.run()