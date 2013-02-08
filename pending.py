import sys
import csv
import string
from datetime import date
from time import strptime
import datetime
import re
import argparse

def makePendingDays(dt):
	tmp=dt.split()
	t2=tmp[0].split("/")
	day=t2[1]
	month=t2[0]
	year=t2[2]
	
	dt=datetime.date(int(year),int(month),int(day))
	today=date.today()
	return abs((today-dt).days)


def cleanupBodySite(site):
	cleansite=list()
	for ele in site:
		ele=ele.replace("Bone Marrow","")
		ele=ele.replace("Peripheral Blood","")
		ele=ele.replace("Paraffin Block","")
		ele=ele.replace(" - ","")
		cleansite.append(ele)
	return cleansite
	
def makeDateObj(datestr):
	year=datestr[0:4]
	month=datestr[4:6]
	day=datestr[6:8]
	year=int(year)
	month=int(month)
	day=int(day)
	return datetime.date(year,month,day)

filename=""
prefix=""
parser=argparse.ArgumentParser(description="pending.py get a list of pending cases by department.  ")
parser.add_argument('-f',action="store",dest="filename")
parser.add_argument('-p',action="store",dest="prefix")

result=parser.parse_args()
filename=result.filename
prefix=result.prefix

rr=csv.reader(open(filename,'rb'),delimiter=',',quotechar='\'')
rr.next()

if prefix=="M1":
	print "***Molecular*****"
if prefix=="X1":
	print "***Summation***"
if prefix=="S1":
	print "***Surgical****"
if prefix=="FH":
	print "******FISH*****"
if prefix=="FC":
	print "*****FLOW*****"

for row in rr:
	if row[1] =="" and row[0][0]==prefix[0] and row[0][1]==prefix[1]:
		if row[3] !='':
			pendingDays=makePendingDays(row[3])
		else:
			pendingDays=makePendingDays(row[2])
		if pendingDays <= 60:
			print row[0],pendingDays,cleanupBodySite(row[4:])


		
		


