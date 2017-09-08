import os
import sqlite3
from flask import Flask, request, session, render_template
from lib.Weather import Weather
from lib.DataOp import WeatherOp, HistoryOp, iniDatabase



app = Flask(__name__)
app.secret_key = os.urandom(24)

#初始化数据库
path = "one.db"
try:
    iniDatabase(path)
except:
    print("创建数据库报错")

def get_help():
    return """<h3>帮助</h3><br/>
    <p>输入城市名并点击查询查询该城市的天气数据；</p>
    <p>点击帮助，获取帮助文档；</p>
    <p>点击历史，获取历史查询信息；</p>"""

#自动生成用户标识
def get_user():
    try:
        cur_user = session['cur_user']
    except:
        cur_user = os.urandom(6)
        session['cur_user'] = cur_user
    return cur_user

@app.route('/', methods=['GET', 'POST'])
def getweather():
    if request.method == "GET":
        return render_template('index.html', outputdata='')

    elif request.method == "POST":

        conn = sqlite3.connect(path)
        cursor = conn.cursor()

        weathOp = WeatherOp(cursor)
        historyOp = HistoryOp(cursor)
        weath = Weather()
        cur_user = get_user()

        action = request.form['action']
        if action == "查询":
            city = request.form['city']
            html = ''
            if city != '':
                # try:
                    #从数据库查询天气数据
                cur_weath = weathOp.selectWeathByCity(city)
                print(cur_weath)
                if cur_weath:
                    cur_weath = cur_weath[0]
                else:
                    #若未查到则从API查询
                    cur_weath = weath.getnow(city)

                html = weath.printnow(cur_weath)
                    #升级weather表和history表
                weathOp.insertOneWeath(cur_weath)
                hisdic = cur_weath + (cur_user, )
                historyOp.insertOneHistory(hisdic)
                # except:
                #     html = "查询错误！"
            outputdata = html

        elif action == "历史":
            history = historyOp.selectAllHistory()
            print(cur_user)
            print(history)
            if len(history) > 0:
                html = "<h3>历史查询记录</h3>"
                i = 1
                for h_weather in history:
                    html += "<br/>"
                    html += f"{i}. "
                    html += weath.printnow(h_weather)
                    i += 1
                outputdata = html
            else:
                outputdata = "没有任何记录"

        elif action == "帮助":
            outputdata = get_help()

        elif action == "更正":
            alterData = request.form['city'].split()
            if len(alterData) == 2 :
                city = alterData[0]
                weather_text = alterData[1]
                if weather_text in ['阴', '雪']:
                    try:
                        weathOp.updateWeathByCity(weather_text, city)
                        outputdata = "更正数据成功！"
                    except:
                        outputdata = "更正数据失败"
            else:
                outputdata = "更正数据格式不正确"
        else:
            outputdata = ""

        cursor.close()
        conn.commit()
        conn.close()
        return render_template('index.html', outputdata=outputdata)


if __name__ == '__main__':
    app.run(debug=True, host = 0.0.0.0)
