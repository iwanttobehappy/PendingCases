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
	
def cleanList(ls):
	clean=""
	for e in ls:
		e=e.replace("NY Presbyterian Hosp. Weill Cornell Med. Ctr. MM Pgm.","Weill Cornell")
		e=e.replace("Chilton Memorial Hospital","Chilton")
		e=e.replace("Costa Rica","Roche")
		e=e.replace("Trinidad","Roche")
		e=e.replace("El Salvador","Roche")
		e=e.replace("Aruba","Roche")
		e=e.replace("Guatemala","Roche")
		e=e.replace("University of Iowa HealthcareClinical Pathology Lab","UIowa")
		e=e.replace("Georgia Health Sciences University Medical Center","Georgia Health Sciences")
		e=e.replace("Research Long Island Jewish Medical Ctr.","LIJ")
		e=e.replace("Memorial Sloan-Kettering Cancer Center","MSKCC")
		e=e.replace("Regional Cancer Care Associates","Regional Cancer Care")
		e=e.replace("Weill Cornell Medical College","Weill Cornell")
		e=e.replace("Health Network Laboratories","HNL")
		
		clean +=e+'\t'
	return clean

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
# order of fields CASE_NUMBER  DATE_REPORTED  DATE_RECEIVED STATION_ID PRACTICE BODY_SITE
if prefix=="M1":
	print "***Molecular*****"
	print "CASE"+'\t'+"days"+'\t'+"practice"+'\t'+"Test Type"
if prefix=="X1":
	print "***Summation***"
	print "CASE"+'\t'+"days"+'\t'+"practice"+'\t'+"Test Type"
if prefix=="S1":
	print "***Surgical****"
	print "CASE"+'\t'+"days"+'\t'+"practice"+'\t'+"Test Type"
if prefix=="FH":
	print "******FISH*****"
	print "CASE"+'\t'+"days"+'\t'+"practice"+'\t'+"Test Type"
if prefix=="FC":
	print "*****FLOW*****"
	print "CASE"+'\t'+"days"+'\t'+"practice"+'\t'+"Test Type"
if prefix=="CG":
	print "*****CYTO*****"
	print "CASE"+'\t'+"days"+'\t'+"practice"+'\t'+"Test Type"

for row in rr:
	if row[1] =="" and row[0][0]==prefix[0] and row[0][1]==prefix[1]:
		if row[3] !='':
			pendingDays=makePendingDays(row[3])
		else:
			pendingDays=makePendingDays(row[2])
		if pendingDays <= 60:
			print row[0]+'\t'+str(pendingDays)+'\t'+cleanList(cleanupBodySite(row[4:]))


		
		


