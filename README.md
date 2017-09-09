# Dataset of materials within glass vessels
New [data set](https://drive.google.com/file/d/0B6njwynsu2hXRFpmY1pOV1A4SFE/view?usp=sharing) of images of materials in transparent vessels in chemistry laboratory setting is presented. This data set contains a thousand images with pixel-wise annotation according to categories ranging from filled and empty to the exact physical phase of the material inside the vessel (liquid, solid, powder, foam, vapors…). 

The data set can be downloaded from each of the following links:
1) https://drive.google.com/file/d/0B6njwynsu2hXRFpmY1pOV1A4SFE/view?usp=sharing
2) https://mega.nz/#!4DQA3LTC!z2jA88Ve_K5f32AaNFrBOWdCtx8CXq65j3wt0nvzH-0

The data set is discussed in the paper: [Setting an attention region for convolutional neural networks using region selective features, for recognition of materials within glass vessels](https://arxiv.org/abs/1708.08711)
## General 
The handling of materials in glassware vessels is the main task in chemistry laboratory research as well as a large number of other activities such as beverage handling. Visual recognition of the physical phase of the materials is essential for many methods ranging from a simple task such as fill-level evaluation to the identification of more complex properties such as solvation, precipitation, crystallization and phase separation. To help train neural nets for this task, a new data set was created. The data set contains a thousand images of materials, in different phases and involved in different chemical processes, in a laboratory setting.
## Dataset labels
Each pixel in each image is labeled according to several layers of classification given below (Figure 1): 

a. Vessel/Background: For each pixel assign value of 1 if it part of the vessel and 0 otherwise. This label was used as ROI map for valve filters method. 

b. Filled/Empty: similar to above but also distinguish between filled and empty regions of the vessel. Assign for each pixel one of the three values: 0) Background, 1) Empty vessel. 2) Filled vessel. 

c. Phase type: Similar to above but distinguish between liquid and solid regions of the filled vessel. Assign for each pixel one of the four values: 0) Background, 1) Empty vessel. 2) Liquid. 3) Solid.

d. The exact physical phase of material: Similar to above but distinguish between specific physical phases classes. For each pixel assign one of 15 values: 1) Background. 2) Empty Vessel. 3) Liquid. 4) Liquid Phase two (in case more than one phase of liquid appear in the vessel). 5) Suspension. 6) Emulsion. 7) Foam. 8) Solid. 9) Gel. 10) Powder. 11) Granular. 12) Bulk. 13) Solid and liquid mixture. 14) Solid Phase two (in case more than one phase of solid exist in the vessel). 15) Vapor.

The annotations are given as images in the size of the original image where the pixel value is the class number. 
![](/Figure1.jpg)

## Validation/Testing set:
The data set is divided into training and validation sets. The testing set is used to test the predictions of nets trained using the training set. The testing set is itself divided into two subsets; one contains images extracted from the same YouTube channels as the training set, and therefore was taken under similar conditions as the training images. The second subset contains images extracted from YouTube channels not included in the training set, and hence contains images taken under different conditions from those used to train the net. The purpose of the second set is to measure the overfitting of the net to the specific conditions of the training set.

## Creating the dataset
The creation of a large number of images with a variety of chemical processes and settings could have been a daunting task. Luckily, several YouTube channels dedicated to chemical experiments exist which offer high-quality footage of chemistry experiments. Thanks to these channels, including NurdRage, NileRed, ChemPlayer, it was possible to collect a large number of high-quality images in a short time. Pixel-wise annotation of these images was another challenging task and was performed by Alexandra Emanuel and Mor Bismuth. 

## Supporting scripts
This repository contains three python script for reading and displaying the dataset.
### Data_Reader.py:
Reader for loading images and annotation from data set
### OverrlayLabelOnImage.py
Overlay the annotation/label on the image for display purpose
### RUN_OverLayGroundTruthLabel.py
A simple script that use the above scripts to read the annotations and images from the data set, and overlay the annotation on the image for display purpose.


