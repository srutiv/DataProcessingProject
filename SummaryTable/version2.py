#!/usr/bin/python

#generates table with url grab

#1.open up ascii file from keck archive
#2. copy url of ascii file
#3. run program
#-input ascii url
#-write to txt file
#-remove whitespace in txt
#remove garbage lines by using the search 'MF.[0-9]' if match, then proceeed to append
#-run the line by line/appending/create summary table thing to new tbl only       
#creates summary table

#https://koa.ipac.caltech.edu/workspace/TMP_3sQjGw_24687/KOA/sci_mf_9200.tbl

import sys
import urllib2
import re


def grab_from_web():
    url_paste = raw_input("URL of ASCII file ->")
    f = urllib2.urlopen(url_paste)
    f2 = open('x.txt', 'w')
    l = f.read()
    f2.write(l)
    f2.close()


def remove_whitespace():
    with open('x.txt') as p:
       lines = p.readlines()
       for line in lines:
          re.sub(r'\s\s+', " ", line)
    p.close()
    

def grab_filter(file_name):
     with open(file_name) as f:
       lines = f.readlines()
       for line in lines:
           x = line.split() 
           if "MF2NAME" in x:
             return x[2]
     f.close()
     

def create_table():
    grab_from_web()
    remove_whitespace()
    print "PI--ProjectName--Mask/TargetName--Filter--ExposureTime(sec)--FileName"
    with open('x.txt') as f:
        lines = f.readlines()
        for line in lines:
           match_data = re.search(r'MF', line)
           if match_data:
              col = line.split()
              x = []
              project_name = ""
              for i in range (14,25):
                 x.append(col[i])
              for item in x:
                 project_name += str(item) + " "
              pi = col[13]
              mask = col[2]
              file_name = col[0]
              exposure_time = col[9]
              filter = grab_filter(file_name)
              print pi, project_name, mask, filter, exposure_time, file_name
    f.close()
    
    
if __name__== "__main__":

  create_table()