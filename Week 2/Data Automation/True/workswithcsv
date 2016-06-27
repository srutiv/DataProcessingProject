#!/usr/bin/python

import csv
import sys


def grab_filter(file_name):
     with open(file_name) as f:
       lines = f.readlines()
       for line in lines:
           x = line.split() 
           if "MF2NAME" in x:
             return x[2]
     f.close()
            

def create_table():
    with open("Data.csv") as f:
        lines = f.readlines()
        for line in lines:
            col = line.split(",")
            pi = col[13]
            project_name = col[14]
            mask = col[2]
            file_name = col[0]
            exposure_time = col[9]
            filter = grab_filter(file_name)
            print pi, project_name, mask, filter, exposure_time, file_name
    f.close()    


if __name__== "__main__":

  create_table()
