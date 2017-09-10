import os
from flask import session

def get_weathdic(path):
    with open(path, 'r', encoding = "utf-8") as dicfile:
        weather_dic = [weath.strip() for weath in dicfile]
    return weather_dic

def get_help():
    return """<h3>帮助</h3><br/>
    <p>输入城市名并点击查询查询该城市的天气数据；</p>
    <p>点击帮助，获取帮助文档；</p>
    <p>点击历史，获取历史查询信息；</p>
    <p>输入“城市 天气”，并点击更改，更改指定城市的实时天气数据；</p>"""

#自动生成用户标识
def get_user():
    try:
        cur_user = session['cur_user']
    except:
        cur_user = os.urandom(6)
        session['cur_user'] = cur_user
    return cur_user
