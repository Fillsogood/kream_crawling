from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

import pymysql

# 데이터 베이스 연결
conn = pymysql.connect(
    host = 'localhost',
    user='root',
    password = '0000',
    db='kream',
    charset = 'utf8mb4',
    # cursorclass = pymysql.cursors.DictCursor
)

conn.cursor()

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User-Agent={user}")
options_.add_experimental_option("detach",True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])
options_.add_argument("--window-size=1000,4500")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options_)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(0.5)

#인기수 클릭 및 발매일수 클릭 함수
def click_p_r():
    #인기순 클릭
    driver.find_element(By.CSS_SELECTOR,".sorting_title").click()
    time.sleep(0.5)
    #발매일순 클릭
    driver.find_elements(By.CSS_SELECTOR,".sorting_list")[0].find_elements(By.CSS_SELECTOR,".sorting_item")[9].click()

# 쿼리문 실행 함수
def execute_query(conn,query,args=None):
    with conn.cursor() as cursor:
        cursor.execute(query,args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:   
            conn.commit()            

#페이지 다운 함수
def key_down_reload():
    for i in range(5):
        driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

#클래스명이 바뀌어있는지 체크 함수
def class_c(items):
    if items:
        info_items = items
    else:
        print("클래스명 확인해주세여")


#shop 클릭
driver.find_elements(By.CSS_SELECTOR,".gnb_list")[0].find_elements(By.CSS_SELECTOR,".gnb_item")[2].click()

time.sleep(2)

#모든 카테고리
cat_shell =driver.find_elements(By.CLASS_NAME,"li_tab ")

#각 카테고리 마다 들어가서 데이터 긁어와서 DB에 저장
for i in cat_shell:
    #각 카테고리 클릭
    i.find_element(By.CSS_SELECTOR,".tab_name").click()
    time.sleep(1)
    category = i.find_element(By.CSS_SELECTOR,".tab_name").text
    #카테고리 전체 및 럭셔리 건너 뛰고 시작
    if category != "전체" and category != "럭셔리": 
        click_p_r()
        time.sleep(1)
        key_down_reload()
        html = driver.page_source
        soup = BeautifulSoup(html,"html.parser")
        items = soup.select(".item_inner")
        for j in items:
            product_brand = j.select_one(".product_info_brand.brand").text #str형
            product_name = j.select_one(".translated_name").text #str형
            product_price = j.select_one(".amount").text.split(" ")[1] #str형 공백 제거
            execute_query(conn,"INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (category,product_brand,product_name,product_price))
conn.close()          
driver.quit()
    


