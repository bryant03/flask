# -*- coding: utf-8 -*-

import pymongo

# 返回一个 collection
# 
def get_coll():

    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.stress
    db.authenticate("stress", "stress")
    user = db.user

    return user


class User(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        user = {"name": self.name, "email": self.email}
        coll = get_coll()
        id = coll.insert(user)
        print (id)
    @staticmethod
    def verify(name,password):
        coll = get_coll()
        answer =0
        for i in coll.find({"name":name}):
            answer=1
            for j in coll.find({"name":name,"password":password}):
                answer=2

        return answer
    @staticmethod
    def sign(name,password):
        answer=2
        for i in get_coll().find({"name":name}):
            answer=3
        if answer == 2:
            add_user=[{"name":name,"password":password}]  
            get_coll().insert(add_user) 

        return answer


    @staticmethod
    def query_users():
        users = get_coll().find()
        print(type(users))
        return users
