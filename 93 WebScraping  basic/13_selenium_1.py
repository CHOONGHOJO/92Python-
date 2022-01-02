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