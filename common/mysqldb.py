import pymysql
from pymysql.cursors import DictCursor

"""
所有的I/O操作：文件、数据库、网络等操作，均要有这三个步骤：
第一步：连接到mysql数据库
第二步：执行sql语句
1.实例化一个游标对象； 2.定义SQL语句； 3.通过游标执行；4.处理执行结果；
第三步：关闭数据库连接
"""
#第一步：连接到mysql数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8', database='zentao', autocommit=True)
#打印数据库版本信息
# print(conn.get_server_info())
# #查询
cursor = conn.cursor(DictCursor)
# sql = "select * from zt_build where id = 3"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# #取某一个字段，即列的记录
# for row in result:
#     print(row[5])
# #直接取某行记录的某列，用二维数组

#建议使用Key-value的方式，即Key=>列名，value=>单元格的值，使用此方式，需要在游标中传入一个参数DictCursor,即：cursor = conn.cursor(DictCursor)
#需要引用游标模块：from pymysql.cursors import DictCursor
# print(result[0]['name'])

#操作数据库updata、insert、delete三个操作必须在操作完成后，提交数据commit()
sql = "update zt_build set name='V1.0' where id = 1"
#执行以上sql语句
cursor.execute(sql)
# #提交操作到数据库
# conn.commit()


#完成使用数据库，需要先关闭游标，再关闭数据库的连接
cursor.close()
conn.close()

