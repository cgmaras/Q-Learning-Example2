"""
Created on Oct 8th
@author: cgmaras
"""
# module to communicate with terminal
import os
import shutil
import glob
import re
import time

def submit():
    class run():
      """
        Runs the numbered inputs decks
      """
      def __init__(self):
        """
          Main Function
        """
        # Get the working directory
        self.workingDir = os.getcwd()
        print (self.workingDir)
        nJobs = self.copyBase()

        self.submit(nJobs)

      def copyBase(self):
        """
          Copies the template files
        """
        i = 0
        # go to the Queue directory
        os.chdir(os.path.join(self.workingDir,'Queue'))

        # get the file names located in Queue directory
        fileList = glob.glob('*')

        print ('The files contained in Queue are: ', fileList)
        for file in fileList:
          # check, one by one, if a file name contains 'new_core'
          if re.search('new_core',file):
            i += 1

        # go back to working directory
        os.chdir(self.workingDir)
        # copy the input files into "simulation" direction
        for j in range(1, i + 1):
          dirName = 'new_core' + str(j)
          fileName = dirName + '.inp'
          # --------------------------------------------------
          # create directories
          # --------------------------------------------------
          # check if the newCore directories exit
          if (os.path.exists(os.path.join('SimRuns',dirName))):
            # If the core directories exist, print warning
            print ('WARNING: THE DIRECTORIES ALREADY EXISTED')
          else:
          # if the core directrories do not exit, create them
            os.system('mkdir SimRuns')
            os.system('mkdir SimRuns/'+dirName)
          os.system('cp Base_Files/cms.pwr-all.lib SimRuns/' + dirName)
          os.system('cp Base_Files/cycle1.res SimRuns/' + dirName)
          # --------------------------------------------------
          # Copy input files
          # --------------------------------------------------
          os.system('cp Queue/' +  fileName + '   SimRuns/' + dirName)
          os.system('cp  Base_Files/run.sh    SimRuns/' + dirName)

          # parse the slurm file:
          self.parse(dirName,os.path.join(self.workingDir,os.path.join('SimRuns',os.path.join(dirName,fileName))))
        return i

      def parse(self,dirName, fileName):
        """
          opens the SLURM bash script and inject executable
          @ In, fileName, string, input file name
          @ Out, None
        """
        # go to the sub-directory ./newRun/new_core1
        os.chdir(os.path.join('SimRuns',dirName))
        # open the bash file and append at the end the simulate execution
        with open('run.sh', 'a+') as inp:
          inp.write('simulate3 '+ fileName)
          inp.write("   \n")
          inp.write('echo "Job Finished"')
          inp.write("   \n")
          inp.write('echo 1>"check.txt"')
        self.cleanUp(dirName + '.out')
        os.chdir(self.workingDir)
        return

      def cleanUp(self, f):
        """
          cleanUp files
          @ In, f, file name to remove
          @ Out, None
        """
        os.system('rm ' +  f)

      def submit(self, nJobs):
        """
          Submits the jobs
        """
        for i in range(1,nJobs + 1 ):
          # go to the directory of interest
          dirName = 'new_core' + str(i)
          fileName = 'new_core' + str(i) + '.inp'
          os.chdir(os.path.join(self.workingDir,os.path.join('SimRuns',dirName)))
          #print (os.getcwd()  )
          #print (os.path.join(self.workingDir,os.path.join('newRun',dirName)))
          os.system ('sbatch run.sh')


    run = run()

#os.system('sbatch copy.sh')
