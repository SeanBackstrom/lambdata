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

#Creates a song class to instantiate song objects
class Song:
    def __init__(self, tempo, genre):
        self.tempo = tempo
        self.genre = genre

    #Song method for user to print stats
    def songstats(self):
        print("The song tempo is ", self.tempo,
        "and the genre is ", self.genre)

#Create test dataframe to check working package
TEST = pd.DataFrame(np.ones(10))
TEST