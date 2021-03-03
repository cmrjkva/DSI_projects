#This program combines individual states' datasets obtained from NOAA National Weather Service into one dataframe

#step 1: required imports
import pandas as pd

#step 2: create an empty dataframe called 'noaa_data'
noaa_data = pd.DataFrame()

#step 3: list all states of interest by their abbreviation (e.g. AZ for Arizona)
states = ['AZ', 'CA', 'CO', 'ID', 'MT','NM', 'NV','OR', 'UT', 'WA', 'WY']

#step 4: determine naming convention and location of files:
path = input('What is the relative path to the folder with files to be combined?')
XX_ = input('What is the extension for files to be combined (include "."")?')

#step 5: loop through all states in the list above
for state in states:
    df = pd.read_csv(path+'/'+state+XX_) # step 5.1: read the state's data into a temporary dataframe
    df['state'] = state # step 5.2: create a column in the dataframe with the state abbreviation so that we know which state each row pertains to after concatenating
    noaa_data = pd.concat([noaa_data,df], axis = 0) # step 5.3: concatenate the temporary dataframe into the "noaa_data" dataframe
    print(f"{len(df)} lines from the {state}{XX_} datafile are now merged into noaa_data") # 5.4 print update message

# step 6: save combined data in a csv file in the specified folder
save_path = input('Where should the csv file be saved?')
noaa_data.to_csv(save_path+'/'+'noaa_data.csv')

#step #7: print update
print(f"The noaa_data.csv file with {noaa_data.shape[0]} rows and {noaa_data.shape[1]} columns is now available in the {save_path} folder!")
