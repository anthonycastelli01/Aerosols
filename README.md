# Aerosols

These are all iPython notebooks, and will only work inside of that framework.

##Box Plot
2D (vertical) plot of aerosols with a slider and run button for time
* Worked:
  * Manual interaction with widgets and both the interact and interact_manual functions.
  * Modifying the original code to generate inline plots instead of separate files.
    * Used `%matplotlib inline` and modified code
* Didn’t work:
  * Hover interactions - Didn't have time to implement on this plot, as we moved on to a combined plot script

##Combined Plotting - Line Graphs with Labels
Combined Box Plot and Particle Sources into one script that generates both plots at once. Three sliders, consisting of x-bin, y-bin, and time sliders, change the parameters and a run button rerenders the plots. Particle sources has been changed to be line graphs of all the particles instead of bar charts of only one. This would be the same as Combined Plotting - Line Graphs, but with labeled lines.
* Worked:
  * See: `Combined Plotting - Line Graphs`
  * Produced a legend displaying all lines.
* Didn't Work:
  * Unable to generate labels that specified which line was being described, only one large legend.
    * Labels require x/y coordinates, unable to determine how to make them not overlap procedurally.

##Combined Plotting - Line Graphs
Combined Box Plot and Particle Sources into one script that generates both plots at once. Three sliders, consisting of x-bin, y-bin, and time sliders, change the parameters and a run button rerenders the plots. Particle sources has been changed to be line graphs of all the particles instead of bar charts of only one.
* Worked:
  * Manual interaction with widgets and both the interact and interact_manual functions.
  * Modifying the original code to generate inline plots instead of separate files.
    * Used `%matplotlib inline` and modified code
  * Modifying code so that source and constituent data were plotted as lines instead of bars, in order to show all particles instead of just one
* Didn’t work:
  * Hover interactions with mpld3
    * Initial intent was to be able to hover over a bin and the source/constituent plots would change. Alternatively, if that was too computationally intensive, one would be able to hover over the bin to see its x/y coordinates and use sliders to generate a graph.
    * Widget sliders and mpld3 code didn't seem to agree with one another. Separately, both worked fine (See: `Dual Plot` for example of mpld3 interaction), however once an attempt to use a slider to change the time an mpld3 plot was implemented, the script generated an empty image. (Or froze? Unable able to determine.)

##Combined Plotting
Combined Box Plot and Particle Sources into one script that generates both plots at once. Three sliders, consisting of x-bin, y-bin, and time sliders, change the parameters and a run button rerenders the plots.
* Worked:
  * Manual interaction with widgets and both the interact and interact_manual functions.
  * Modifying the original code to generate inline plots instead of separate files.
    * Used `%matplotlib inline` and modified code
* Didn’t work:
  * Hover interactions with mpld3
    * Widget sliders and mpld3 code didn't seem to agree with one another. Separately, both worked fine (See: `Dual Plot` for example of mpld3 interaction), however once an attempt to use a slider to change the time an mpld3 plot was implemented, the script generated an empty image. (Or froze? Unable able to determine.)

##Dual Plot
Example code of interactivity desired in the future. This MPLD3 script shows circles on bottom half of the plot and a changing sine wave plotted on top that changes period and amplitude based on which circle is hovered over. In the future this would ideally be added to the Combined Plotting (- Line Graphs?) so that the user could hover over the bins and the particle plots would change.
* Worked:
  * Example code from the internet.
* Didn’t work:
  * Merging it into other plots previously made to display aerosol data.

##Dual Scatter
Scatter plots of several variables against each other, never made it past the initial plots because the interactivity didn’t work out.
* Worked:
  * Plotting three variables against each other as one set of plots.
* Didn’t work:
  * Combining with iteractivity seen at [this MPLD3 example website](https://mpld3.github.io/examples/linked_brush.html)
  * Similar problems as the Combined Plotting series - MPLD3 and Widgets just won't work at the same time.
    * It might be possible to write a slider into MPLD3 code, using the D3 code seen [here in this page](http://thematicmapping.org/playground/d3/d3.slider/), and controlling the time that way, but that's just speculation.

##Particle Sources
Bar charts of both sources and composition of aerosol particles with sliders for x-bin, y-bin, and time variables, as well as a button to run the script with new variables each time.
* Worked:
  * Manual interaction with widgets and both the interact and interact_manual functions.
  * Modifying the original code to generate inline plots instead of separate files.
    * Used `%matplotlib inline` and modified code
* Didn’t work:
  * Didn't go past this, only intended to test it out before combining it with the `Box Plot` plots.

##Scatterplot Data
Scatterplot of BC vs OC with a slider for time and a run button to run the script with new variables after changes are made.
* Worked:
  * Manual interaction with widgets and both the interact and interact_manual functions.
  * Modifying the original code to generate inline plots instead of separate files.
    * Used `%matplotlib inline` and modified code
* Didn’t work:
  * Any hover interactivity with MPLD3, but there wasn't enough time to thoroughly test it out.

##Supersaturation Plot
Intended to be a plot of supersaturation values from a separate set of data that Nicole was using, but when we updated to python3 the partmc file needed to be updated and I never got back to it.
* Worked:
  * Initially, in Python 2.7, the `interact` method was able to change the plot based on time.
* Didn’t work:
  * When updating to Python 3, partmc needed to be updated but never was, so it stayed broken.