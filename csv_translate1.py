from sys import argv
import csv
import re

script, fn1, fn2, fn3, fn4, fn5, fn6, fn7, fn8 = argv

ifile1 = open(fn1, "rb")
reader1 = csv.reader(ifile1)
ofile1 = open('temp1.csv', "wb")
writer1 = csv.writer(ofile1, delimiter='|')

ifile2 = open(fn2, "rb")
reader2 = csv.reader(ifile2)
ofile2 = open('temp2.csv', "wb")
writer2 = csv.writer(ofile2, delimiter='|')

ifile3 = open(fn3, "rb")
reader3 = csv.reader(ifile3)
ofile3 = open('temp3.csv', "wb")
writer3 = csv.writer(ofile3, delimiter='|')

ifile4 = open(fn4, "rb")
reader4 = csv.reader(ifile4)
ofile4 = open('temp4.csv', "wb")
writer4 = csv.writer(ofile4, delimiter='|')

ifile5 = open(fn5, "rb")
reader5 = csv.reader(ifile5)
ofile5 = open('temp5.csv', "wb")
writer5 = csv.writer(ofile5, delimiter='|')

ifile6 = open(fn6, "rb")
reader6 = csv.reader(ifile6)
ofile6 = open('temp6.csv', "wb")
writer6 = csv.writer(ofile6, delimiter='|')

ifile7 = open(fn7, "rb")
reader7 = csv.reader(ifile7)
ofile7 = open('temp7.csv', "wb")
writer7 = csv.writer(ofile7, delimiter='|')

ifile8 = open(fn8, "rb")
reader8 = csv.reader(ifile8)
ofile8 = open('temp8.csv', "wb")
writer8 = csv.writer(ofile8, delimiter='|')

for row in reader1:
        writer1.writerow(row)

for row in reader2:
        writer2.writerow(row)

for row in reader3:
        writer3.writerow(row)

for row in reader4:
        writer4.writerow(row)

for row in reader5:
        writer5.writerow(row)

for row in reader6:
        writer6.writerow(row)

for row in reader7:
        writer7.writerow(row)

for row in reader8:
        writer8.writerow(row)

ifile1.close()
ofile1.close()

ifile2.close()
ofile2.close()

ifile3.close()
ofile3.close()

ifile4.close()
ofile4.close()

ifile5.close()
ofile5.close()

ifile6.close()
ofile6.close()

ifile7.close()
ofile7.close()

ifile8.close()
ofile8.close()
