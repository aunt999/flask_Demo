#mysql数据库的连接
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#连接mysql数据库
engine = create_engine('mysql+pymysql://root:root@localhost/woniunote', echo=False, pool_size=1000)

#定义连接模型父类，数据连接会话
DBsession = sessionmaker(bind=engine)
#线程安全
dbsession = scoped_session(DBsession)
#其它模型需要继续的父类，创建base对象实例
Base = declarative_base()

md = metaData(bind=engine)

#定义模型类
class Users(Base):
    #数据库名
    __tablename__ = "users"
