#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from plot import *
from cluster import *


def plot(data, auto_select_dc=False):
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dpcluster = DensityPeakCluster()
    distances, max_dis, min_dis, max_id, rho, rc = dpcluster.local_density(
        load_paperdata, data, auto_select_dc=auto_select_dc)
    delta, nneigh = min_distance(max_id, max_dis, distances, rho)
    plot_rho_delta(rho, delta)  # plot to choose the threthold

if __name__ == '__main__':
    # plot('./data/data_in_paper/example_distances.dat')
    # plot('./data/data_others/spiral_distance.dat')
    # plot('./data/data_others/aggregation_distance.dat')
    # plot('./data/data_others/flame_distance.dat')
    # plot('./data/data_others/jain_distance.dat')
    # plot('./data/data_others/test_distance.dat')


    # plot('./data/data_others/feature/features_distance.dat')
    # plot('./data/data_others/feature/features_consine_distance.dat')
    # plot('./data/data_others/feature/features_pearson_distance.dat')

    # plot('./data/data_others/normal_distance.dat')
    # plot('./data/data_others/sexy_distance.dat')
    # plot('./data/data_others/pulp_distance.dat')

    plot('./data/data_others/sexy_1000_distance.dat')
