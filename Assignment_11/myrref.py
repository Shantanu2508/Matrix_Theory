#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:39:18 2020

@author: shantanu
"""
#changes:
    #n--->c

import numpy as np



def myrref(B,m,n):
    A=B.copy()
    rows,cols=A.shape
    r=0
    row_exchange=np.arange(rows)
    for c in range(cols):
        pivot = np.argmax(np.abs(A[r:rows, c])) + r
        maxpivot= np.abs(A[pivot,c])
        
        #If pivot element ie m=0 we select new element in same row
        #If we reach last row and all element are 0 return A
        while maxpivot==0:
            if r!=rows-1 and c==cols-1 and maxpivot==0:
                r=r+1 
            if r==rows-1 and c==cols-1 and maxpivot==0:
                return A,A[0:rows,n:cols]
            c=c+1
            pivot=np.argmax(np.abs(A[r:rows,c]))+r
            maxpivot=np.abs(A[pivot,c])
            
        if pivot!=r:
            A[[r,pivot],c:cols] = A[[pivot,r],c:cols]
            row_exchange[[r,pivot]]=row_exchange[[pivot,r]]
            A[r, c:cols] = A[r, c:cols] / A[r, c];
        else : A[r, c:cols] = A[r, c:cols] / A[r, c];

        v=A[r,c:cols]
        
        if r>0:
            ridx_above=np.arange(r)
            A[ridx_above,c:cols]=A[ridx_above,c:cols] - np.outer(A[ridx_above,c],v)
        if r<rows-1:
            ridx_below=np.arange(r+1,rows)
            A[ridx_below,c:cols] = A[ridx_below,c:cols] - np.outer(A[ridx_below,c],v)
            
        r+=1
        if r==rows:  break;
    return A,A[0:rows,n:cols]