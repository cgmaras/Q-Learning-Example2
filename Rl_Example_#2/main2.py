import time
import os
import user_input
"""
Created on Oct 17th
@author: cgmaras
"""
# This file controls the controller for the RL/SIMULATE algorithm
# First 3 parts include:
# 1.) Input Generation
# 2.) Job Submittal (Simulate)
# 3.) Output Postproccessing
def submit2():
    # varify the path using getcwd()
    cwd = os.getcwd()
    # print the current directory
    print("Current working directory is:", cwd)

    # 1.) Creating Simulate input files
    import InputGen2
    from InputGen2 import inputgen
    inputgen()

    # 2.) Submitting Simulate jobs to cluster and creating file structure
    os.chdir('/home/cgmaras/Python/CameronRL/')
    import simulate
    from simulate import submit
    submit()
    os.chdir('/home/cgmaras/Python/RLsim_Code/')
    # 3.) Reading and parsing output files to produce summary
    # os.chdir('/home/cgmaras/Python/RLsim_Code/')
    # import Output_Search
    # from Output_Search import output
    # output()




# old format
#
#
#
# # 1.) Creating Simulate input files
#
# print("Running Input Generation......")
# os.system('python3 InputGen2.py')
#
# # 2.) Submitting Simulate jobs to cluster and creating file structure
# os.chdir('/home/cgmaras/Python/RLsim_Code/')
# print("Submitting jobs......")
# os.system('python3 simulate.py')
#
#
# # 3.) Reading and parsing output files to produce summary
# os.chdir('/home/cgmaras/Python/RLsim_Code/')
# print("Analyzing output files.......")
# os.system('python3 Output_Search.py')
