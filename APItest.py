import pymysql,keys
from flask import Flask

conn=pymysql.connect(
    user = keys.USER, #str
    passwd = keys.PW, #str
    host = keys.HOST, #str
    db = keys.DB, #str
    port = keys.PORT, #int
)

cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    select = "select * from schedule order by year , month , day"
    cursor.execute(select)
    rows = cursor.fetchall()
    ms = ""
    if (len(rows) == 0):
        return "予定はありません"
    
    for row in rows:
        s = str(row).strip("(")
        sche = s.strip(")")
        schedule = sche.split(",",4)
        content = schedule[4].split("'",10)
        ms = ms + str(schedule[1]) + "年" + str(schedule[2]) + "月" + str(schedule[3]) + "日：" + str(content[1]) + "\n"
    return ms

if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost",port=5001)