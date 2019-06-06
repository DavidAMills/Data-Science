# Imports necessary libraries.
import time

# Function to ask user what file to open.
choice = input("Which file would you like to analyze?")

# Start the system clock to record how long a process takes.
start = time.process_time()

# Open the file stream (f), use "with" to automatically close the file when done.
with open(choice, "r") as f:
    # Reads the first line.
    first_line = f.readline()
    # Checks for tabs in the file.
    if '\t' in first_line:
        Delimiter = "Tab"
    elif ',' in first_line:
        Delimiter = "Comma"
    # Prints the first line.
    print("This is a " + Delimiter + "-delimited file.")
    print ("The first line reads: \n" + first_line)

# Prints the total time the process took to run.
print (time.process_time() - start)

    # This code will run until every line in the filestream is read.
    #for line in filestream:
        # Splits the line according to comma separated values into an array called "currentline".
        #currentline = line.split(",")
        # Sums the line.
        #total = str(int(currentline[0]) + int(currentline[1]) + int(currentline [2])) + "\n"
        # Prints the total.
        #print (total)
