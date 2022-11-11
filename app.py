# -*- coding: utf-8 -*-

from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


# 1단계 : 코드 수정
# 2단계 : 스킬 등록 (URL)
# 3단계 : 시나리오에서 등록한 스킬 호출
# 4단계 : 배포

## 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody

## 카카오톡 이미지형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody
















## 카카오톡 텍스트형 응답
@app.route('/api/saysubway', methods=['POST'])
def saysubway():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    url = 'C:/Users/h/Desktop/chatbot/'
    driver = webdriver.Chrome(url + 'chromedriver.exe')
    time.sleep(0.5)
    driver.get("https://safecity.seoul.go.kr/acdnt/sbwyIndex.do")
    time.sleep(0.5)

    parentElement = driver.find_elements(By.XPATH, '//*[@id="dv_as_timeline"]/li')
    subli=[]
    # ul 태그 아래 있는 li 반복 뽑기
    for i in parentElement:
        i.click()
        time.sleep(0.05)
        a = i.text
        subli.append(a)
        i.click()


    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": subli[0] + subli[1]
                    }
                }
            ]
        }
    }
    driver.close()
    return responseBody