from flask import Flask
import os

#static_url_plan表示静态资源的路径，static_folder表示指定静态目录；templates表示指定模板目录
app = Flask(__name__, static_url_path='/', static_folder='resource', template_folder='template')
#生成随机着种子，用于产生session ID
app.config['SECRET_KEY'] = os.urandom(24)

# def gettype_02():
#     type = {'1': 'PHP开发2', '2': 'Java开发1', '3': 'Python开发3'}
#     return type
# app.jinja_env.globals.update(mytype=gettype_02)

#自定义模板页面的过滤器
def mylen(str):
    return len(str)
app.jinja_env.filters.update(mylen=mylen)

#无jinjr2模板的演练
if __name__ == '__main__':
    from controller.jinja2 import *
    app.register_blueprint(jinjar2)
    app.run(port=8080, debug=True)
