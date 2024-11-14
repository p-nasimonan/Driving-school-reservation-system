"""
バックエンド（フロントの情報をもとに自動入力して予約する部分）

このスクリプトは、Seleniumを使用して自動的にウェブサイトにログインし、予約を行うシステムです。
主な機能として、ログイン、通常予約、キャンセル待ち予約があります。
制限事項として、Chromeドライバのパスが正しく設定されている必要があります。
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
#options.add_argument('--headless')  # ヘッドレスモードを無効にする

# Chromeドライバのパスを指定する
driver = webdriver.Chrome(options=options)

def open_web(URL):
    """
    ウェブページを開く関数
    Args:
        URL
    """
    driver.get(URL)

def login(student_id: str, password: str):
    """
    ログインを行う関数

    Args:
        student_id (str): 教習生番号
        password (str): パスワード
    """
    driver.refresh()
    # 再ログインと書かれていた場合クリックする
    try:
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, "input[value='戻る']")
        button.click()

        button = driver.find_element(By.CSS_SELECTOR, "input[value='再ログイン']")
        button.click()
    except:
        pass

    try:
        # 教習生番号を入力
        field = driver.find_element(By.NAME, 'ID')
        field.send_keys(student_id)
        # パスワードを入力
        field = driver.find_element(By.NAME, 'Pass')
        field.send_keys(password)
        # ログインボタンを押す
        login_button = driver.find_element(By.CSS_SELECTOR, "input[value='ログイン']")
        login_button.click()

        print("ログイン成功")
    except Exception as e:
        print(f"Error in login: {e}")

def reserve_time_slot(time_slot: str):
    """
    指定された時間帯のボタンをクリックする関数

    Args:
        time_slot (str): 予約したい時間帯（例: "10:40"）
    """
    row = None
    for i in range(1,13):
        try:
            # 表を取得する
            element=driver.find_element(By.XPATH, f'/html/body/p[5]/table/tbody/tr[{i}]/td[1]/p') 
            print(element.text)
            # 指定された時間帯の行を見つける
            if time_slot == element.text:
                print("行を見つけました")
                row = i
        except:
            print(f"存在しない行:{i}")

    if row == None:
        raise Exception("指定した時間が表に見つかりませんでした")
    
    try:
        print(f"{time_slot}の予約中")
        reserve_button = driver.find_element(By.XPATH, f"/html/body/p[5]/table/tbody/tr[{row}]/td[2]/div/form")
        reserve_button.click()

         # 予約を確定する
        confirm_button = driver.find_element(By.CSS_SELECTOR, "input[value='続　行']")
        confirm_button.click()

        print("予約成功")
        
    except Exception as e:
        if "no such element" in str(e):
            print(f"予約が開いていませんでした: {time_slot}")
        else:
            print(f"Error in reserve_time_slot: {e}")

def normal_reserve(student_id: str, password: str, date: str, time_slot: str):
    """
    通常予約を行う関数

    Args:
        student_id (str): 教習生番号
        password (str): パスワード
        date (str): 予約したい日付
        time_slot (str): 予約したい時間帯
    """
    try:
        # ログインする
        login(student_id, password)
        
        # 技能予約をクリック
        skill_reserve_button = driver.find_element(By.CSS_SELECTOR, "input[value='技能予約']")
        skill_reserve_button.click()
        print("予約中")

        # 予約したい日付を選択
        date_field = driver.find_element(By.CSS_SELECTOR, f"input[value='{date}']")
        date_field.click()
        print(date+"の予約を確認")
        time.sleep(1)

        # 予約したい時間を選択し予約する
        reserve_time_slot(time_slot)
       
    except Exception as e:
        print(f"Error in normal_reserve: {e}")

def cancel_time_slot(time_slot:str):
    row = None
    for i in range(1,13):
        try:
            # 表を取得する
            element=driver.find_element(By.XPATH, f'/html/body/form/p/table/tbody/tr[{i}]/td[1]/p') 
            print(element.text)
            # 指定された時間帯の行を見つける
            if time_slot == element.text:
                print("行を見つけました")
                row = i
        except:
            print(f"存在しない行:{i}")

    if row == None:
        raise Exception("指定した時間が表に見つかりませんでした")
    
    try:
        # 取得した行のボタンを押す
        print(f"{time_slot}の予約中")
        reserve_button = driver.find_element(By.XPATH, f"/html/body/form/p/table/tbody/tr[{row}]/td[2]/input")
        reserve_button.click()


        print("更新ボタンを押します")
        update_button = driver.find_element(By.CSS_SELECTOR, "input[value='＜更新＞']")
        update_button.click()

        # 何番目か知らせる
        print(f"順番／申込数／制限数:{driver.find_element(By.XPATH, f"/html/body/form/p/table/tbody/tr[{row}]/td[3]/p").text}")
    except Exception as e:
        if "no such element" in str(e):
            print(f"予約が開いていませんでした: {time_slot}")
        else:
            print(f"Error in reserve_time_slot: {e}")


def cancelmachi(student_id: str, password: str, time_slot: str):
    """
    キャンセル待ち予約を行う関数

    Args:
        student_id (str): 教習生番号
        password (str): パスワード
        time_slot (str): 予約したい時間帯
    """
    try:
        # ログインする
        login(student_id, password)
        # キャンセル待ちをクリック
        cancel_wait_button = driver.find_element(By.CSS_SELECTOR, "input[value='キャンセル待ち']")
        cancel_wait_button.click()
        # 予約したい時間を予約する
        cancel_time_slot(time_slot)

    except Exception as e:
        print(f"Error in cancelmachi: {e}")



if __name__ == '__main__':
    open_web("http://217.178.99.36/Scripts/MGrqispi015.dll?APPNAME=NK-YOYAKU&PRGNAME=login")

    cancelmachi("60354", "051231", "17:50")
