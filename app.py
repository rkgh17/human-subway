# -*- coding: utf-8 -*-
from flask import Flask
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local
def db_create():
	# Heroku
    engine = create_engine("postgresql://your_url", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS iris(
            id int NOT NULL,
            sepal_length FLOAT NOT NULL,
            sepal_width FLOAT NOT NULL,
            pepal_length FLOAT NOT NULL,
            pepal_width FLOAT NOT NULL,
            species VARCHAR(100) NOT NULL
        );"""
    )
    data = pd.read_csv('data/iris.csv')
    print(data)
    data.to_sql(name='iris', con=engine, schema = 'public', if_exists='replace', index=False)

application = Flask(__name__)

@application.route("/")
def index():
    # db_create()
    return "DB Created Done!!!"

if __name__ == "__main__":
    db_create()
    application.run()