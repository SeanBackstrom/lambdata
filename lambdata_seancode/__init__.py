'''
a useful set of data science functions
'''

import pandas as pd
import numpy as np

from lambdata_seancode import example_module

def nullfinder(df):
    '''
    this function will print out all the nulls found in each column
    of the dataframe
    '''

    print("Null totals in each column:")
    print(df.isnull().sum())


def listocol(list_, df):
    '''
    this function will convert a list to a column
     onto the dataframe provided
    '''
    

    df = df.assign(listocol= list_)
    return df


#Create test dataframe to check working package
TEST = pd.DataFrame(np.ones(10))
TEST