#!/usr/bin/env python
import csv
import sys
import decimal
import os
import os.path
import itertools as IT

#clears folder

if os.path.exists('Data2.csv'):
    os.remove('Data2.csv')

if os.path.exists('Transposed Data'):
    os.remove('Transposed Data.csv')

if os.path.exists('Project Names'):
    os.remove('Project Names.csv')

if os.path.exists('Data1'):
    os.remove('Data1.csv')

#makes csv files
    
with open('Data1.csv','w') as fp:
    a = csv.writer(fp,delimiter=',')
    data=[]
    a.writerows(data)

with open('Data2.csv','w') as fp:
    a = csv.writer(fp,delimiter=',')
    data=[]
    a.writerows(data)
    
with open('Transposed Data.csv','w') as fp:
    b = csv.writer(fp,delimiter=',')
    data=[]
    b.writerows(data)

with open('Project Names.csv','w') as fp:
    b = csv.writer(fp,delimiter=',')
    data=[]
    b.writerows(data)
    
#transfers tbl data to csv

with open('sci_mf_20083.tbl.txt','r') as infile, open('Data1.csv', 'wb') as outfile:
    in_txt = csv.reader(infile, delimiter = '\t')
    out_csv = csv.writer(open('Data1.csv', 'wb'))
    out_csv.writerows(in_txt)

#fixes glitches
    
filenames = ['Data1.csv', 'Data2.csv']
handles = [open(filename, 'rb') for filename in filenames]    
readers = [csv.reader(f, delimiter=',') for f in handles]

with  open('Project Names.csv', 'wb') as h:
    writer = csv.writer(h, delimiter=',', lineterminator='\n')
    for rows in IT.izip_longest(*readers, fillvalue=['']):
        combined_row = []
        for row in rows:
            row = row[15:25]
            combined_row.extend(row)
        writer.writerow(combined_row)

for f in handles:
    f.close()

#transposes data

from itertools import izip
a = izip(*csv.reader(open("Data1.csv", "rb")))
csv.writer(open("Transposed Data.csv", "wb")).writerows(a)

#makes rows into lists

with open('Transposed Data.csv') as f:
    transposeddatalist = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    reader = csv.reader(f)
    for row in reader:
        for col in range(2327):
            transposeddatalist[col].append(row[col])
            
with open('Data1.csv') as f:
    datalist = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    reader = csv.reader(f)
    for row in reader:
        for col in range(15):
            transposeddatalist[col].append(row[col])


            
#identify lists

            pilist = list(set(datalist [13]))
            projlist = list(set(datalist [14]))
            pinumber = len(pilist)
            projnumber = len(projlist)

#making loop

    answer = "7"
    while answer != "5":

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
                    if pichoice in datalist[13]:
                        piprojlist = []
                        for i, j in enumerate(datalist[13]):
                            if j == pichoice:
                                pidatalist = transposeddatalist[i]
                                newlist = pidatalist[14]
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
                    if projname in datalist[14]:
                        masklist = []
                        for i, j in enumerate(datalist[14]):
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
                    if projname in datalist[14]:
                        masklist = []
                        for i, j in enumerate(datalist[14]):
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


