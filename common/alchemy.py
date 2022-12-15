# mysql数据库的连接
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# 连接mysql数据库
engine = create_engine('mysql+pymysql://root:root@localhost/woniunote')

# 定义连接模型父类，数据连接会话
DBsession = sessionmaker(bind=engine)
# 线程安全
dbsession = scoped_session(DBsession)
# 其它模型需要继续的父类，创建base对象实例
Base = declarative_base()
# 定义元数据
md = MetaData(bind=engine)


# 定义模型类
class Users(Base):
    # 数据库名
    __table__ = Table('user', md, autoload=True)


if __name__ == '__main__':
    # 不带任何条件的查询all()查询并返回所有， first() 为查询并返回第一条
    # result = dbsession.query(Users).all()
    # 带条件的查询，采用条件参数的方式，这种条件参数写法需要从类名开始取
    # result = dbsession.query(Users).filter(Users.userid == 1).all()
    # 带条件的查询，采用字典方式查询，使用filter_by的函数
    # result = dbsession.query(Users).filter_by(userid=1).all()
    # # # 定义查询字段，并有查询条件，只获取第一条结果
    result = dbsession.query(Users.userid, Users.nickname).filter(Users.userid >= 1).first()
    print(result.nickname)
    # 直接获取查询返回的对象和地址
    print(result)
    # # 直接获取可以通过[数组].字段名
    # print(result[0].nickname)
    # 使用循环的方式获取每一行的内容
    # for row in result:
    #     # 通过字row后面的字段名获取相应字段的内容
    #     print(row.userid, row.nickname)
    # 新增
    # user = Users(username='reader2@@niuxy.com', password='123456', role='editor', credit=50)
    # dbsession.add(user)
    # dbsession.commit()

    # 修改，需要先查询再操作
    # row = dbsession.query(Users).filter_by(userid=2).first()
    # row.credit = '50'
    # dbsession.commit()

    # 删除
    row = dbsession.query(Users).filter(Users.userid >= 3).delete()
    dbsession.commit()
