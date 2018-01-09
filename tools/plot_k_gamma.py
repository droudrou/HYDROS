#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:43:08 2018

@author: mdrouin
"""

from pylab import *
from sys import argv
import matplotlib.pyplot as plt

dat=genfromtxt(argv[1])
n=len(dat)
print("Number of lines : ", n)

k=dat[:,0]
g=dat[:,3]

plt.plot(k,g,'red')
xlabel('Frequency')
ylabel('Damping rate')
tight_layout()
show()

