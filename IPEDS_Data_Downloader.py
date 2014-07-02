# Accesses the IPEDS Data Center to download a .csv file of all Title
# IV compliant, US institutions sorted by "Awards/degrees conferred by
# program (CIP), award level, race/ethnicity, and gender: July 1, 2011
# to June 30, 2012."

from selenium import webdriver
from os import getcwd
import time

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/vnd.ms-excel")

browser = webdriver.Firefox(firefox_profile=fp)

browser.get('http://nces.ed.gov/ipeds/datacenter/LoadSession.aspx')
form = browser.find_element_by_id('tbJobNumberToLoad')
form.send_keys('Guest_83245948923')
browser.find_element_by_name('ibtnLoadJobNumber').click()
browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divInstructions"]/table/tbody/tr/td[2]/a/img').click()

def variables():
    """Selects the proper fields to generate the download data"""

    browser.find_element_by_id('divSurveytitle3').click()
    browser.find_element_by_id('divFileTitle4').click()
    browser.find_element_by_xpath('//*[@id="divSection1_4_Variables"]/div[4]/div[2]/div[1]/a[1]').click()
    browser.find_element_by_id('imgContinueButton').click()
    download()

def download():
    """Downloads the .csv file"""

    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2012"]/div[2]/div[2]/div[1]/a').click()

words =  browser.page_source

if "In order to get a custom data set, select data to include" in words:
    variables()
elif "Completions, awards and degrees by 6-digit cipcode" in words:
    download()
else:
    print "Everything is ruined, nothing is what it seems, and your program is broken."

time.sleep(150)
browser.close()
