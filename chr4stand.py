import os
import sqlite3
from datetime import datetime,timezone,timedelta
from flask import Flask, request, session, render_template
from lib.Weather import Weather
from lib.DataOp import WeatherOp, HistoryOp, iniDatabase, cleanDatabase
from lib.ProgramAction import get_weathdic, get_help, get_user, datetimeformat


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.add_template_filter(datetimeformat, 'datetimeformat')

#初始化数据库
path = "one.db"
try:
    iniDatabase(path)
except:
    pass
    # print("创建数据库报错")

weather_dic = get_weathdic('weather_dic.txt')

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
        weatherdata = []
        title = ""
        cleanDatabase(cursor)

        action = request.form['action']
        if action == "select":
            city = request.form['city']
            html = ''
            if city != '':
                try:
                    # 从数据库查询天气数据
                    cur_weath = weathOp.selectWeathByCity(city)

                    if cur_weath:
                        cur_weath = cur_weath[0]
                    else:
                        #若未查到则从API查询
                        cur_weath = weath.getnow(city)

                    weatherdata = [cur_weath]
                    html = '<h3>实时天气数据</h3>'
                    #升级weather表和history表
                    weathOp.insertOneWeath(cur_weath)
                    cur_time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
                    hisdic = (cur_weath[0], cur_weath[1], cur_weath[2], cur_weath[3], cur_time, cur_user)
                    historyOp.insertOneHistory(hisdic)
                except:
                    html = "查询错误！"
            title = html

        elif action == "history":
            history = historyOp.selectHistoryByUser(cur_user)

            if len(history) > 0:
                weatherdata = history
                html = "<h3>历史查询记录</h3>"
                title = html
            else:
                title = "没有任何记录"

        elif action == "help":
            title = get_help()

        elif action == "alter":
            alterData = request.form['city'].split()
            if len(alterData) == 2 :
                city = alterData[0]
                weather_text = alterData[1]
                if weather_text in weather_dic:
                    try:
                        weathOp.updateWeathByCity(weather_text, city)
                        title = "更正数据成功！"
                    except:
                        title = "更正数据失败"
                else:
                    title = "请输入正确的天气"
            else:
                title = "更正数据格式不正确"
        else:
            title = ""

        cursor.close()
        conn.commit()
        conn.close()
        return render_template('index.html', title=title, weatherdata=weatherdata)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
