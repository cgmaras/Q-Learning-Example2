import random
from random import choice
# --------------- Primary Input File for RL/SIMULATE Code ---------------------------------
#
#
#

class Input:

    def __init__(self):
        self.base = '/home/cgmaras/Python/RLsim_Code/Base_Files/base.inp'       # Base Input File Directory
        self.lib = '/home/cgmaras/Python/RLsim_Code/Base_Files/cms.pwr-all.lib' # Fuel Repository directory
        self.res = '/home/cgmaras/Python/Base_Files/cycle1.res'                 # Initial Restart file
        self.Runs = 1                                                           # Number of SIMULATE Runs
        self.FA = 157                                                           # Core Configuration (Number of Fuel Assemblies)
        self.out = '/home/cgmaras/Python/CameronRL/Outputs'                    # Output File Directory


## core layout
FuelMap = [8,8,7,7,6,5,4,2,0]
RefMap = [1,1,2,1,2,2,2,3,3]
BaffleMap = [0,0,0,1,1,2,3,4,6]



Fuel_2 = {}
Fuel_3 = {}
Fuel_4 = {}
Fuel_5 = {}
Fuel_6 = {}
Fuel = {}
Fuel_2 = {'Flag': 2, 'Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 16, 'INV': 50}
Fuel_3 = {'Flag': 2, 'Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 16, 'INV': 50}
Fuel_4 = {'Flag': 2, 'Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16, 'INV': 50}
Fuel_5 = {'Flag': 2, 'Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 16, 'INV': 50}
Fuel_6 = {'Flag': 2, 'Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16, 'INV': 50}
Fuel = {'2':Fuel_2, '3':Fuel_3, '4':Fuel_4, '5':Fuel_5, '6':Fuel_6}

# fuel types
Types = [2,3,4,5,6]

#user defined loading LoadingPattern
LoadingPattern = [[4, 5, 2, 2, 2, 6, 6, 5, 1], 
                  [6, 5, 3, 2, 3, 2, 3, 5, 1], 
                  [2, 3, 2, 4, 2, 3, 5, 1, 1], 
                  [2, 2, 4, 2, 3, 5, 5, 1, 0], 
                  [2, 3, 2, 3, 2, 5, 1, 1, 0], 
                  [6, 2, 3, 5, 5, 1, 1, 0, 0], 
                  [6, 3, 5, 5, 1, 1, 0, 0, 0], 
                  [5, 5, 1, 1, 1, 0, 0, 0, 0], 
                  [1, 1, 1, 0, 0, 0, 0, 0, 0]] 





class State4(object):
    def __init__(self):
    # middle 4 FA - initial state
        self.State4 = [4,3,6,3]









#################################################################################################################################################
#Reflector = ["1,9","2,9","3,8","3,9","4,8","5,7","5,8","6,6","6,7","7,5","7,6","8,3","8,4","8,5","9,1","9,2","9,3"]
#Baffle = ["4,9","5,9","6,9","7,9","8,9","9,9","9,4","9,5","9,6","9,7","9,8","8,6","8,7","8,8","7,7","7,8","6,8"]


#class Fuel:
#  def __init__(self, Type=None, Enrichment=None, BU=None, BP=None, Volume=None):
#    self.Type = Type                                                            # Fuel Type from Project
#    self.Enrichment = Enrichment                                                # Enrichment of FA in U235 w/o
#    self.BU = BU                                                                # Burnup
#    self.BP = BP                                                                # Number of Burnable Poison Rods
#    self.Volum = Volume                                                         # Number of FA in inventory
#    self.Flag = "2"                                                             # flag for inputgen

#Fuel_2 = Fuel(2,2.0,0,0,50)
#Fuel_3 = Fuel(3,2.5,0,0,50)
#Fuel_4 = Fuel(4,2.5,0,16,50)
#Fuel_5 = Fuel(5,3.2,0,0,50)
#Fuel_6 = Fuel(6,3.2,0,16,50)
#print(Fuel_5.Type)
