import requests
import datetime
class Weather(object):
    """天气类，用于查询和打印天气数据"""

    def __init__(self):
        """用于初始化API设置"""
        self.nowapi = 'https://api.seniverse.com/v3/weather/now.json'
        self.key = '4r9bergjetiv1tsd'
        self.language = 'zh-Hans'
        self.unit = 'c'
        self.timeout = 3

    def getnow(self, city):
        """根据输入参数名查询天气数据，返回字典"""
        result = requests.get(self.nowapi, params={
            'key': self.key,
            'location': city,
            'language': self.language,
            'unit': 'c'
            }, timeout=self.timeout)

        cur_weath = result.json()
        now = cur_weath['results'][0]['now']
        weathdir = (cur_weath['results'][0]['location']['name'],
            now['text'],
            now['wind_direction'],
            now['temperature'],
            datetime.datetime.now())

        return weathdir

    def trantemper(self, temperature):
        """转换温度单位"""
        if self.unit == 'c':
            return f"{temperature}°C"
        elif self.unit == 'f':
            temper = float(temperature)
            f = temper * 9 / 5 + 32
            return f"{f}°F"
