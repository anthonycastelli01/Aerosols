import numpy
import partmc
import scipy
import mpl_helper
import config
import random
import matplotlib
import math
import sys

def grid_box_details(x_bin, y_bin, time):
    # filename prefix
    dir = config.data_dir
    prefix = config.file_prefix
    filename =  '%s_%08i.nc' %(prefix,time)

    # Compute the black carbon mass fraction
    x_axis = partmc.log_grid(min=1e-9,max=1e-6,n_bin=60)
    bc_axis = partmc.linear_grid(min=0,max=1.,n_bin=50)

    x_centers = x_axis.centers()
    ncf = scipy.io.netcdf.netcdf_file(config.data_dir+'/'+filename, 'r')
    particles = partmc.aero_particle_array_t(ncf)
    env_state = partmc.env_state_t(ncf)
    aero_data = partmc.aero_data_t(ncf)
    ncf.close()

    bc = particles.masses(include = ["BC"])
    dry_mass = particles.masses(exclude = ["H2O"])
    bc_frac = bc / dry_mass

    dry_diameters = particles.dry_diameters()

    # Find the particles in a certain bin
    x_bins = x_axis.find(dry_diameters)
    y_bins = bc_axis.find(bc_frac)
    print x_bins[0:10]
    print y_bins[0:10]
    # make figure
    width_in = 3.25
    (figure, axes, cbar_axes) = mpl_helper.make_fig(figure_width=width_in,
        colorbar=True,left_margin=.7,right_margin=1, top_margin=0.3,
        bottom_margin=.6, colorbar_height_fraction=0.8)

    # Pick a particle bin
    parts = []
    sources = particles.n_orig_parts
    # this could be better
    x_parts = numpy.ma.masked_not_equal(x_bins, x_bin)
    y_parts = numpy.ma.masked_not_equal(y_bins, y_bin)
    xx = numpy.ma.MaskedArray.nonzero(x_parts)
    yy = numpy.ma.MaskedArray.nonzero(y_parts)
    parts = list(set(xx[0]).intersection(yy[0]))
    print parts
    # Randomly select from particles
    if (len(parts) == 0):
        print 'no particles in this bin'
        return

    index = random.choice(parts)
    print 'particle list', parts
    print 'particle chosen', index

    # Get the sources
    strings = aero_data.source_names
    print sources[:,index]
    print strings
    # Make the figure of sources
    (fig, axes) = mpl_helper.make_fig(figure_width=width_in,
       axis_ratio=2,
       left_margin=.7,right_margin=.1, top_margin=0.25,
       bottom_margin=1.1, colorbar_height_fraction=0.8)
    width = .5
    x_values_source = numpy.arange(0,len(aero_data.source_names)) + .5*width

    segmentdata = {'red':   [(0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  1.0, 1.0)],

         'green': [(0.0,  0.0, 0.0),
                   (0.25, 0.0, 0.0),
                   (0.75, 1.0, 1.0),
                   (1.0,  1.0, 1.0)],

         'blue':  [(0.0,  0.0, 0.0),
                   (0.5,  0.0, 0.0),
                   (1.0,  1.0, 1.0)]}
    sourcecolors = ['DarkBlue','DarkRed','DarkGreen','SteelBlue','DarkViolet']
    axes.bar(x_values_source, sources[:,index], width, color=sourcecolors,edgecolor=sourcecolors)
    # Make it pretty with labels
    axes.set_xticks(x_values_source+.5*width)
    axes.set_ylabel(r'number from source')
    axes.set_xlabel(r'particle sources')
    labels = ['small bkgrd','large bkgrd','cooking','diesel','gasoline']
    for tick in axes.get_xaxis().get_major_ticks():
        tick.set_pad(2.0)
        tick.label1 = tick._get_text1()
    axes.set_xticklabels(labels, rotation=45)
    axes.set_xlim([0,x_values_source[-1] + 1.5*width])
    max_sources = numpy.max(sources[:,index])+1
    axes.set_ylim([0,max_sources])
    axes.set_yticks(numpy.arange(0,max_sources+1))

    axes.spines["top"].set_visible(False)
    axes.spines["right"].set_visible(False)
    axes.get_xaxis().tick_bottom()
    axes.get_yaxis().tick_left()

    # Save the figure
    fig.savefig('figs/particle_sources_%08i.png'
         %(time))
    # Make a figure regarding the mass distribution of species
    # What species we want?
    species_list = ['BC', 'OC', 'NO3', 'SO4', 'NH4']
    colors = ['black','green','blue','red','orange']
    values = numpy.zeros(len(species_list))
    for ii, value in enumerate(species_list):
        species_masses = particles.masses(include=[value])
        values[ii] = species_masses[index]  
    # Convert units from kg to micrograms
    values *= 1e9
    # Make the figure
    (fig, axes) = mpl_helper.make_fig(figure_width=width_in,
        axis_ratio=2,
        left_margin=.7,right_margin=.1, top_margin=0.25,
        bottom_margin=.55, colorbar_height_fraction=0.8)
    x_values = numpy.arange(0,len(species_list)) + .5*width
    axes.grid(b='on',which='major',axis='y',color='gray')
    axes.bar(x_values, values,width,color=colors,edgecolor=colors)
    axes.set_ylabel(r'mass $\left(\mu\rm g\right)$')
    axes.set_xlabel(r'particle constituents')
    axes.set_xticks(x_values+.5*width)
    axes.grid(b='on',which='major',axis='y',color='gray',alpha=.5, linestyle=':')

    latex_labels = []
    for ii,spec in enumerate(species_list):
        latex_labels.append(aero_data.species_tex_names[spec])
    axes.set_xticklabels(latex_labels,verticalalignment='top')
    axes.set_xlim([0,x_values[-1] + 1.5*width])
    max_value = (numpy.ceil(numpy.max(values) / 10**numpy.floor(numpy.log10(numpy.max(values)))))*10**numpy.floor(numpy.log10(numpy.max(values)))
    axes.set_ylim([0,max_value])
    axes.set_yticks(numpy.arange(0,max_value+1e-12,.5*10**numpy.floor(numpy.log10(numpy.max(values)))))
    axes.spines["top"].set_visible(False)
    axes.spines["right"].set_visible(False)
    axes.get_xaxis().tick_bottom()
    axes.get_yaxis().tick_left()
    for label in axes.yaxis.get_ticklabels()[1:6:2]:
       print label
       label.set_visible(False)
    fig.savefig('figs/particle_composition_%08i.png'
        %(time))

    return

# main program
grid_box_details(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
