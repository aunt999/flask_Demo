# 创建一个数据表的模型
from sqlalchemy import Table, MetaData
from main import db


# 在模型文件中进行数据的定义与连接操作
class Users(db.Model):
    __table__ = Table('user', MetaData(bind=db.engine), autoload=True)

    # 定义一个操作数据库的函数
    def find_user_by_id(self, userid):
        row = db.session.query(Users).filter_by(userid=1).first()
        return row.username
