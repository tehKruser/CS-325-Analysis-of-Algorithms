# Import functions
from datetime import datetime
import p2algorithms as algs
from itertools import zip_longest
import sys
import os.path


# Turn runs on/off by setting to True/False
run_file = True
run_pr3 = False
run_pr4 = False
run_pr5 = False
run_pr7 = False


# Check program arguments
if len(sys.argv) == 1:
    data_file = 'coins.txt'  # for testing purposes
elif len(sys.argv) > 1:
    data_file = str(sys.argv[1])
    if len(sys.argv) == 3:
        if str(sys.argv[2]) == "exp":
            print("Experimental runs turned on. Estimated execution time: 9 minutes")
            run_pr3 = True
            run_pr4 = True
            run_pr5 = True
            run_pr7 = True

if not os.path.isfile(data_file):
    run_file = False
    print("No such file in directory!")

#print("File exists:", os.path.isfile(data_file))

results_file = data_file[:-4] + 'change.txt'
PR3_exp_results_file = 'PR3_ExperimentalResults.txt'
PR4_exp_results_file = 'PR4_ExperimentalResults.txt'
PR5_exp_results_file = 'PR5_ExperimentalResults.txt'
PR7_exp_results_file = 'PR7_ExperimentalResults.txt'

# Python Documentation Recipe to group file input
def GROUPER(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


# Common code to write results to output file
def WRITERESULTS(data, coincounts, totalcoins, fileobject):
    lineprint = "";
    for ea in data:
        fileobject.write(str(ea) + "\t")
        lineprint += "{}{}".format(ea, "\t")
    print(lineprint)
    fileobject.write("\n")
    lineprint = ""
    for ea in coincounts:
        fileobject.write(str(ea) + "\t")
        lineprint += "{}{}".format(ea, "\t")
    print(lineprint)
    fileobject.write("\n")
    fileobject.write(str(totalcoins) + "\n\n")
    print("{}{}".format(totalcoins, "\n"))


# Common code to time the algorithms
def RUNEXPERIMENT(alg, n_array, data, n_multiplier, print_header, output_file):
    template = "{0:10}|{1:10}|{2:16}|{3:13}"

    if print_header:
        with open(output_file, 'a') as fw:
            fw.write("A Values\tTime (Seconds)\tOptimal Solution\tDenominations\n")
        print(template.format("A Values", "Time (s)", "Optimal Solution", "Denominations"))

    for ea in n_array:
        target = ea * n_multiplier

        # Start timer
        startTime = datetime.now()

        # Run Algorithm
        c, m = alg(data, target)

        # stop timer
        totalTime = datetime.now() - startTime

        with open(output_file, 'a') as fw:
            fw.write(str(target) + "\t" + str(totalTime.total_seconds()) + "\t" + str(m) + "\t" + str(len(data)) + "\n")
        data_print = [target, totalTime.total_seconds(), m, len(data)]
        print(template.format(*data_print))


'''
########################################################
############# Run Algorithms on Input File #############
########################################################
'''

if run_file:
    print("\n******Solving Input File ******")
    print("Running Solutions on {}...\n".format(data_file))
    # Delete contents of test results file
    with open(results_file, 'w') as fw:
        fw.write("")

    # Open data_file
    with open(data_file, 'r') as fr:

        # Read every 2 lines using grouper function
        for line1, line2 in GROUPER(fr, 2):
            # Split line into an array of values
            # This is the denomination array in test files
            data = list(map(int, line1.split()))
            dataTarget = int(line2)

            # Append Enumeration results to 'results_file'
            with open(results_file, 'a') as fw:
                fw.write("Algorithm 1: Change Slow\n")
                print("Algorithm 1: Change Slow")
                # Call Algorithm 1: ChangeSlow to get the max sub array and max sum
                c, m = algs.ChangeSlow(data, dataTarget)
                WRITERESULTS(data, c, m, fw)

                fw.write("Algorithm 2: Change Greedy\n")
                print("Algorithm 2: Change Greedy")
                # Call Algorithm 2: ChangeGreedy
                c, m = algs.ChangeGreedy(data, dataTarget)
                WRITERESULTS(data, c, m, fw)

                fw.write("Algorithm 3: Change DP\n")
                print("Algorithm 3: Change DP")
                # Call Algorithm 3: ChangeDP
                c, m = algs.ChangeDP(data, dataTarget)
                WRITERESULTS(data, c, m, fw)

'''
########################################################
################ Experimental Time Runs ################
########################################################
'''

'''********************** Question 3 Runs **********************'''
if run_pr3:

    # Array for Project Report Question 3
    A3 = []
    i = 100
    for i in range(100, 305, 5):
        A3.append(i)
    V3 = [1, 5, 10, 25, 50]

    # Delete contents of test results file
    with open(PR3_exp_results_file, 'w') as fw:
        fw.write("Experimental Time Runs\n")
    print("\n******Project Report Question 3******\nRunning Experiment...")

    # Algorithm 1: Change Slow
    with open(PR3_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 1: Change Slow\n")
    print("\nAlgorithm 1: Change Slow")

    RUNEXPERIMENT(algs.ChangeSlow, A3, V3, 1, True, PR3_exp_results_file)

    # Algorithm 2: Change Greedy
    with open(PR3_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 2: Change Greedy\n")
    print("\nAlgorithm 2: Change Greedy")

    RUNEXPERIMENT(algs.ChangeGreedy, A3, V3, 100000, True, PR3_exp_results_file)

    # Algorithm 3: Change DP
    with open(PR3_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 3: Change Dynamic Programming\n")
    print("\nAlgorithm 2: Change Dynamic Programming")

    RUNEXPERIMENT(algs.ChangeDP, A3, V3, 1000, True, PR3_exp_results_file)

'''********************** Question 4 Runs **********************'''
# Arrays used for questions 4 and 5
A_small = []
for j in range(25, 126, 1):
    A_small.append(j)

A_medium = []
for j in range(100000, 100101, 1):
    A_medium.append(j)

A_large = []
for j in range(10000000, 10000101, 1):
    A_large.append(j)

if run_pr4:
    # Arrays for Project Report Question 4
    V4_1 = [1, 2, 6, 12, 24, 48, 60]
    V4_2 = [1, 6, 13, 37, 150]

    # Delete contents of test results file
    with open(PR4_exp_results_file, 'w') as fw:
        fw.write("Experimental Time Runs\n")
    print("\n******Project Report Question 4******\nRunning Experiment...")

    '''***************** Solutions for A when V1 Denominations *****************'''

    # Algorithm 1: Change Slow (V1)
    with open(PR4_exp_results_file, 'a') as fw:
       fw.write("\nAlgorithm 1: Change Slow (V1)\n")
    print("\nAlgorithm 1: Change Slow (V1)")

    RUNEXPERIMENT(algs.ChangeSlow, A_small, V4_1, 1, True, PR4_exp_results_file)

    # Algorithm 2: Change Greedy (V1)
    with open(PR4_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 2: Change Greedy (V1)\n")
    print("\nAlgorithm 2: Change Greedy (V1)")

    RUNEXPERIMENT(algs.ChangeGreedy, A_large, V4_1, 1, True, PR4_exp_results_file)

    # Algorithm 3: Change DP (V1)
    with open(PR4_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 3: Change DP (V1)\n")
    print("\nAlgorithm 3: Change DP (V1)")

    RUNEXPERIMENT(algs.ChangeDP, A_medium, V4_1, 1, True, PR4_exp_results_file)

    '''***************** Solutions for A when V2 Denominations *****************'''

    # Algorithm 1: Change Slow (V2)
    with open(PR4_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 1: Change Slow (V2)\n")
    print("\nAlgorithm 1: Change Slow (V2)")

    RUNEXPERIMENT(algs.ChangeSlow, A_small, V4_2, 1, True, PR4_exp_results_file)

    # Algorithm 2: Change Greedy (V2)
    with open(PR4_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 2: Change Greedy (V2)\n")
    print("\nAlgorithm 2: Change Greedy (V2)")

    RUNEXPERIMENT(algs.ChangeGreedy, A_large, V4_2, 1, True, PR4_exp_results_file)

    # Algorithm 3: Change DP (V1)
    with open(PR4_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 3: Change DP (V2)\n")
    print("\nAlgorithm 3: Change DP (V2)")

    RUNEXPERIMENT(algs.ChangeDP, A_medium, V4_2, 1, True, PR4_exp_results_file)

'''********************** Question 5 Runs **********************'''
if run_pr5:

    # Array for Project Report Question 5 (Re-Use A's from 4)
    V5 = [1]
    for k in range(2, 32, 2):
        V5.append(k)

    # Delete contents of test results file
    with open(PR5_exp_results_file, 'w') as fw:
        fw.write("Experimental Time Runs\n")
    print("\n******Project Report Question 5******\nRunning Experiment...")

    # Algorithm 1: Change Slow
    with open(PR5_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 1: Change Slow\n")
    print("\nAlgorithm 1: Change Slow")

    RUNEXPERIMENT(algs.ChangeSlow, A_small[:50], V5, 1, True, PR5_exp_results_file)

    # Algorithm 2: Change Greedy
    with open(PR5_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 2: Change Greedy\n")
    print("\nAlgorithm 2: Change Greedy")

    RUNEXPERIMENT(algs.ChangeGreedy, A_large, V5, 1, True, PR5_exp_results_file)

    # Algorithm 3: Change DP
    with open(PR5_exp_results_file, 'a') as fw:
        fw.write("\nAlgorithm 3: Change DP\n")
    print("\nAlgorithm 3: Change DP")

    RUNEXPERIMENT(algs.ChangeDP, A_medium, V5, 1, True, PR5_exp_results_file)


'''********************** Question 7 Runs **********************'''
if run_pr7:

    # Question 7 Number of Denominations vs Time
    den_array = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    target = [75]

    with open(PR7_exp_results_file, 'w') as fw:
        fw.write("Question 7: Denominations versus Time\n")
    print("\n******Project Report Question 7******\nRunning Experiment...")

    for i in range(3, len(den_array) - 1, 1):
        print_header = False

        if i == 3:
            print_header = True

        # Algorithm 1: Change Slow
        if print_header:
            with open(PR7_exp_results_file, 'a') as fw:
                fw.write("\nAlgorithm 1: Change Slow\n")
            print("\nAlgorithm 1: Change Slow")
        RUNEXPERIMENT(algs.ChangeSlow, target, den_array[:i], 1, print_header, PR7_exp_results_file)

    for i in range(3, len(den_array) - 1, 1):
        print_header = False
        if i == 3:
            print_header = True

        # Algorithm 2: Change Greedy
        if print_header:
            with open(PR7_exp_results_file, 'a') as fw:
                fw.write("\nAlgorithm 2: Change Greedy\n")
            print("\nAlgorithm 2: Change Greedy")
        RUNEXPERIMENT(algs.ChangeGreedy, target, den_array[:i], 150000, print_header, PR7_exp_results_file)

    for i in range(3, len(den_array) - 1, 1):
        print_header = False
        if i == 3:
            print_header = True

            # Algorithm 3: Change DP
        if print_header:
            with open(PR7_exp_results_file, 'a') as fw:
                fw.write("\nAlgorithm 3: Change DP\n")
            print("\nAlgorithm 3: Change DP")
        RUNEXPERIMENT(algs.ChangeDP, target, den_array[:i], 15000, print_header, PR7_exp_results_file)
