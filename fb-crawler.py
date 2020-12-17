from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

# 關閉通知
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'notifications': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars") 

# 打啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

#輸入email 
context = driver.find_element_by_css_selector('#email')
context.send_keys('qlixilp@yahoo.com.tw') 

#輸入password
context = driver.find_element_by_css_selector('#pass')
context.send_keys('Kevin3466')

commit = driver.find_element_by_css_selector('button[type=''submit'']').click()
time.sleep(3)
spec_url = "https://www.facebook.com/groups/NTU.Head"
driver.get(spec_url)

for x in range(2):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    
    
k = len(driver.find_elements_by_xpath('//div/div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]'))
print(k)
for i in range(k):
    ha = driver.find_element_by_xpath('//div/div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')
    try :
        driver.execute_script('arguments[0].click();',ha)
    except:
        pass
    time.sleep(0.5)

# soup = BeautifulSoup(driver.page_source, 'html.parser')
soup = BeautifulSoup(driver.page_source, 'lxml')





# titles = soup.find_all('span',class_ ="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa fgxwclzu a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m")

titles = soup.find_all('div',id = re.compile('^jsc'))
# titles1 = titles.find_all_next('div',class_='')

links = soup.find_all('a',{'class':"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"})

# 失敗中
# link = driver.find_elements_by_css_selector('span span[class="tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"] a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')
# for i in link:
#     print('網址3：'+ i.get_attribute('href'))



for i in titles:
    print(i)

# for i in titles:
#     print('內容1：'+ i.text)

# links1 = soup.find_all('a',attrs = {'class':'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw','href':re.compile('^https://www.facebook.com/groups/NTU.Head/permalink')})
# links2 = soup.find_all('a')
    
# for i in links:
#     print('網址：' + i.get('href'))
    
# for i in links1:
#     print('網址1：' + i.get('href'))
#     print(type(i.get('href')))
#     print(type(i))
    
# for i in links2:
#     e = 'https://www.facebook.com/groups/NTU.Head/permalink'
#     a = '網址2：' + i.get('href')
#     if e not in a:
#         pass
#     else:
#         print(a)