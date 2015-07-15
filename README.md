# Aerosols

These are all iPython notebooks, and will only work inside of that framework.

##Box Plot
2D (vertical) plot of aerosols with a slider and run button for time
* Worked:
..* Manual interaction with widgets and both the interact and interact_manual functions.
..* Modifying the original code to generate inline plots instead of separate files.
....* Used '%matplotlib inline' and modified code
* Didn’t work:
..* Hover interactions - Didn't have time to implement on this plot, as we moved on to a combined plot script

##Combined Plotting - Line Graphs
Combined Box Plot and Particle Sources into one script that generates both plots at once. Three sliders, consisting of x-bin, y-bin, and time sliders, change the parameters and a run button rerenders the plots. Particle sources has been changed to be line graphs of all the particles instead of bar charts of only one.
* Worked:
* Didn’t work:

##Combined Plotting
Combined Box Plot and Particle Sources into one script that generates both plots at once. Three sliders, consisting of x-bin, y-bin, and time sliders, change the parameters and a run button rerenders the plots.
* Worked:
* Didn’t work:

##Dual Plot
Example code of interactivity desired in the future. This MPLD3 script shows circles on bottom half of the plot and a changing sine wave plotted on top that changes period and amplitude based on which circle is hovered over. In the future this would ideally be added to the Combined Plotting (- Line Graphs?) so that the user could hover over the bins and the particle plots would change.
* Worked:
* Didn’t work:

##Dual Scatter
Scatter plots of several variables against each other, never made it past the initial plots because the interactivity didn’t work out.
* Worked:
* Didn’t work:

##Particle Sources
Bar charts of both sources and composition of aerosol particles with sliders for x-bin, y-bin, and time variables, as well as a button to run the script with new variables each time.
* Worked:
* Didn’t work:

##Scatterplot Data
Scatterplot of BC vs OC with a slider for time and a run button to run the script with new variables after changes are made.
* Worked:
* Didn’t work:

##Supersaturation Plot
Intended to be a plot of supersaturation values from a separate set of data that Nicole was using, but when we updated to python3 the partmc file needed to be updated and I never got back to it.
* Worked:
* Didn’t work: