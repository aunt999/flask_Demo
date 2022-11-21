from flask import Flask, render_template, redirect, url_for, session, make_response,request
import os

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

#首页地址post请求，带参数，methods=  为定义请示为类型
@app.route('/user/reg', methods=['POST','GET'])
def register():
    return 'good'


@app.route('/red')
def red():
    return redirect('/')

@app.route('/sess')
def sess():
    #设置Session的内容：用户名、呢称、角色权限
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
    # return '你当前的呢称（保存在Session内的）为：%s' %session.get('username')
    # 读取Cookies
    return '你当前的呢称（保存在Cookie内的）为：%s' % request.cookies.get('username')
    #清空session
    # session.clear()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
