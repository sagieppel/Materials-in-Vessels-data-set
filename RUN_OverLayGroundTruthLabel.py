#Read images and annotation from Materials in vessels dataset and overlay the label on the image
# Download the materials in vessels dataset
#and  set Label_Dir and Image dir to the main dataset dir and the image dir respectively
# The overlay labes should appear in the OutDir
#--------------------------------------------------------------------------------------------------------------------
Label_Dir="Materials_In_Vessels/"# Main folder of the dataset
Image_Dir="Materials_In_Vessels/Train_Images/"#Images of the dataset
OutDir="Output/" # Library where the output images will be display
#-------------------------------------------------------------------------------------------------------------
import numpy as np
import scipy.misc as misc
import os
import Data_Reader
import OverrlayLabelOnImage as Overlay
#-------------------------------------------------------------------------------------------------------------------
NUM_CLASSES = 15+2+3+4 #Total number of classes in data_Set
################################################################################################################################################################################
Reader = Data_Reader.Data_Reader(Image_Dir, Label_Dir, 1) #initiate data set reader
if not os.path.exists(OutDir): os.makedirs(OutDir)
#---------------------------------------------------------------------------------------------------------------
print("Saving output to:" + OutDir)
fim = 0
 #---------------------------------------------------------------------------------------------------------------
print("Start Predicting " + str(Reader.NumFiles) + " images")
while (Reader.itr < Reader.NumFiles):
        print(str(fim * 100.0 / Reader.NumFiles) + "%")
        fim += 1
# ........................................Read image.................................................................................
        FileName=Reader.OrderedFiles[Reader.itr]
        Images, LabelsVessel, LabelsOnePhase, LabelsSolidLiquid, LabelsAllPhases = Reader.ReadNextBatchClean()  # Read images and ground truth annotation
# ............................Overlay label on image according to several set of labels and save in OutDir...............................................................
        w=1
        OverlayImg=np.concatenate((Images[0], Overlay.OverLayLiquidSolid(Images[0],LabelsVessel[0,:,:,0],w),Overlay.OverLayFillLevel(Images[0],  LabelsOnePhase[0,:,:,0], w),Overlay.OverLayLiquidSolid(Images[0],  LabelsSolidLiquid[0,:,:,0], w), Overlay.OverLayExactPhase(Images[0], LabelsAllPhases[0,:,:,0], w)), axis=1)
        #misc.imshow(OverlayImg) #Save image with overlay label
        misc.imsave(OutDir + FileName,OverlayImg)#Save image with overlay label