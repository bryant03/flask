# -*- coding: utf-8 -*-
from flask import Flask,url_for,request
from flask_mongoengine import MongoEngine 
import json
from model import User

app = Flask(__name__)


# test 是链接的数据库
#app.config['MONGODB_SETTINGS'] = {'db': 'stress'}


# 实例化
#db = MongoEngine(app)
#db.authenticate("stress", "stress")
@app.route('/')
def index():
    return 'this is index page'

@app.route('/hello',methods=['POST','GET'])
def hello_world():
    if request.method=='POST':
        return 'fuck'
    else :
        return 'Hello World!'

@app.route('/login',methods=['POST','GET'])
def login():
    # 获取post.form

    PostForm=request.form
    # 获取post的字典
    dict_data = {key:dict(request.form)[key][0] for key in dict(request.form)}
    # 将字典转换为json
    xjson=json.loads(dict_data['body'])
    name=xjson['name']
    password=xjson['password']
    op=xjson['op']
    answer=0  #要返回给APP的参数
    
    if op== '1':
        answer= User.verify(name,password)
    else :
        answer= User.sign(name,password)        
    return str(answer)

# 获取用户数据
@app.route('/test',methods=['POST','GET'])
def test():
    if request.method =='GET':
        return 'you use a get method.'
    else :
        dict_data = {key:dict(request.form)[key][0] for key in dict(request.form)}
        print(dict_data)
        #print('request.data ',request.data)
        print('request.form ',request.form)
        return 'ok, server get it.'
    
@app.route('/user',methods=['post'])
def show_user_profile():
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# with app.test_request_context():
#     print (url_for('index'))
#     print (url_for('hello_world'))
#     print (url_for('show_user_profile',username='df'))



# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'

if __name__ == '__main__':
    app.run()
