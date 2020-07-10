# lambdata

A python package with useful Data Science functions

So far, lambdata is split into 5 python files with handwritten created code. 

Please advise that lambdata is in current development and has test files currently inside the package that will not be present in a final version release.


# Lambdata currently has two useful functions:

## nullfinder(df):

This function takes in a dataframe and will return to you all the null values summed together in each column of your dataframe.

It is located in init.py under lambdata_seancode

## listtocol(list_, df):

This function takes a list, then converts it and places it as a column onto the end of the given dataframe.

It is located in init.py under lambdata_seancode

# Files in lambdata

To assist navigating the packages source code I have created this guide on all current manually created files. All manually created files are located inside **lambdata_seancode**.

## init.py

Contains all imports of outside packages as well as the callable functions of lambdata.

## example_module.py

Used as a test module (surprise!) to test connections between modules, and local imports between files.

## lambdata_test.py

A file containing class tests using unittest to determine validity of instantiated classes present in lambdata

## songclass.py

A non-relevant experiment of python classes to test the cross workings of classes between modules.

## tester.ipynb

A python notebook used to test and implement new functions that will eventually be included into lambdata's official functions.

# Outside of lambdata_seancode

## setup.py

Includes all relevant information to be built and distributed successfully onto PyPi.
