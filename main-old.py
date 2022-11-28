from flask import Flask, render_template, redirect, url_for, session, make_response,request
import os
from w3lib import url

#static_url_plan表示静态资源的路径，static_folder表示指定静态目录；templates表示指定模板目录
app = Flask(__name__, static_url_path='/', static_folder='resource', template_folder='template')
#生成随机着种子，用于产生session ID
app.config['SECRET_KEY'] = os.urandom(24)


#首页地址,默认get
@app.route('/')
def index():
    return render_template('index.html')

#文章页面get
@app.route('/article')
def read():
    return render_template('article.html')

#文章页面get第几页
@app.route('/article/<int:articleid>-<page>')
def my_read(articleid, page):
    return f"你正访问编号为：{articleid}的文章，目前是第{page}页"


#首页地址post请求，带参数，methods=  为定义请示为类型
@app.route('/user/reg', methods=['POST','GET'])
def register():
    return 'good'


@app.route('/red')
def red():
    return redirect('/')

#定义session
@app.route('/sess')
def sess():
    #设置Session的内容：用户名、呢称、角色权限
    session['islogin'] = 'true'
    session['username'] = 'woxy'
    session['nickname'] = '强哥'
    session['role'] = 'editor'
    return 'Done'




# Cookies的设置
@app.route('/cookie')
def cookie():
    #构建一个Cookie的对象
    response = make_response('这个Cookie操作')
    #设置Cookie的内容
    response.set_cookie('username', 'qiang', max_age=30)
    response.set_cookie('password', '123456', max_age=30)
    return response


@app.route('/sc/read')
def scread():
    #读取Session
    return '你当前的呢称（保存在Session内的）为：%s' %session.get('username')
    # # 读取Cookies
    # return '你当前的呢称（保存在Cookie内的）为：%s' % request.cookies.get('username')
    #清空session
    # session.clear()

#针对app定义的僵尸拦截器
@app.before_request
def before():
    #若用户已经登录session['islogin']='true',则不拦截
    # url = request.path #获取当前访问的地址后面定义路由部分内容
    #所有静态资源（JS、Image、CSS等），必须设置为白名单
    #登录或都跟用户权限要求相关的接口，必须放行
    #或者设置一个列表，来管理白名单
    #首先是路由接口列表
    pass_list = ['/', '/reg', '/login', '/vcode', '/sess']
    #资源列表接口


    suffix = url.endswith('.png') or url.endswith('.jpg') or url.endswith('.css') or url.endswith('.js')
    # if url == '/sess':
    if url in pass_list or suffix:
        pass
    elif session.get('islogin') != 'true':
        return '你当前还没有登录，无法访问页面'
    else:
        pass





if __name__ == '__main__':
    # 引用模块文档demo.py
    from controller.demo import *
    # 注册蓝图，才可以引用
    app.register_blueprint(demo)
    app.run(port=8080, debug=True)
