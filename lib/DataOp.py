<<<<<<< HEAD
import sqlite3

def iniDatabase(path):
    """初始化数据库，创建weather和history两个表"""
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE WEATHER
        (ID    INTEGER  PRIMARY KEY  AUTOINCREMENT ,
        CITY            TEXT     NOT NULL,
        WEATHER_TXT     TEXT     NOT NULL,
        WIND_DIRECTION  TEXT     NOT NULL,
        TEMPERATURE     INT      NOT NULL,
        UPDATE_TIME     timestamp     NOT NULL)
        """)

    cursor.execute("""CREATE TABLE HISTORY
        (ID    INTEGER  PRIMARY KEY  AUTOINCREMENT ,
        CITY            TEXT     NOT NULL,
        WEATHER_TXT     TEXT     NOT NULL,
        WIND_DIRECTION  TEXT     NOT NULL,
        TEMPERATURE     INT      NOT NULL,
        UPDATE_TIME     timestamp     NOT NULL,
        USER            TEXT)
        """)
    cursor.close()
    conn.commit()
    conn.close()


class WeatherOp(object):
    """天气数据表操作类"""
    def __init__(self, cursor):
        self.cursor = cursor

    def updateWeathByCity(self, weath, city):
        self.cursor.execute("""UPDATE WEATHER SET WEATHER_TXT = ? WHERE CITY = ?""", (weath, city))

    def insertOneWeath(self, weathdir):
        self.cursor.execute("""INSERT INTO WEATHER (CITY, WEATHER_TXT,
                    WIND_DIRECTION, TEMPERATURE, UPDATE_TIME)
                    VALUES (?, ?, ?, ?, ?)""",weathdir)

    def selectAllWeather(self):
        self.cursor.execute("SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME FROM WEATHER")
        weathdic = self.cursor.fetchall()
        return weathdic

    def selectWeathByCity(self, city):
        self.cursor.execute("""SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME
                    FROM WEATHER
                    WHERE CITY = ?""", (city,))
        weathdic = self.cursor.fetchall()
        return weathdic

    def deleteWeatherOuttime(self):
        self.cursor.execute("""DELETE FROM WEATHER WHERE DATETIME(UPDATE_TEME) > DATETIME('now', '-10 minutes')""")

    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()



class HistoryOp(object):
    """历史数据存储表操作类"""
    def __init__(self, cursor):
        self.cursor = cursor

    def insertOneHistory(self, historydir):
        self.cursor.execute("""INSERT INTO HISTORY (CITY, WEATHER_TXT,
                    WIND_DIRECTION, TEMPERATURE, UPDATE_TIME, USER)
                    VALUES (?, ?, ?, ?, ?, ?)""",historydir)

    def selectAllHistory(self):
        self.cursor.execute("""SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME
                    FROM HISTORY""")
        hisdic = self.cursor.fetchall()
        return hisdic

    def selectHistoryByUser(self, user):
        self.cursor.execute("""SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME
                    FROM HISTORY
                    WHERE USER = ?""", (user,))
        hisdic = self.cursor.fetchall()
        return hisdic

    def deleteHistoryByUser(self, user):
        self.cursor.execute("""DELETE FROM HISTORY WHERE USER = ?""", (user,))


    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()
=======
import sqlite3

def iniDatabase(path):
    """初始化数据库，创建weather和history两个表"""
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE WEATHER
        (ID    INTEGER  PRIMARY KEY  AUTOINCREMENT ,
        CITY            TEXT     NOT NULL,
        WEATHER_TXT     TEXT     NOT NULL,
        WIND_DIRECTION  TEXT     NOT NULL,
        TEMPERATURE     INT      NOT NULL,
        UPDATE_TIME     timestamp     NOT NULL)
        """)

    cursor.execute("""CREATE TABLE HISTORY
        (ID    INTEGER  PRIMARY KEY  AUTOINCREMENT ,
        CITY            TEXT     NOT NULL,
        WEATHER_TXT     TEXT     NOT NULL,
        WIND_DIRECTION  TEXT     NOT NULL,
        TEMPERATURE     INT      NOT NULL,
        UPDATE_TIME     timestamp     NOT NULL,
        USER            TEXT)
        """)
    cursor.close()
    conn.commit()
    conn.close()


class WeatherOp(object):
    """天气数据表操作类"""
    def __init__(self, cursor):
        self.cursor = cursor

    def updateWeathByCity(self, weath, city):
        self.cursor.execute("""UPDATE WEATHER SET WEATHER_TXT = ? WHERE CITY = ?""", (weath, city))

    def insertOneWeath(self, weathdir):
        self.cursor.execute("""INSERT INTO WEATHER (CITY, WEATHER_TXT,
                    WIND_DIRECTION, TEMPERATURE, UPDATE_TIME)
                    VALUES (?, ?, ?, ?, ?)""",weathdir)

    def selectAllWeather(self):
        self.cursor.execute("SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME FROM WEATHER")
        weathdic = self.cursor.fetchall()
        return weathdic

    def selectWeathByCity(self, city):
        self.cursor.execute("""SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME
                    FROM WEATHER
                    WHERE CITY = ?""", (city,))
        weathdic = self.cursor.fetchall()
        return weathdic

    def deleteWeatherOuttime(self):
        self.cursor.execute("""DELETE FROM WEATHER WHERE DATETIME(UPDATE_TEME) > DATETIME('now', '-10 minutes')""")

    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()



class HistoryOp(object):
    """历史数据存储表操作类"""
    def __init__(self, cursor):
        self.cursor = cursor

    def insertOneHistory(self, historydir):
        self.cursor.execute("""INSERT INTO HISTORY (CITY, WEATHER_TXT,
                    WIND_DIRECTION, TEMPERATURE, UPDATE_TIME, USER)
                    VALUES (?, ?, ?, ?, ?, ?)""",historydir)

    def selectAllHistory(self):
        self.cursor.execute("""SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME
                    FROM HISTORY""")
        hisdic = self.cursor.fetchall()
        return hisdic

    def selectHistoryByUser(self, user):
        self.cursor.execute("""SELECT CITY, WEATHER_TXT, WIND_DIRECTION, TEMPERATURE, UPDATE_TIME
                    FROM HISTORY
                    WHERE USER = ?""", (user,))
        hisdic = self.cursor.fetchall()
        return hisdic

    def deleteHistoryByUser(self, user):
        self.cursor.execute("""DELETE FROM HISTORY WHERE USER = ?""", (user,))


    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()
>>>>>>> 96f6736d69e7ab1524131eac947d5bdd565da3f0
