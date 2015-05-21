def get_specs():
  """Returns the details regarding the run being investigated. These values
     should mirror the values found in the namelist.input file.
  """

  num_times = 7 # number of output times
  num_layers = 15 # number of vertical layers of data. This may not match nz.
  num_box_x = 40 # number of east-west boxes
  num_box_y = 30 # number of north-south boxes
  dx = 4.0 # delta x in km
  dy = 4.0 # delta y in km
  
  return(num_times, num_layers, num_box_x, num_box_y, dx, dy)
