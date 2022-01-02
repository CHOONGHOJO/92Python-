from selenium import webdriver
# browser = webdriver.Chrome("c:/Downloads/chromedriver.exe")
# browser = webdriver.Chrome("/home/cjoe731/Desktop/python(NadoCoding)/무료강의(활용편3:WebScraping) basic/chromedriver")
# browser = webdriver.Chrome("./chromedriver")
browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()
elem = browser.find_element_by_id("query")
elem
from selenium.webdriver.common.keys import Keys
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_tag_name("a")
elem

elem = browser.find_elements_by_tag_name("a")
elem

for e in elem:
  e.get_attribute("href")

########################################
browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.back()
elem.send_keys("나도코딩")
elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
elem = browser.find_element_by_xpath("//*[@id='daumBtnSearch'/html/body/article/header/div[1]/form/fieldset/div[1]/div/button[2]")
elem.click()
# browser.close()
browser.quit()
exit()