# Accesses the IPEDS Data Center to download a .csv file of all Title
# IV compliant, US institutions sorted by "Awards/degrees conferred by
# program (CIP), award level, race/ethnicity, and gender: July 1, 2011
# to June 30, 2012."

from sys import exit
from splinter import Browser
import time

br = Browser()
br.visit('http://nces.ed.gov/ipeds/datacenter/LoadSession.aspx')
br.fill('tbJobNumberToLoad', 'Guest_83245948923')
button = br.find_by_name('ibtnLoadJobNumber')
button.click()
br.click_link_by_partial_href('CDSPreview.aspx?stepId=4')

def variables():
    """Selects the proper fields to generate the download data"""

    br.find_by_id('divSurveytitle3').click()
    br.find_by_id('divFileTitle4').click()
    br.click_link_by_partial_href('javascript:void(0)')
    br.find_by_id('imgContinueButton').click()
    download()

def download():
    """Downloads the .csv file"""

    br.click_link_by_partial_href('CDSFinal.aspx?year=2012&surveyNumber=3&fileNumber=4&sectionNumber=1&qv1=&qv2=&qv3=&command=csv')
    exit(0)

if "In order to get a custom data set, select data to include" in page:
    variables()
elif "Completions, awards and degrees by 6-digit cipcode" in page:
    download()
else:
    print "Everything is ruined, nothing is what it seems, and your program is broken."

time.sleep(5)
br.quit()
