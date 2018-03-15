#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:43:04 2018

@author: zhuriheng
"""

from distance_builder import *
from distance import *

import numpy as np

if __name__ == '__main__':
    builder = DistanceBuilder()

    i = 0
    while i<14:
        builder = DistanceBuilder()
        builder.load_points(r'../data/data_others/feature/' + str(i) + '.txt')
        builder.build_distance_file_for_cluster(
                SqrtDistance(), r'../data/data_others/feature/' + str(i) + '_sqrt_distance.dat')
        i = i+1
        
    #builder.load_points(r'../data/data_others/feature/features.txt')
    #builder.build_distance_file_for_cluster(
        #SqrtDistance(), r'../data/data_others/feature/features_sqrt_distance.dat')
    #builder.build_distance_file_for_cluster(
        #ConsineDistance(), r'../data/data_others/feature/features_consine_distance.dat')
    #builder.build_distance_file_for_cluster(
        #PearsonDistance(), r'../data/data_others/feature/features_pearson_distance.dat')
