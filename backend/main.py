"""
バックエンド（自動入力して予約する部分）
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import flask
import sys
import time

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # ヘッドレスモードを無効にする

# Chromeドライバのパスを指定する
driver = webdriver.Chrome(options=options)



def reserve():
    # Webページを開く
    driver.get("http://217.178.99.36/Scripts/MGrqispi015.dll?APPNAME=NK-YOYAKU&PRGNAME=login")
    
    # 教習生番号

    # ＠パスワード