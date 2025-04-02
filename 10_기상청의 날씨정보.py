# import requests
# from bs4 import BeatifulSoup

# url = 'https://www.weather.go.kr/w/index.do'
# weather_info = requests.get(url)
# soup = BeautifulSoup(weather_info.text, 'html.parser')
# # #current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-1 > li.w-icon.w-temp.no-w > span.tmp
# print(soup.select('span.tmp').text)

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.weather.go.kr/w/index.do'

chrome_option = Options()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url)

# 암시적 대기
# 암시적 대기는 전역적으로 설정되어, 이후의 모든 find_element()와 find_elements()에 적용
# driver.implicitly_wait(5)
# tmp_element = driver.find_element(by=By.CSS_SELECTOR, value='span.tmp')

# 명시적 대기
# 특정 요소에 대해서만 대기 조건을 설정하고, 그 요소에 대해서만 기다림
wait = WebDriverWait(driver, 10)
tmp_element = wait.until(
    EC.presence_of_element_located(By.CSS_SELECTOR, value='span.tmp')
)

print(tmp_element.text)
