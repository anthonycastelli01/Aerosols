#!/usr/bin/env python

import scipy.io
import sys
import numpy as np
import matplotlib
import os

import matplotlib.pyplot as plt
sys.path.append("../../tool")
import partmc

def make_plot(in_dir, in_filename, title, out_filename):
    print 'file ', in_dir+in_filename
    
    ncf = scipy.io.netcdf.netcdf_file(in_dir+in_filename, 'r')
    particles= partmc.aero_particle_array_t(ncf)
    ncf.close()
    
    bc =  particles.masses(include = ["BC"])/particles.aero_data.molec_weights[0]
    oc =  particles.masses(include = ["OC"])/particles.aero_data.molec_weights[3] 
    no3 =  particles.masses(include = ["NO3"])/particles.aero_data.molec_weights[1]  

    plt.scatter(bc,oc)
    
    a = plt.gca() # gets the axis
    a.set_xscale("log") # x axis log
    a.set_yscale("log") # y axis log
    plt.axis([1e-20, 1e-15, 1e-20, 1e-15]) # axis limit

    plt.title(title)
    fig = plt.gcf()
    fig.savefig(out_filename)

for counter in range(1,25):
    print "counter = ", counter
    
    in_dir = "out/"
    in_filename = "urban_plume_4m_0001_000000%02d.nc" % counter
    title = " %02d hours" % (counter-1)
    out_filename = "figs/scatter_mass_%02d.pdf" % counter

    print title

    make_plot(in_dir, in_filename, title, out_filename)

