# -*- coding: utf-8 -*-

from flask_script import Manager
from app import app
from model import User

# 实例化
manager = Manager(app)

# 修饰器
@manager.command
def save():
    user = User('caolei', 'ming@hehe.com')
    user.save()

@manager.command
def query_users():
    
    users = User.query_users()
    for user in users:
        print (user)


if __name__ =="__main__":
    manager.run()
