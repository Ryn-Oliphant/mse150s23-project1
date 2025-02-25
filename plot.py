import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(fname=filename,delimiter=' ',comments='"',usecols=range(6))   # Attempts to load filename into local variable data.

## Part 0 (Done)
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw_data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw
# at the command line.


## Part 1 (Done)
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw
# Make sure to include axis labels and units!
# plt.plot(xdata, ydata, arguments-to-make-plot-pretty)


## Part 2 (Done)
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable
# Don't worry about deleting parts you might need later -- that's why we use git!


## Part 3 (Done)
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


## Part 4 (Done)
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.

#Added Code below

def youngs_modulus (data):
    
    lin_fit = np.polyfit(data[0:200,5],data[0:200,1],1)
    lin_func = np.poly1d(lin_fit)
    
    print("Young's Modulus = ",lin_fit[0],'Pa')
    
youngs_modulus(data)



fig = plt.figure(figsize=(6,4))

plt.plot(data[:,5],data[:,1],'c.')
plt.xlabel('Strain (%)',size=12)
plt.ylabel('Stress (Pa)',size=12)
plt.title('Stress vs Strain of '+filename[39:-4],size=14)
plt.savefig('stress-v-strain_'+filename[39:-4]+'.png')
plt.show()