import numpy as np
import os
import scipy.misc as misc
import random
#------------------------Class for reading training and  validation data for materials in vessels data set---------------------------------------------------------------------
class Data_Reader:


################################Initiate folders were files are and list of train images############################################################################
    def __init__(self,ImageDir,LabelDir, BatchSize,Suffle=True):
        self.NumFiles = 0 # Number of files in reader
        self.Epoch = 0 # Training epochs passed
        self.itr = 0 #Iteration
        #Image directory
        self.Image_Dir=ImageDir
        # Directories  for labels of various annotations modes

        self.Vessel_Label_Dir = LabelDir+"/VesselLabels/"
        self.Phase_Label_Dir =  LabelDir+"/FillLevelLabels/"
        self.LiquidSolid_Label_Dir =  LabelDir+"/LiquidSolidLabels/"
        self.AllPhases_Label_Dir =  LabelDir+"/ExactPhaseLabels/"
        self.OrderedFiles=[]
        # Read list of all files
        self.OrderedFiles += [each for each in os.listdir(self.Image_Dir) if each.endswith('.PNG') or each.endswith('.JPG') or each.endswith('.TIF') or each.endswith('.GIF') or each.endswith('.png') or each.endswith('.jpg') or each.endswith('.tif') or each.endswith('.gif') ] # Get list of training images
        self.BatchSize=BatchSize #Number of images used in single training operation
        self.NumFiles=len(self.OrderedFiles)
        self.OrderedFiles.sort() # Sort files by names
######################################Read next batch of images and labels with no augmentation######################################################################################################
    def ReadNextBatchClean(self): #Read image and labels without agumenting
        if self.itr>=self.NumFiles: # End of an epoch
            self.itr=0
            self.Epoch+=1
        batch_size=np.min([self.BatchSize,self.NumFiles-self.itr])

        Sy=1
        Sx=1

#-----------Augument Images and labeles-------------------------------------------------------------------
        Images = []
        LabelsVessel = []
        LabelsOnePhase = []
        LabelsSolidLiquid = []
        LabelsAllPhases = []

        for f in range(batch_size):
#.............Read image and labels from files.........................................................
           Img = misc.imread(self.Image_Dir + "/" + self.OrderedFiles[self.itr])
           Img = Img[:, :, 0:3]
           LbName = self.OrderedFiles[self.itr][0:-4] + ".png"
           LBVessel = misc.imread(self.Vessel_Label_Dir + "/" + LbName)
           LBPhase = misc.imread(self.Phase_Label_Dir + "/" + LbName)
           LBLiquidSolid = misc.imread(self.LiquidSolid_Label_Dir + "/" + LbName)
           LBAllPhases = misc.imread(self.AllPhases_Label_Dir + "/" + LbName)
           self.itr += 1
#............Set Batch size according to first image...................................................
           if f==0:
                Sy,Sx=LBVessel.shape
                Images = np.zeros([batch_size,Sy,Sx,3], dtype=np.float)
                LabelsVessel = np.zeros([batch_size,Sy,Sx,1], dtype=np.int)
                LabelsOnePhase = np.zeros([batch_size, Sy,Sx, 1], dtype=np.int)
                LabelsSolidLiquid = np.zeros([batch_size, Sy,Sx, 1], dtype=np.int)
                LabelsAllPhases = np.zeros([batch_size,Sy,Sx, 1], dtype=np.int)
#..........Resize and strecth image and labels....................................................................
           Img = misc.imresize(Img, [Sy,Sx], interp='bilinear')
           LBVessel = misc.imresize(LBVessel, [Sy, Sx], interp='nearest')
           LBPhase = misc.imresize(LBPhase, [Sy, Sx], interp='nearest')
           LBLiquidSolid = misc.imresize(LBLiquidSolid, [Sy, Sx], interp='nearest')
           LBAllPhases = misc.imresize(LBAllPhases, [Sy, Sx], interp='nearest')
#...................Load image and label to batch..................................................................

           Images[f]=Img
           LabelsVessel[f,:,:,0]=LBVessel
           LabelsOnePhase[f,:,:,0]=LBPhase
           LabelsSolidLiquid[f,:,:,0]=LBLiquidSolid
           LabelsAllPhases[f,:,:,0]=LBAllPhases
#.................Return batch............................................................................
        return Images, LabelsVessel, LabelsOnePhase, LabelsSolidLiquid, LabelsAllPhases




