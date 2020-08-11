#!/usr/bin/env python3

import time
from argparse import ArgumentParser, RawTextHelpFormatter
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

example = '''Example: 

python3 theTypingCat.py -t 1
python3 theTypingCat.py -b firefox -t 5
python3 theTypingCat.py -b chrome -t 3 -u username'''

parser = ArgumentParser(epilog=example, formatter_class=RawTextHelpFormatter)
parser.add_argument("-t", "--time", help="1, 3 or 5 for 1 minute, 3 minutes or 5 minutes test respectively")
parser.add_argument("-u", "--username", help="username for login (optional)")
parser.add_argument("-b", "--browser", help="chrome or firefox (default is chrome)")
args = parser.parse_args()

if args.time and args.username:
	if args.time != "1" and args.time != "3" and args.time != "5":
		parser.print_help()
		exit()
	if args.username:
		password = getpass("Password for "+args.username+": ")
		if args.browser and args.browser == 'firefox':
			driver = webdriver.Firefox()
			driver.maximize_window()
		else:
			options = webdriver.ChromeOptions()
			options.add_argument("--start-maximized")
			driver = webdriver.Chrome(chrome_options=options)

		driver.get('https://thetypingcat.com/sign-in')
		wait=WebDriverWait(driver,2)
		
		wait.until(EC.presence_of_element_located((By.NAME,"email")))
		user = driver.find_element_by_name('email')
		wait.until(EC.presence_of_element_located((By.NAME,"password")))
		passwd = driver.find_element_by_name('password')
		user.send_keys(args.username)
		passwd.send_keys(password)
		passwd.send_keys(Keys.RETURN)
		time.sleep(3)

		wait.until(EC.presence_of_element_located((By.CLASS_NAME,"fa.fa-tachometer.margin-right-5")))
		getTestPage1m = driver.find_element_by_class_name('fa.fa-tachometer.margin-right-5')
		getTestPage1m.click()
		time.sleep(2)

	if args.time == "3":
		# wait.until(EC.presence_of_element_located((By.CLASS_NAME,"text-notransform.btn.btn-default")))
		getTestPage3m = driver.find_elements_by_class_name('text-notransform.btn.btn-default')[0]
		getTestPage3m.click()
		time.sleep(2)
	elif args.time == "5":
		# wait.until(EC.presence_of_element_located((By.CLASS_NAME,"text-notransform.btn.btn-default")))
		getTestPage5m = driver.find_elements_by_class_name('text-notransform.btn.btn-default')[1]
		getTestPage5m.click()
		time.sleep(2)

elif args.time:
	if args.time != "1" and args.time != "3" and args.time != "5":
		parser.print_help()
		exit()
	if args.browser and args.browser == 'firefox':
		driver = webdriver.Firefox()
		driver.maximize_window()
	else:
		options = webdriver.ChromeOptions()
		options.add_argument("--start-maximized")
		driver = webdriver.Chrome(chrome_options=options)

	if args.time == "1":
		driver.get('https://thetypingcat.com/typing-speed-test/1m')
		wait=WebDriverWait(driver,2)
		wait.until(EC.presence_of_element_located((By.CLASS_NAME,"char.active")))
	elif args.time == "3":
		driver.get('https://thetypingcat.com/typing-speed-test/3m')
		wait=WebDriverWait(driver,2)
		wait.until(EC.presence_of_element_located((By.CLASS_NAME,"char.active")))
	elif args.time == "5":
		driver.get('https://thetypingcat.com/typing-speed-test/5m')
		wait=WebDriverWait(driver,2)
		wait.until(EC.presence_of_element_located((By.CLASS_NAME,"char.active")))

else:
	parser.print_help()
	exit()

while True:
	text = driver.find_element_by_class_name("char.active")
	currentChar = text.get_attribute("data-char")
	actions = ActionChains(driver)
	if currentChar == "⏎":
		actions.send_keys(Keys.RETURN)
	else:
		actions.send_keys(currentChar)
	actions.perform()
	time.sleep(0.02)

# time.sleep(30)
# driver.quit()
# driver.close()
