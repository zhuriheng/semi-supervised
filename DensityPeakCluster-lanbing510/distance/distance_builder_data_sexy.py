#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:21:37 2018

@author: zhuriheng
"""

from distance_builder import *
from distance import *

import numpy as np

if __name__ == '__main__':
    builder = DistanceBuilder()
    builder.load_points(r'../data/data_others/feature/sexy_1000.txt')
    builder.build_distance_file_for_cluster(
        SqrtDistance(), r'../data/data_others/feature/sexy_1000_sqrt_distance.dat')
    #builder.build_distance_file_for_cluster(
        #SqrtDistance(), r'../data/data_others/feature/sexy_sqrt_distance.dat')
    #builder.build_distance_file_for_cluster(
        #ConsineDistance(), r'../data/data_others/feature/sexy_consine_distance.dat')
    #builder.build_distance_file_for_cluster(
        #PearsonDistance(), r'../data/data_others/feature/sexy_pearson_distance.dat')
