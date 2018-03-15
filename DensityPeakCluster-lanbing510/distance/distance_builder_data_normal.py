#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:19:25 2018

@author: zhuriheng
"""

from distance_builder import *
from distance import *

import numpy as np

if __name__ == '__main__':
    builder = DistanceBuilder()
    builder.load_points(r'../data/data_others/feature/normal.txt')
    builder.build_distance_file_for_cluster(
        SqrtDistance(), r'../data/data_others/feature/normal_sqrt_distance.dat')
    #builder.build_distance_file_for_cluster(
        #ConsineDistance(), r'../data/data_others/feature/normal_consine_distance.dat')
    #builder.build_distance_file_for_cluster(
        #PearsonDistance(), r'../data/data_others/feature/normal_pearson_distance.dat')
