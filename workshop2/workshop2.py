# -*- coding: utf-8 -*-

"""Main module."""
import unittest
import numpy as np

def calc_mean(input_data):
    n = len(input_data)
    sum_data = 0
    
    for i in range(0,n):
        sum_data = sum_data + input_data[i]

    mean = sum_data / n

    return mean

data_1 = np.arange(1,10,1)
answer = calc_mean(data_1)
print(answer)