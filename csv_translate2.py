from sys import argv
import re
import unicodecsv

script, filename = argv

csvfile = "CIP_Codes.csv"

txt = open(filename)
red = txt.read()
reed = re.sub('["]', '', red)
reid = re.sub("[']", '', reed)
rad = re.sub('A\.', '', reid)
road = re.sub('C2012_', '', rad)
with open(csvfile, "w") as output:
	output.write(road)
