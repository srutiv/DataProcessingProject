#!/usr/bin/python

"""https://koa.ipac.caltech.edu/workspace/TMP_3sQjGw_24687/KOA/sci_mf_9200.tbl """

import sys
import urllib2
import re

#1.open up ascii file from keck archive
#2. copy url of ascii file
#3. run program
#-input ascii url
#-write ascii file to x.tbl
#-remove whitespace in tbl
#-write x.tbl into a new tbl
#remove garbage lines by using the search 'MF.[0-9]' if match, then proceeed to append
#garbage lines will not match
#-run the line by line/appending/create summary table thing to new tbl only       
#-write new tbl to csv [optional]
#-remove whitespace from x.csv
#create summary table


def grab_from_web():
    f = urllib2.urlopen("https://koa.ipac.caltech.edu/workspace/TMP_3sQjGw_24687/KOA/sci_mf_9200.tbl")
    f2 = open('x.txt', 'w')
    l = f.read()
    f2.write(l)
    f2.close()
    print "reached point 1"

def remove_whitespace():
    with open('x.txt') as p:
       lines = p.readlines()
       for line in lines:
          re.sub(r'\s+', "!", line)
    p.close()
    print "reached point 3"

def grab_filter(file_name):
     with open(file_name) as f:
       lines = f.readlines()
       for line in lines:
           x = line.split() 
           if "MF2NAME" in x:
             return x[2]
     f.close()          

# problem :remove whitespace is not working -> grabs wrong collumn
#fix the splits and delimiters

def create_table():
    grab_from_web()
    print "reached point 2"
    remove_whitespace()
    print "reached point 4"
    with open('x.txt') as f:
        lines = f.readlines()
        for line in lines:
           match_data = re.search(r'MF', line)
           if match_data:
              print "reached point 5"
              col = line.split(" ")
              pi = col[13]
              project_name = col[14]
              mask = col[2]
              file_name = col[0]
              exposure_time = col[9]
              filter = grab_filter(file_name)
              print pi, project_name, mask, filter, exposure_time, file_name
           else:
              print "failed"
    f.close()
    
    
if __name__== "__main__":

  create_table()
