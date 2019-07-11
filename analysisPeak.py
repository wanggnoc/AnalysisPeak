# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
chrDict={
'chr1':249250621,
'chr2':243199373,
'chr3':198022430,
'chr4':191154276,
'chr5':180915260,
'chr6':171115067,
'chr7':159138663,
'chr8':146364022,
'chr9':141213431,
'chr10':135534747,
'chr11':135006516,
'chr12':133851895,
'chr13':115169878,
'chr14':107349540,
'chr15':102531392,
'chr16':90354753,
'chr17':81195210,
'chr18':78077248,
'chr19':59128983,
'chr20':63025520,
'chr21':48129895,
'chr22':51304566,
'chrX':155270560,
'chrM':16571,}
files = './E003-H3K4me1.narrowPeak'
counts=0
array=set()
import numpy as np
with open(files) as f:
    for line in f:
        lines = line.strip().split('\t')
        chr,start,end = lines[0],int(lines[1]),int(lines[2])
        len1 = np.intersect1d(np.arange(start//200*200,(start//200+1)*200),np.arange(start,(start//200+1)*200))
        len2 = np.intersect1d(np.arange(end//200*200,(end//200+1)*200),np.arange(end//200*200,end))
       	index_s = start//200+1 if len(len1)<100 else start//200
        index_e = end//200-1 if len(len2)<100 else end//200
        for ind in range(index_s,index_e+1):
            array.add(chr+"_"+str(ind))
        if counts+1%1000 == 0:
            print(counts)
print(len(array))
    
    
