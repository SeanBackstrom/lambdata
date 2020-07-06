'''
a useful set of data science function
'''

import pandas as pd
import numpy as np

from lambdata_seancode import example_module

def nullfinder(df):
    print("Null totals in each column:")
    print(df.isnull().sum())
    
def listocol(list_, df):
    
    df = df.assign(listocol= list_)

    return df


TEST = pd.DataFrame(np.ones(10))
TEST