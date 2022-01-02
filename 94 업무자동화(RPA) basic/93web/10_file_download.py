import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_firectory':r'/home/cjoe731/Desktop/python(NadoCoding)/2 파이썬  활용편/무료강의(활용편4)업무자동화(RPA)basic/3web/'})

browser = webdriver.Chrome( "./chromedriver", options=chrome_options)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame('iframeResult')

# download link click
elem = browser.find_element(By.XPATH,  '/html/body/p[2]/a')
elem.click()

# /home/cjoe731/Desktop/python(NadoCoding)/2 파이썬  활용편/무료강의(활용편4)업무자동화(RPA)basic/3web
# /home/cjoe731/Desktop/python(NadoCoding)/2 파이썬  활용편/무료강의(활용편4)업무자동화(RPA)basic/3web/


time.sleep(3)
browser.quit()

