import pymysql

"""
所有的I/O操作：文件、数据库、网络等操作，均要有这三个步骤：
第一步：连接到mysql数据库
第二步：执行sql语句
1.实例化一个游标对象； 2.定义SQL语句； 3.通过游标执行；4.处理执行结果；
第三步：关闭数据库连接
"""
#第一步：连接到mysql数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8', database='zentao')
#打印数据库版本信息
print(conn.get_server_info())
cursor = conn.cursor()
sql = "select * from zt_build"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
