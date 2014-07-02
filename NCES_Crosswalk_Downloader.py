# Access the IPEDS database to download the CIP to SOC file that
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

time.sleep(10)
browser.close()

filename = re.compile('Final.+_.+.xls')
shutil.move(filename, '../Tutorials/CrosswalkData.xls')
