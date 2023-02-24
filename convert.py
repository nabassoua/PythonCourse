#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### EXERCISES FROM PYTHON APPRENTISSAGE ACTIF BY JP. ROY            ##
######################################################################

"""
convert seconds to hrs, mins, and secs

"""

def convert(secs):

    secs_to_hr = secs / 3600
    full_hr = secs // 3600
    mins = secs_to_hr * 60
    print(mins)
    full_mins = mins // 1
    rem_secs = (mins - int(mins)) * 60
    print("{} corresponds to: ".format(secs))
    print("{} hr(s): {} mins: {} secs".format(full_hr,full_mins,int(rem_secs)))
    
    
my_secs=int(input("Please enter your seconds: "))
convert(my_secs)
