from sys import argv
import re
import unicodecsv

script, fn1, fn2, fn3, fn4, fn5, fn6, fn7, fn8 = argv

txt1 = open(fn1)
red1 = txt1.read()
reid1 = re.sub("[']", '', red1)
rad1 = re.sub('\|[A-Z]+\d+\w*?\.', '|', reid1)
with open("CIP_Codes2012.csv", "w") as output:
        output.write(rad1)

txt2 = open(fn2)
red2 = txt2.read()
reid2 = re.sub("[']", '', red2)
rad2 = re.sub('\|[A-Z]+\d+.*?\.', '|', reid2)
with open("Sector2012.csv", "w") as output:
        output.write(rad2)

txt3 = open(fn3)
red3 = txt3.read()
reid3 = re.sub("[']", '', red3)
rad3 = re.sub('\|[A-Z]+\d+.*?\.', '|', reid3)
with open("CIP_Codes2011.csv", "w") as output:
        output.write(rad3)

txt4 = open(fn4)
red4 = txt4.read()
reid4 = re.sub("[']", '', red4)
rad4 = re.sub('\|[A-Z]+\d+.*?\.', '|', reid4)
with open("Sector2011.csv", "w") as output:
        output.write(rad4)

txt5 = open(fn5)
red5 = txt5.read()
reid5 = re.sub("[']", '', red5)
rad5 = re.sub('\|[A-Z]+\d+.*?\.', '|', reid5)
with open("CIP_Codes2010.csv", "w") as output:
        output.write(rad5)

txt6 = open(fn6)
red6 = txt6.read()
reid6 = re.sub("[']", '', red6)
rad6 = re.sub('\|[A-Z]+\d+.*?\.', '|', reid6)
with open("Sector2010.csv", "w") as output:
        output.write(rad6)

txt7 = open(fn7)
red7 = txt7.read()
reid7 = re.sub("[']", '', red7)
rad7 = re.sub('\|[A-Z]+\d+.*?\.', '|', reid7)
with open("CIP_Codes2009.csv", "w") as output:
        output.write(rad7)

txt8 = open(fn8)
red8 = txt8.read()
reid8 = re.sub("[']", '', red8)
rad8 = re.sub('\|[A-Z]+\d+.*?\.', '|', reid8)
with open("Sector2009.csv", "w") as output:
        output.write(rad8)
