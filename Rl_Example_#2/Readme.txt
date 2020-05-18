Reinforcement Learning (Q-Learning) Example

This is an example of the RL/Q-Learning Framework developed by Cameron Maras and Gregory Delipei.

This code works in conjuction with the Studsvik SIMULATE-3 nodal code using pre-defined fuel inventories.

Example #2 - This example contains only Q-learning results with 5 Epochs and 5 Iterations per Epoch (25 total SIMULATE runs).




The results from the example can be found in results.txt, which contains some SIMULATE output data and Q-learning results for each step.

The file user_input.py contains the user defined input for the SIMULATE portion of the code.

The file rl_pwr.py contains the main RL algorithm controller, with user defined options for the Q-learning settings.

The directory "Base Files" contains the following needed for the simulation:
	- sample restart (.res) file for SIMULATE-3 
	- a sample input (.inp) file for SIMULATE-3 
	- a sample shell script (.sh) for SLURM 
	- fuel library file (.lib) from CASMO code suite for pre-defined fuel inventory
	
The directory "Queue" contains the SIMULATE input file(s) created by the code, ready for submission via the RDFMG cluster.

The directory "SimRuns" contains subdirectories for each of the SIMULATE calculation runs, including copied files from "Base Files" that are required.

The directory "Outputs" contains the collected SIMULATE output files from the user specified number of calculations.

