from flask import Blueprint, render_template,session
jinjar2 = Blueprint('jinjar2', __name__)

# @jinjar2.context_processor
# def gettype():
#     type = {'1': 'PHP开发', '2': 'Java开发', '3': 'Python开发11'}
#     return dict(mytype=type)

# #若要为自定义函数传参数，则需要使用二层闭包的方式
# @jinjar2.context_processor
# def myfun():
#     def mytype(arg):
#         type = {'1': 'PHP开发', '2': 'Java开发', '3': 'Python开发11'}
#         type = arg+1
#         return type
#     return dict(mytype=mytype)


@jinjar2.route('/jinja2')
def jinjar2_demo():
    session['username'] = '笔记'
    articlex = {'title': 'Flask实战教程', 'count': 100}
    return render_template('myhtml.html', article=articlex, count=100)
