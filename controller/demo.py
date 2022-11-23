from flask import Blueprint

demo = Blueprint('demo', __name__)

@demo.route('/demo')
#函数名称不能与全局变量名称一致
def my_demo():
    return '这是另外一个模块中的页面'
