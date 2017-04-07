# Import functions
from datetime import datetime
from random import *
import p1algorithms as algs


# File names
data_file = 'MSS_Problems.txt'
results_file = 'MSS_Results.txt'
exp_results_file = 'MS_ExperimentalResults.txt'


# Common code to write results to output file
def WRITERESULTS(data, subarray, maxsum, fileobject):
    for ea in data:
        fileobject.write(str(ea) + " ")
    fileobject.write("\n")
    for ea in subarray:
        fileobject.write(str(ea) + " ")
    fileobject.write("\n")
    fileobject.write(str(maxsum) + "\n\n")


# Common code to time the algorithms
def RUNEXPERIMENT(alg, n_array, n_multiplier, output_file):
    with open(output_file, 'a') as fw:
        fw.write("N Values\tTime (Seconds)\n")

    for ea in n_array:
        # Create array of random integers of size N
        array = []
        n_adjusted = int(ea) * n_multiplier
        for i in range(n_adjusted):
            array.append(randint(-100, 101))

        # Start timer
        startTime = datetime.now()

        # Run Algorithm
        max_i, max_j, maxsum = alg(array, 0, len(array)-1)

        # stop timer
        totalTime = datetime.now() - startTime

        with open(output_file, 'a') as fw:
            fw.write(str(n_adjusted) + "\t" + str(totalTime.total_seconds()) + "\n")
        print("N =", n_adjusted, "| Time =", totalTime.total_seconds(), "s")


######## Run Algorithms on Input File ########

# Delete contents of test results file
with open(results_file, 'w') as fw:
    fw.write("")


# Open data_file
with open(data_file, 'r') as fr:

    # Read each line
    for line in fr:

        # Split line into an array of values
        data = line.split()

        # Append Enumeration results to 'results_file'
        with open(results_file, 'a') as fw:

            # Call Algorithm 1: Enumeration to get the max sub array and max sum
            max_i, max_j, maxsum = algs.MAXSUBARRAY_Enum(data, 0, len(data)-1)

            fw.write("Algorithm 1: Enumeration Results\n")
            WRITERESULTS(data, data[max_i:max_j+1], maxsum, fw)

            # Call Algorithm 2: Enumeration to get the max sub array and max sum
            max_i, max_j, maxsum = algs.MAXSUBARRAY_BetterEnum(data, 0, len(data)-1)

            fw.write("Algorithm 2: Better Enumeration Results\n")
            WRITERESULTS(data, data[max_i:max_j+1], maxsum, fw)

            # Call Algorithm 3: Divide and Conquer to get the max sub array and max sum
            max_i, max_j, maxsum = algs.MAXSUBARRAY_DnC(data, 0, len(data)-1)

            fw.write("Algorithm 3: Divide and Conquer Results\n")
            WRITERESULTS(data, data[max_i:max_j+1], maxsum, fw)

            # Call Algorithm 4: Linear Time to get the max sub array and max sum
            max_i, max_j, maxsum = algs.MAXSUBARRAY_Linear(data, 0, len(data)-1)

            fw.write("Algorithm 4: Linear Results\n")
            WRITERESULTS(data, data[max_i:max_j+1], maxsum, fw)

######## Experimental Time Runs ########

# Delete contents of test results file
with open(exp_results_file, 'w') as fw:
    fw.write("Experimental Time Runs\n")
print("Experimental Time Runs")

# Array for N sizes
N = [25, 35, 50, 75, 100, 125, 250, 500, 750, 1000]

# Algorithm 1: Enumeration
with open(exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 1: Enumeration\n")
print("\nAlgorithm 1: Enumeration")

RUNEXPERIMENT(algs.MAXSUBARRAY_Enum, N, 1, exp_results_file)


# Algorithm 2: Better Enumeration
with open(exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 2: Better Enumeration\n")
print("\nAlgorithm 2: Better Enumeration")

RUNEXPERIMENT(algs.MAXSUBARRAY_BetterEnum, N, 10, exp_results_file)


# Algorithm 3: Divide and Conquer
with open(exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 3: Divide and Conquer\n")
print("\nAlgorithm 3: Divide and Conquer")

RUNEXPERIMENT(algs.MAXSUBARRAY_DnC, N, 1000, exp_results_file)


# Algorithm 4: Linear Time
with open(exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 4: Linear Time\n")
print("\nAlgorithm 4: Linear Time")

RUNEXPERIMENT(algs.MAXSUBARRAY_Linear, N, 10000, exp_results_file)
