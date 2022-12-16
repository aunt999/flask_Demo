# 控制类，主要控制页面跳转
from module.users import Users
from flask import Blueprint


user = Blueprint('users', __name__)


@user.route('/user')
def user_demo():
    # 实例化User类
    users = Users()
    row = users.find_user_by_id(1)
    return row


