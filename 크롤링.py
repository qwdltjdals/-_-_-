from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install())) # 드라이버 객체 생성 - selenium웹드라이버 - chrome

driver.get("https://comic.naver.com/webtoon")
time.sleep(2) # 화면에 보여져야지만 데이터를 가져올 수 있음 - 아래에 있는거는 스크롤링이 되어야 가져올 수 있음!

menuList = driver.find_elements(by=By.CSS_SELECTOR, value='.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a') # =document.querySelectAll

menuNameList = []

for menu in menuList[1:8]: # 1부터 8이 되기 전까지만
    menu.click()
    menuNameList.append(menu.text)
    time.sleep(1)

    webtoonList = driver.find_elements(by=By.CSS_SELECTOR, value='.ContentList__content_list--q5KXY > .item')
    for webtoon in webtoonList:
        driver.execute_script("arguments[0].scrollIntoView(true);", webtoon) # 해당 웹툰 위치로 스크롤 이동
        time.sleep(0.2)
        posterImg = webtoon.find_element(by=By.CSS_SELECTOR, value='img')
        posterImgUrl = posterImg.get_attribute(name="src")
        print(posterImgUrl)


print(f"메뉴이름리스트: {menuNameList}")