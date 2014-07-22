# Accesses the IPEDS Data Center to download a .csv file of all Title
# IV compliant, US institutions sorted by "Awards/degrees conferred by
# program (CIP), award level, race/ethnicity, and gender: July 1, 2011
# to June 30, 2012."

from selenium import webdriver
import os
import time
from sys import exit
import re
from subprocess import call

fp = webdriver.FirefoxProfile("/home/Jonathan.Kulakofsky/.mozilla/firefox/6aixyafr.Selenium")

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")

browser = webdriver.Firefox(firefox_profile=fp)
browser.get('http://nces.ed.gov/ipeds/datacenter/LoadSession.aspx')
form = browser.find_element_by_id('tbJobNumberToLoad')
form.send_keys('Guest_24322988597')
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
    time.sleep(180)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "CIP_Codes2012.csv"])
    
    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2012"]/div[3]/div[2]/div[1]/a').click()
    time.sleep(30)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "Sector2012.csv"])
    
    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2011"]/div[2]/div[2]/div[1]/a').click()
    time.sleep(180)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "CIP_Codes2011.csv"])
    
    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2011"]/div[3]/div[2]/div[1]/a').click()
    time.sleep(30)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "Sector2011.csv"])
    
    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2010"]/div[2]/div[2]/div[1]/a').click()
    time.sleep(220)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "CIP_Codes2010.csv"])
    
    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2010"]/div[3]/div[2]/div[1]/a').click()
    time.sleep(30)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "Sector2010.csv"])
    
    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2009"]/div[2]/div[2]/div[1]/a').click()
    time.sleep(220)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "CIP_Codes2009.csv"])
    
    browser.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_divAllVariablesPerYear2009"]/div[3]/div[2]/div[1]/a').click()
    time.sleep(30)
    directory = os.listdir('../Project')
    list = ', '.join(directory)
    zipgex = 'CSV_\d+-\d*.zip'
    zipcompile = re.compile(zipgex)
    zipname = re.findall(zipcompile,list)
    zip = zipname[0]
    call(["unzip", zip])
    call(["rm", zip])
    
    directory2 = os.listdir('../Project')
    list2 = ', '.join(directory2)
    htmlgex = 'CSV_\d+-\d*.html'
    htmlcompile = re.compile(htmlgex)
    htmlname = re.findall(htmlcompile,list2)
    html = htmlname[0]
    call(["rm", html])
    filegex = 'CSV_\d+-\d*.csv'
    filecompile = re.compile(filegex)
    filename = re.findall(filecompile,list2)
    file = filename[0]
    call(["mv", file, "Sector2009.csv"])

words = browser.page_source

if "In order to get a custom data set, select data to include" in words:
    variables()
elif "Completions, awards and degrees by 6-digit cipcode" in words:
    download()
else:
    print "Everything is ruined, nothing is what it seems, and your program is broken."
    browser.close()
    exit(0)

browser.close()
