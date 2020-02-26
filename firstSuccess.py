#!/usr/bin/env python3

import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://thetypingcat.com/typing-speed-test/1m')
assert "Typing Test" in driver.title
time.sleep(3)

# text = driver.find_element_by_class_name("screen-display ")
# text = driver.find_element_by_class_name("line.active")
# text = driver.find_element_by_class_name("char.active")
# text = driver.find_element_by_class_name("word")
# currentWord = text.get_attribute("data-word")
# print(text.get_attribute("data-char"))
# time.sleep(2)

while True:
	text = driver.find_element_by_class_name("char.active")
	currentChar = text.get_attribute("data-char")
	print(currentChar)
	actions = ActionChains(driver)
	if currentChar == "⏎":
		actions.send_keys(Keys.RETURN)
	else:
		actions.send_keys(currentChar)
	actions.perform()
	# time.sleep(0.016)
	time.sleep(0.02)




time.sleep(15)

driver.quit()
driver.close()



# wait=WebDriverWait(browser,10)
# wait.until(EC.presence_of_element_located((By.ID,"content")))
