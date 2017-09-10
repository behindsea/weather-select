import os
from flask import session

def get_weathdic(path):
    with open(path, 'r', encoding = "utf-8") as dicfile:
        weather_dic = [weath.strip() for weath in dicfile]
    return weather_dic

#自动生成用户标识
def get_user():
    try:
        cur_user = session['cur_user']
    except:
        cur_user = os.urandom(6)
        session['cur_user'] = cur_user
    return cur_user

def datetimeformat(value):
    timestr = value[0:19]
    return timestr
