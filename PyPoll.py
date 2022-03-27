# import csv and os modules to be able to navigate operating system
# and to read csv files
import csv
import os
# define file_to_load as a variable referencing the file object
# uses the operating system path to look for the joined folders

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with always needs a : at the end
#with open(file_to_save, "w") as txt_file:
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
#Print each row in the CSV file
    #for row in file_reader:
        #print(row)
    # Write some data to the file.
    #use the \n to command new line 
    #txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
    #Print the header row
    headers = next(file_reader)
    print(headers)