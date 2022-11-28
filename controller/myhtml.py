from flask import Blueprint

myhtml = Blueprint('myhtml',__name__)

#设置一段html代码直接在页面生成，相当于无jinja2时，html是怎么返回页面的演练
#直接将html写在代码中，并返回
@myhtml.route('/template01')
def template01():

    resp = '''
    <div style="width:500px; height:300px; margin:auto; border:solid 2px red">
        <a href="#">笔记</a>
        <ul>
            <li>这是菜单</li>
            <li>这是单项</li>
            <li>这是多项</li>
            <li>这是判断</li>
            <li>这是简答</li>
            <li>这是应用</li>
        </ul>
        <p>欢迎登录</p>
    </div>
    '''
    return resp


#直接将html和变量进行拼接，再返回
@myhtml.route('/template02/<username>')
def template02(username):

    resp = '''
    <div style="width:500px; height:300px; margin:auto; border:solid 2px red">
        <a href="#">笔记</a>
        <ul>
            <li>这是菜单</li>
            <li>这是单项</li>
            <li>这是多项</li>
            <li>这是判断</li>
            <li>这是简答</li>
            <li>这是应用</li>
        </ul>
        <p>欢迎%s登录</p>
    </div>
    ''' % username
    return resp

#把html保存到文件.html的文件中，打开文件，并返回
@myhtml.route('/template03')
def template03():
    with open('d:/mypro/pytest/flaskDemo/flask_Demo/template/myhtml.html', encoding='utf-8') as file:
        html = file.read()

    return html

#把html保存到文件.html的文件中标记的变量，进行替换，打开文件，并返回
#使用替换来实现html内指定的变量的赋值
@myhtml.route('/template04')
def template04():
    with open('d:/mypro/pytest/flaskDemo/flask_Demo/template/myhtml.html', encoding='utf-8') as file:
        html = file.read()

    html = html.replace('{{username}}', '笔记')

    return html