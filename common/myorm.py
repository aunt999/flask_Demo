#第一部分，使用非orm的模式设计数据库表操作
import pymysql
from pymysql.cursors import DictCursor

class MySQL:
    #初始化并实例创建数据库连接
    def __init__(self):
        #创建数据库连接
        conn =pymysql.connect(host='127.0.0.1', user='root', password='root', charset='utf8', database='zentao', autocommit=True)
        #创建游标，并定义可以获取游标的字段名
        self.cursor = conn.cursor(DictCursor)

    #定义查询方法
    def query(self,sql):
        #执行sql语句
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    #定义修改操作方法
    def my_update(self, sql):
        try:
            self.cursor.execute(sql)
            return 'OK'
        except:
            return "Fail"


#封装成标准的模型类，提供子类继承
#数据库方面不指定明确的表名
#增加一个field()方法来指定查询哪些列，*代表所有列
class Model:
    ##构造方法，自动化列表转为Key，value的对应关系
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

   #通过链接操作的最后返回必定指向自己如：return self ,指定查询哪些字段，让查询的字段不在语句内固定
    def field(self, columns):
       self.columns = columns
       return self

    #重新封装查询方法，让表名与字段名不固定
    def select(self, **where):
        #获取继承的子类传进来的表名,此处的self为子类的类名
        table = self.__class__.__getattribute__(self, "table_name")

        #判断对象是否包含对应的属性，即传入的对象columns属性
        if hasattr(self, "columns"):
            sql = "select %s from %s" % (self.columns, table)
        else:
            sql = "select * from %s" % table
        # 取出where字典参数的内容,使用None判断列否为空，即使where无值也是非空，只有采用判断len(where)！=0才能真正判断是否空值
        # if where is not None:
        if len(where) != 0:
            sql += " where"
            for k, v in where.items():
                sql += " %s=%s and" % (k, v)
            sql += " 1=1"

        # 增加条件输入的查询操作
        result = MySQL().query(sql)
        return result

            # 封装新增

    def insert(self):
        # 构造函数取出来的字典后，在Insert时需要把key 与 value分开为两个列表，分别对应插入语法的两个部分
        keys = []
        values = []
        for k, v in self.__dict__.items():
            keys.append(k)
            values.append(str(v))

        # 使用join将连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
        sql = "insert into %s(%s) value('%s')" % (self.table_name, ",".join(keys), "','".join(values))
        result = MySQL().query(sql)
        return result



# #增加使用类似ORM框架模式的数据库操作方式的类Users,而原来的类Mysql不变
# class Users:
#     #定义数据库表名，以类属性的方式来定义, 此处定义表名与类名不一至。
#     # 也是将类名直接当做表名来处理，此时需要使用__class__来获取类名，相当于表名，这种方式即将表转为面向对象处理
#     table_name = 'zt_build'
#
#     #构造方法，自动化列表转为Key，value的对应关系
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             #动态生成字典关系
#             self.__setattr__(k, v)
#         print(self.__dict__)
#
#     #封装查询操作
#     #*变量（*a)：获取是不定长的列表参数； **变量(**a)：获取的是不定长的字典参数
#     def select(self, **where):
#         sql = "select * from %s" % self.table_name
#         #取出where字典参数的内容,使用None判断列否为空，即使where无值也是非空，只有采用判断len(where)！=0才能真正判断是否空值
#         # if where is not None:
#         if len(where) !=0:
#             sql +=" where"
#             for k, v in where.items():
#                 sql += " %s=%s and"% (k, v)
#             sql +=" 1=1"
#
#         #增加条件输入的查询操作
#         result = MySQL().query(sql)
#         return result
#
#    #封装新增
#     def insert(self):
#         #构造函数取出来的字典后，在Insert时需要把key 与 value分开为两个列表，分别对应插入语法的两个部分
#         keys = []
#         values = []
#         for k, v in self.__dict__.items():
#             keys.append(k)
#             values.append(str(v))
#
#         #使用join将连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#         sql = "insert into %s(%s) value('%s')" % (self.table_name, ",".join(keys), "','".join(values))
#         result = MySQL().query(sql)
#         return result

#子类继承于父类
class Users(Model):
    table_name = 'zt_build'

    #通过子类的构造函数，调用父类的构造函数
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':
    user = Users()
    #查询所有记录
    # result = user.select()
   #查询指定字段的内容
    result = user.field('id, project, name').select(id=1)
    print(result)