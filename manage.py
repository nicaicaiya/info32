# 导入脚本管理器
from flask_script import Manager

# 从info目录下的__init__文件中导入创建app的函数create_app
from info import create_app


# 调用info目录下的__init__文件的函数
app = create_app('development')


# 实例化管理器对象
manage = Manager(app)

if __name__ == '__main__':
    # app.run()
    print(app.url_map)
    manage.run()