# Access the IPEDS database to download the CIP to SOC file that
# crosswalks the two codes.

from splinter import Browser
import requests
import time

br = Browser()
br.visit('http://nces.ed.gov/ipeds/cipcode/resources.aspx?y=55')
br.find_by_xpath('//*[@id="ctl00_ctl00_CIPContent_ContentPlaceHolder1_LinkButton_FINALCIPtoSOCcrosswalk"]').first.click()

time.sleep(5)
br.quit()
