from sys import argv
import csv
import re

script, filename = argv

ifile = open(filename, "rb")
reader = csv.reader(ifile)
ofile = open('temp.csv', "wb")
writer = csv.writer(ofile, delimiter='|')

for row in reader:
	writer.writerow(row)

ifile.close()
ofile.close()
