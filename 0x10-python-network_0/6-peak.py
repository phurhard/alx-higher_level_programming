#!/usr/bin/python
''' This function finds the peak in a list of integers'''
def find_peak(list_of_integers):
    '''Return: The peak in the list of integers
        '''
    try:
        list_of_integers.sort()
        return list_of_integers[-1]
    except:
        return None
