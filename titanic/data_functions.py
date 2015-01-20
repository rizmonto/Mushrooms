'''
Created on Jan 9, 2015

@author: rangeles
'''
import csv as csv
import numpy as np
import pandas as pd

def load_instances(filename):
    #csv.reader is an iterator
    csv_file_object = csv.reader(open('train.csv', 'rb'))
    #calling next will iterate once over the 1st row, effectively starting at the 2nd row
    header = csv_file_object.next()
    data = []

    for row in csv_file_object:
        data.append(row)

    return data

def load_instances_panda(filename):
    # For .read_csv, always use header=0 when you know row 0 is the header row
    df = pd.read_csv(filename, header = 0)

    return df

