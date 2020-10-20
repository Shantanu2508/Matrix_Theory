#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:09:14 2020

@author: shantanu
"""

import numpy as np
from myrref import *

A=np.array([[2,-1,1],[-1,1,1],[3,1,9],[2,-3,-5]],float)
B=np.array([[3],[-1],[0],[1]],float)
AB=np.column_stack((A,B))
ABrref,invAB=myrref(AB,4,4)
print(ABrref)
rankA=np.linalg.matrix_rank(A)
rankAB=np.linalg.matrix_rank(ABrref)
print("Rank of matrix A is : ",rankA)
print("Rank of matrix AB is : ",rankAB)
