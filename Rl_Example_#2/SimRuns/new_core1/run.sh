#!  /bin/sh
#
#PBS -N simulate
#PBS -e error.dat
#PBS -o info.dat
#PBS -p gradq
#PBS -l nodes=1:ppn=1
cd $SLURM_SUBMIT_DIR
echo $SLURM_SUBMIT_DIR
#  Make sure we're in right directory
date

echo "starting job..."

simulate3 /home/cgmaras/Python/CameronRL/SimRuns/new_core1/new_core1.inp   
echo "Job Finished"   
echo 1>"check.txt"