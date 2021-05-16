# https://www.naver.com/
# 입력한 검색어와 관련된 기사 탐색 크롤러

import time
import selenium
from selenium import webdriver

print('관련 기사를 찾아드립니다! 검색어를 입력하세요.')
keyword = input('>> : ')

URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
driver = webdriver.Chrome(executable_path='C:/Users/USER/PycharmProjects/chromedriver.exe')
driver.get(url=URL)

search_box = driver.find_element_by_name('query')
search_box.send_keys(keyword)
search_btn = driver.find_element_by_class_name("bt_search")
search_btn.click()

news_list = driver.find_elements_by_class_name('news_tit')

for title in news_list:
    print(title.text)

print('')
second = int(input('몇 초 간 기사 화면을 탐색하시겠습니까? '))

for link in news_list:
    link.click()
    time.sleep(second) # 기사 화면을 사용자가 입력한 시간 동안 보여준다

    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

driver.close()