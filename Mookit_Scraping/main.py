from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

def convert_to_pretty(name):
    name = name.text.split()
    name = "".join(str(i) for i in name)

    return name

# login_url = ('https://hello.iitk.ac.in/user/login')
# secure_url = ('https://hello.iitk.ac.in/user/27771')

# payload = {
#     'name': 'udvasb20',
#     'pass': 'Kiit@20',
#     'form_build_id': 'form-CHTzlYgjdgsOObKV1A7qFzrRxkKiKmjBs2Oz3cimerM',  
#     'form_id': 'user_login_form',
#     'op': 'SIGN IN'
# }

# html_text = requests.post(login_url, data=payload)
# print(html_text.text)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://hello.iitk.ac.in/user/login')


name_box = driver.find_element(by=By.NAME, value='name')
name_box.send_keys('udvasb20')
pass_box = driver.find_element(by=By.NAME, value='pass')
pass_box.send_keys('Kiit@20')
submit = driver.find_element(by=By.NAME, value='op')
submit.click()

course_button = driver.find_element(by=By.PARTIAL_LINK_TEXT,value='Dr. Kamal Poddar, Dr. Rajesh Kitey')
course_button.click()

access_course = driver.find_element(by=By.ID, value='edit-access-course')
access_course.click()

page = driver.page_source.encode('utf-8')
soup = BeautifulSoup(page,'lxml')
weekwises = soup.find_all('div',  class_=False, id_=None)
for weekwise in weekwises:
    week_no = weekwise.find('div', class_='weekWrapper')
    bullets = weekwise.find_all('li', class_=False)
    for bullet in bullets:
        bullet_name = bullet.find('span', class_="weekListItemTitle")
        lecture_items = bullet.find_all('div', class_="lectureItem")
        for lecture_item in lecture_items:
            lecture_name = lecture_item.find('div', class_="lectureInfoBoxText")
            lecture_time = lecture_item.find('div', class_="lectureInfoBoxLength")
            bullet_name = convert_to_pretty(bullet_name)
            lecture_name = convert_to_pretty(lecture_name)
            lecture_time = convert_to_pretty(lecture_time)
            print(bullet_name,week_no.text,lecture_name,lecture_item)
   

print("Success!")
