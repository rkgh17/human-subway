from flask import Flask
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

def db_create():
    engine = create_engine("postgres://tbbkrrtsyawpna:dfdb5f863367f9201af65c0e118c7be707d839509e9e60439d6b942ac32b826c@ec2-18-215-41-121.compute-1.amazonaws.com:5432/d8ijkeso1uk8kf", echo = False)
    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS dbsub(
            name VARCHAR(50) NOT NULL,
            subtime VARCHAR(50) NOT NULL,
            content VARCHAR(500) NOT NULL
        );"""
    )

    subdb = ['지하철사고', '2022-11-11 08:01', '서울교통공사에서 알려드립니다. 현재 4호선에서 「전국장애인차별철폐연대」의 지하철 타기 선전전이 진행되고 있습니다. 이로 인해 4호선 열차운행이 상당시간 지연될 수 있으니 이점 참고하여 열차를 이용해 주시기 바랍니다. 서울교통공사는 열차운행이 신속히 정상화될 수 있도록 최선을 다하겠습니다.']
    subdb.to_sql(name='dbsub', con=engine, schema = 'public', if_exists='replace', index=False)


app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "DB Created Done!!!"

if __name__ == "__main__":
    db_create()
    app.run()