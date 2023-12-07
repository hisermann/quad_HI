import csv
import os
import sys
import numpy as np
import pandas 
import scipy.interpolate as interp

# Settings
des_time_step = 1/400  # Desired time step that you want to upscale the data to  
search_dir = './'  # Set search directory
log_ident = 'backflip231207_contact_frameCorrected.csv'  # Set log file identifier

print('desired timestep: ', des_time_step)
print('search directory: ', search_dir)
WITHFILTER = 'filter' in sys.argv

# Find all log files that shall be upscaled
def get_all_log_files(log_ident, path):
    result = []
    alreadyFilled = False
    for root, dirs, files in os.walk(path):
         for filename in files:
            if log_ident in filename and not 'TaskSpace' in filename and not 'interp' in filename:
                result.append(os.path.join(root, filename))
            if 'filled' in filename: 
                alreadyFilled = True
    return result, alreadyFilled

logsToUpscale, alreadyFilled = get_all_log_files(log_ident, search_dir)

# Upscale all log files
numFiles = len(logsToUpscale)
count = 1
print('#######################')
print('Upscaling in process...')
print('#######################')
for fileName in logsToUpscale:
    print('file ' + str(count) + '/' + str(numFiles) + ': ' + str(fileName))
    # Load the data
    data = pandas.read_csv(fileName)
    cols = list(data.columns) 
    if 't[s]' not in data.columns:
        print('Error: Your data does not contain a ''t[s]'' column with time stamps!')
    # Check if 'contactPhases' column exists
    if 'contactPhases' in cols:
        cols.remove('contactPhases')  # Exclude 'contactPhases' from interpolation
    # Interpolate the data
    interpolator = {col: interp.CubicSpline(data['t[s]'], data[col],) for col in cols}
    total_time = data.iloc[-1]['t[s]']
    data_interp = []
    for t in np.arange(0, total_time+des_time_step, des_time_step):
        row = [interpolator[col](t).item() for col in cols]
        if 'contactPhases' in data.columns:
            nearest_time = data.loc[data['t[s]'].sub(t).abs().idxmin(), 't[s]']
            contact_phase = data.loc[data['t[s]'] == nearest_time, 'contactPhases'].values[0]
            row.append(int(contact_phase))
        data_interp.append(row)
    # Write interpolated data
    with open(os.path.splitext(fileName)[0]+'_interp.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(cols + ['contactPhases'])  # Write header
        writer.writerows(data_interp[:-1])  # Write data
    count += 1
print('Done.')
