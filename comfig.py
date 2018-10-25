# 导入redis实例
from redis import StrictRedis
# 自定义配置类
class Config():
    # 开启调试模式
    DEBUG = True
    # 设置秘钥
    SECRET_KEY = 'AD5V1H4u4AaYdsd6ux0YtrbTv+LrFgPTj8ywq6wKNvSxhg62xoKkJfwcdZs1'
    # 制定session信息存储的位置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host='127.0.0.1', port=6379)
    # 对session信息进行签名
    SESSION_USE_SINGER = True
    # flask框架再带的配置session有效期
    PERMANENT_SESSION_LIFETIME = 86400