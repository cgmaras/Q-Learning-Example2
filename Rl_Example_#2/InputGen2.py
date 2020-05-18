import numpy as np
import os
import random
import user_input
from user_input import Input
from user_input import Fuel
from user_input import Types
from user_input import LoadingPattern
from user_input import FuelMap
from user_input import RefMap
from user_input import BaffleMap
from random import choice
dummy = Input()
#fuelin = Fuel()


def inputgen():
    print("Started input gen...")
    # with open('new_input', 'w') as f1:
    #   with open('workymcworker.inp', 'r+') as f:
    #       contents = f.readlines()
    #       for x in contents:
    #           print(x)
    #       f1.writelines(contents)
    filename3 = '/home/cgmaras/Python/RLsim_Code/user_input.py'
    os.makedirs('Queue')
    Runs = dummy.Runs
    filename2 = dummy.base
    with open(filename2) as search:
        lines = search.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()


    #print(FuelMap)
    # getting fuel coords
    fuelpos = []
    refpos = []
    bafpos = []
    length = len(FuelMap)
    for i in range(length):
        length2 = FuelMap[i]
        for j in range(length2):
            fuelpos.append(str(i+1) + "," + str(j+1))
    #print(fuelpos)

    # getting reflector coords
    length = len(FuelMap)
    for i in range(length):
        length2 = FuelMap[i]
        length3 = RefMap[i]
    #
        for k in range(length3):
            refpos.append(str(i+1) + "," + str(length2+k+1))
    #print(refpos)

    # getting baffle coords
    length = len(FuelMap)
    for i in range(length):
        length2 = FuelMap[i]
        length3 = RefMap[i]
        length4 = BaffleMap[i]
    #
        for k in range(length4):
            bafpos.append(str(i+1) + "," + str(length2+length3+1+k))
    #print(bafpos)

# reflector and baffle positions
# Reflector = ["1,9","2,9","3,8","3,9","4,8","5,7","5,8","6,6","6,7","7,5","7,6","8,3","8,4","8,5","9,1","9,2","9,3"]
# Baffle = ["4,9","5,9","6,9","7,9","8,9","9,9","9,4","9,5","9,6","9,7","9,8","8,6","8,7","8,8","7,7","7,8","6,8"]




    # creating dictionaries for each position in core
    main, row = {}, {}
    x = int(Runs)                                               # number of different LPs to be made
    for k in range(x):
        for i in range(1,10):
            for j in range(1,10):
                name = str(i) + "," + str(j)
                main[name] = {}
                if name in refpos:                   # using flag to determine fuel, reflector, or baffle
                    main[name]['Flag'] = 1
                elif name in bafpos:
                    main[name]['Flag'] = 0
                else:
                    main[name]['Flag'] = 2

                if main[name]['Flag'] == 2:
                    main[name]['Fuel Type'] = LoadingPattern[i-1][j-1]       # fuel type based on 412/512 project description, using random dist for now
                    if main[name]['Fuel Type'] == 2:
                        main[name]['Enrichment'] = str(Fuel['2']['Enrichment'])                          # assembly averaged enrichment (u235 w/o)
                        main[name]['BP'] = Fuel['2']['BP']                                  # number of burnable poison rods in assembly
                        main[name]['BU'] = Fuel['2']['BU']
                    elif main[name]['Fuel Type'] == 3:
                        main[name]['Enrichment'] = str(Fuel['3']['Enrichment'])
                        main[name]['BP'] = Fuel['3']['BP']
                        main[name]['BU'] = Fuel['3']['BU']
                    elif main[name]['Fuel Type'] == 4:
                        main[name]['Enrichment'] = str(Fuel['4']['Enrichment'])
                        main[name]['BP'] = Fuel['4']['BP']
                        main[name]['BU'] = Fuel['4']['BU']
                    elif main[name]['Fuel Type'] == 5:
                        main[name]['Enrichment'] = str(Fuel['5']['Enrichment'])
                        main[name]['BP'] = Fuel['5']['BP']
                        main[name]['BU'] = Fuel['5']['BU']
                    else:
                        main[name]['Enrichment'] = str(Fuel['6']['Enrichment'])
                        main[name]['BP'] = Fuel['6']['BP']
                        main[name]['BU'] = Fuel['6']['BU']
                elif main[name]['Flag'] == 1:
                    main[name]['Fuel Type'] = 1
                    main[name]['BU'] = 0
                    main[name]['Enrichment'] = 0
                    main[name]['BP'] = 0
                else:
                    main[name]['Fuel Type'] = 0
                    main[name]['BU'] = 0                # non-fuel filling with zeros
                    main[name]['Enrichment'] = 0
                    main[name]['BP'] = 0
                #print(main)
            row[i] = '\'FUE.TYP\'  '+ str(i) +',   '
            for j in range(1,10):
                row[i] += str(main[str(i) + "," + str(j)]['Fuel Type']) + '   '
            row[i] = row[i][:-3] + '/' + '\n'

        with open('/home/cgmaras/Python/CameronRL/Queue/new_core' + str(k+1) + '.inp', 'w') as f:
            for i in range(2):
                f.writelines(lines[i] + '\n')
            for i in range(1,10):
                f.writelines(row[i])
            for i in range(11,20):
                f.writelines(lines[i] + '\n')




    print("Finished input gen...")








    #print(main)
    ###############################################################################
    # above needs to be pulled and used to write like below
    ###############################################################################

    # reading SIMULATE base input file
    # filename2 = 'C:/Users/cgmaras/Desktop/Python/base.inp'
    # with open(filename2, 'r') as search:
    #     lines = search.readlines()
    #     for i in range(len(lines)):
    #         lines[i] = lines[i].rstrip()
    #
    # # creating core LP map
    # loading = {'core1':2, 'core2':6,'core3':3,'core4':4}
    # print(list(loading.keys()))
    # for core in list(loading.keys()):
    #   input = np.zeros((9,9))
    #   for i in range(9):
    #       input[i] = lines[i+2][16:49].split()
    #
    #   for i in range(2,8):
    #       input[input==i]=loading[core]
    #
    # # converting input array to strings for building new input file
    #   input_string = {}
    #   for i in range(9):
    #       input_string[i] = ''
    #       for j in range(9):
    #           input_string[i] += (str(int(input[i,j])) + '   ')
    #       input_string[i] = input_string[i][:-3]
    #
    # # writing new SIMULATE input files
    #   with open('C:/Users/cgmaras/Desktop/Python/Core Queue/new_' + core + '.inp', 'w') as f:
    #       for i in range(2):
    #           f.writelines(lines[i] + '\n')
    #       for i in range(9):
    #           f.writelines('\'FUE.TYP\'  '+ str(i+1) +',   ' + input_string[i] + '/' + '\n')
    #       for i in range(11,20):
    #           f.writelines(lines[i] + '\n'
