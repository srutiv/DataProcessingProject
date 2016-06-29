#!/usr/bin/env python
import csv
import sys
import decimal
import os
import os.path
import itertools as IT
#from astropy.io import ascii
#import numpy as np

#clears folder

if os.path.exists('Transposed Data.csv'):
    os.remove('Transposed Data.csv')

if os.path.exists('Data1.csv'):
    os.remove('Data1.csv')

#makes csv files
    
with open('Data1.csv','w') as fp:
    a = csv.writer(fp,delimiter=',')
    data=[]
    a.writerows(data)

with open('Transposed Data.csv','w') as fp:
    b = csv.writer(fp,delimiter=',')
    data=[]
    b.writerows(data)
    
#transfers tbl data to csv

with open('sci_mf_20083.tbl.txt','r') as infile, open('Data1.csv', 'wb') as outfile:
    in_txt = csv.reader(infile, delimiter = '\t')
    out_csv = csv.writer(open('Data1.csv', 'wb'))
    out_csv.writerows(in_txt)

#transposes data

from itertools import izip
a = izip(*csv.reader(open("Data1.csv", "rb")))
csv.writer(open("Transposed Data.csv", "wb")).writerows(a)

#makes rows into lists

with open('Data1.csv',"r") as fj:
    reader = csv.reader(fj,delimiter = ",")
    data = list(reader)
    row_count = len(data)
    bracknum = row_count + int('1')

with open('Transposed Data.csv') as f:
    transposeddatalist = [[None]] * bracknum
    reader = csv.reader(f)
    for row in reader:
        for col in range(row_count):
            transposeddatalist[col].append(row[col])
            
with open('Transposed Data.csv',"r") as fk:
    reader = csv.reader(fk,delimiter = ",")
    data = list(reader)
    row_count1 = len(data)
    bracknum1 = row_count1 + int('1')

with open('Data1.csv') as fw:
    datalist = [[None]] * bracknum1
    reader = csv.reader(fw)
    for row in reader:
        for col in range(row_count1):
            datalist[col].append(row[col])
            
#identify lists

#cleans up pilist

print datalist[20]            
pilist = list(set(datalist [14]))
pilist[:] = (elem[:13] for elem in pilist)
pilist = [x.strip('\t') for x in pilist]
realpilist = [x.strip(' ') for x in pilist]
pilist = [s for s in realpilist if len(s) > 2]
pilist = [s for s in pilist if '|' not in s]

#making loop

number = "6"
while number != "5":

#options

    answer = raw_input('Press 1 for information about PIs, Press 2 for information about projects, Press 5 to quit: ')

#PI Info

    if answer == "1":   
        pianswer = raw_input('Press 1 for a list of PIs, Press 2 for the number of PIs, Press 5 to quit: ')
        if pianswer == '1':
            print pilist
            listorquit = raw_input('Press 1 for a list of the projects under a certain PI, Press 5 to quit: ')
            if listorquit == "1":
                pichoice = raw_input('Enter the name of the PI whose projects you want listed: ')
                if pichoice in realpilist:
                    piprojlist = []
                    for i, j in enumerate(projlist):
                        if j == pichoice: 
                           pidatalist = projectnamecol[i]
                           newlist = pidatalist[15]
                           piprojlist.append(newlist)
                    uniquelist = list(set(piprojlist))
                    print uniquelist
                    numorquit = raw_input('Press 1 for the number of projects under this PI, Press 5 to quit: ')
                    if numorquit == "1":
                        print len(uniquelist)
                    elif numorquit == "5":
                        sys.exit()
                else:
                    print('That PI is not part of this database. Please try again')
            if listorquit == "5":
                sys.exit()
        elif pianswer == '2':
            pinumber = len(pilist)
            print pinumber
        elif pianswer == "5":
            sys.exit()

#Project Info             

    elif answer == "2":
        projanswer = raw_input('Press 1 for a list of projects, Press 2 for the number of projects, Press 5 to quit: ')
        if projanswer == "1":
            print projlist
            maskanswer = raw_input('For the masks used in a project, Press 1. For the total exposure of a project, Press 2. For the number of nights assigned to a project, Press 3. To quit, Press 5: ')
            if maskanswer == "1":
                projname = raw_input('Enter the name of the project of which you want the masks used listed: ')
                if projname in projlist:
                    masklist = []
                    for i, j in enumerate(projlist):
                        if j == projname:
                            plist = transposeddatalist[i]
                            newlist = plist[2]
                            masklist.append(newlist)
                        uniquelist = list(set(masklist))
                        print uniquelist
                        numorquit = raw_input('For the number of masks used, Press 1. To quit, Press 5: ')
                        if numorquit == "1":
                            print len(uniquelist)
                            sys.exit()
                        elif numorquit == "5":
                            sys.exit()
                    else:
                        print('That project is not part of this database. Please try again')
            elif maskanswer == "2":  #total exposure time(elapsed time) on each mask(target name)
                targetname = raw_input('Enter the name of the specific mask(target name) of which you want to know the total exposure time: ')
                with open('Data.txt') as f: #use data from txt file
                    lines = f.readlines()
                    totaltimes = []
                    for line in lines:
                      if targetname in line:
                          totaltimes.append(line.split()[11]) #append value from elapsedtime/exposuretime collumn (index 11)
                f.close()
                totaltimesfloat = [] #convert items in totaltimes list from strings to floats
                for item in totaltimes:
                   totaltimesfloat.append(float(item))
                print sum(totaltimesfloat), "seconds"
            elif maskanswer == "3":
                projname = raw_input('Enter the name of the project of which you want the to know the number of nights assigned: ')
                if projname in projlist:
                    masklist = []
                    for i, j in enumerate(projlist):
                        if j == projname:
                            plist = transposeddatalist[i]
                            newlist = plist[7]
                            masklist.append(newlist)
                        uniquelist = list(set(masklist))
                    print len(uniquelist)
                else:
                    print('That project is not part of this database. Please try again')
            elif maskanswer == "5":
                sys.exit()
        elif projanswer == "2":
            print projnumber
        elif projanswer == "5":
            sys.exit()

        

#exit loop           

    elif answer == "5":
        sys.exit()

fs.close()
