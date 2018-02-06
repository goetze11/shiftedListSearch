#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#shiftedListSearch

shifted_lists = [[8, 9, 10, 11, 1, 3, 7], [6, 8, 10, 2, 4], 
                 [2, 4, 6, 8, 10], [], [5], 12]

def find_largest_int(shift_list):
    mid_index = len(shift_list)//2
    if len(shift_list) > 1:
        if shift_list[0] <= shift_list[mid_index]:
            #first half of list does not contain largest integer
            return find_largest_int(shift_list[mid_index: ])
        else:
            #first half of list contains the largest integer
            return find_largest_int(shift_list[0:mid_index])
    else:
        #we have found the largest element
        return shift_list[0]

        
#Run sample lists
if __name__ == "__main__":
    for shift_list in shifted_lists:
        if shift_list and isinstance(shift_list, list):
            largest_int = find_largest_int(shift_list)
            print("Largest Int is {0}".format(largest_int))
        else:
            print("Not an acceptable input format")


