# Access the NCES database to download the CIP to SOC file that
# crosswalks the two codes.

from selenium import webdriver
import os
import time
import shutil
import re

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/vnd.ms-excel")

browser = webdriver.Firefox(firefox_profile=fp)
browser.get('http://nces.ed.gov/ipeds/cipcode/resources.aspx?y=55')
browser.find_element_by_xpath('//*[@id="ctl00_ctl00_CIPContent_ContentPlaceHolder1_LinkButton_FINALCIPtoSOCcrosswalk"]').click()

time.sleep(30)
browser.close()

directory = os.listdir('../Project')
list  = ', '.join(directory)
filegex = 'FINALCIPtoSOCcrosswalk_\d+.xls'
filecompile = re.compile(filegex)
filename = re.findall(filecompile,list)
file = filename[0]
shutil.move(file, 'CrosswalkData.xls')
