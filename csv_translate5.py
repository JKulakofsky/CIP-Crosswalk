from sys import argv
import re
from subprocess import call

script, filename = argv

txt = open(filename)
red = txt.read()
reed = re.sub('["]', '', red)
reid = re.sub("[']", '', reed)
rad = re.sub('=', '', reid)
with open("Crosswalk2000-2010.csv", "w") as output:
        output.write(rad)

call(["rm", "Crosswalk2000to2010.csv"])
