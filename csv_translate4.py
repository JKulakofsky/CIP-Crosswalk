from sys import argv
import re
import unicodecsv

script, filename = argv

txt = open(filename)
red = txt.read()
reed = re.sub('["]', '', red)
reid = re.sub("[']", '', reed)
rad = re.sub(r'C2012_A\.', '', reid)
with open("CIP_Codes.csv", "w") as output:
        output.write(rad)
