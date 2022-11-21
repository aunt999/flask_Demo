from flask import Flask, render_template
#static_url_plan表示静态资源的路径，static_folder表示指定静态目录；templates表示指定模板目录
app = Flask(__name__, static_url_path='/', static_folder='resource', template_folder='template')

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


if __name__ == '__main__':
    app.run(port=8080, debug=True)
