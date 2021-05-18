# https://www.naver.com/
# 입력한 검색어와 관련된 기사 탐색 크롤러

import time
import selenium
from selenium import webdriver
import matplotlib
import matplotlib.pyplot as plt

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

title_list = []
index = 0
for title in news_list:
    index += 1
    title_list.append(title.text)
    print('(%d) ' %index + title.text)

matplotlib.rcParams["font.size"]=14
plt.rc('font', family='Malgun Gothic')

x = list(range(1,11))
y = [10,9,8,7,6,5,4,3,2,1]
plt.bar(x, y, color='b', label='관련도')
plt.title('검색어 관련 10개 기사의 관련도')
plt.legend(loc='upper right')
plt.xlabel('검색어 관련 10개 기사 제목')
plt.ylabel('관련도(상대적)')

plt.show() # 그래프 창 닫기를 해주셔야 다음 단계가 진행됩니다

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