from flask import Flask, current_app
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# 为兼容老版本的mysql需要通过pymsql注册上mysqldb
import pymysql

from controller import user

pymysql.install_as_MySQLdb()

# static_url_plan表示静态资源的路径，static_folder表示指定静态目录；templates表示指定模板目录

app = Flask(__name__, static_url_path='/', static_folder='resource', template_folder='template')
# 生成随机着种子，用于产生session ID
app.config['SECRET_KEY'] = os.urandom(24)

# Flask使用集成的方式连接mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/woniunote?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 实例化DB对象
db = SQLAlchemy(app)
# md = db.MetaData(bind=db.engine)
cxl = app.app_context()
cxl.push()


# def gettype_02():
#     type = {'1': 'PHP开发2', '2': 'Java开发1', '3': 'Python开发3'}
#     return type
# app.jinja_env.globals.update(mytype=gettype_02)

# 自定义模板页面的过滤器
# def mylen(str):
#     return len(str)
#
#
# app.jinja_env.filters.update(mylen=mylen)
#
#
# # 定制错误页面
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('error-404.html')


# 无jinja2模板的演练
if __name__ == '__main__':
    from controller.jinja2 import *

    app.register_blueprint(jinjar2)

    from controller.user import *
    app.register_blueprint(user)

    app.run(port=8080, debug=True)
