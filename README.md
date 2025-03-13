# City Builder 



<!-- Image -->

![citescape catppuccin](https://github.com/JoeHarper-tech/VFX-6102-citybuilder/blob/main/pictures/cat_evening-sky.png?raw=true)

<!-- Title -->

## A tool for sideFX Houdini that creates a template city
&nbsp; <br>


<!-- Installation -->
<details align="center">
 <summary>Installation</summary>
    
 <p align="left">
  
 &nbsp; 
 ### Step one
 <img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/installation/tut01.png?raw=true" width="500">\
 right click in the toolbar and click new tool <br>
 &nbsp; 
 ## 

 ### Step two
 <img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/installation/step02.png?raw=true" width="500">\
 Fill in the Name and Label of the tool, add an icon aswell if you want :D <br>
 &nbsp; 
 ##
 
 ### Step three
 <img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/installation/step03.png?raw=true" width="500">\
 Press the script tab, then paste the [script](https://github.com/kuisux/VFX-6102-citybuilder/blob/main/cityBuilder_v001.py) into the box <br>
 &nbsp; 
 ##


 ### Step four
 <img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/installation/step04.png?raw=true" width="500">\
 Press the accpet button <br>
 &nbsp; 
 ##

</p>
</details>

<!-- Usage -->
<details align="center">
<summary>Usage</summary>

### Step One
<img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/Usage/usageOne.png?raw=true" width="500">\
Press the tool from the tool shelf <br>
&nbsp;
##

### Step two
<img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/Usage/usageTwo.png?raw=true" width="500">\
Fill in the window with the desired parameters <br>
&nbsp;
##
 
</details>

<!-- Code -->
<details align="center">
<summary>Code</summary>

<div align="left">
 
```python
from re import X
#-----------------------------------------------------------------------------------------------#
#         ,-----.,--.  ,--.               ,-----.          ,--.,--.   ,--.                      #
#        '  .--./`--',-'  '-.,--. ,--.    |  |) /_ ,--.,--.`--'|  | ,-|  | ,---. ,--.--.        #
#        |  |    ,--.'-.  .-' \  '  /     |  .-.  \|  ||  |,--.|  |' .-. || .-. :|  .--'        #
#        '  '--'\|  |  |  |    \   '      |  '--' /'  ''  '|  ||  |\ `-' |\   --.|  |           #
#         `-----'`--'  `--'  .-'  /       `------'  `----' `--'`--' `---'  `----'`--'           #
#                            `---'                                                              #
#-----------------------------------------------------------------------------------------------#


from PySide2 import QtCore
from PySide2 import QtWidgets
import hou
import json
import os
import random


class cityBuilder(QtWidgets.QWidget):
    def __init__(self, parent=None):

#------------------------------------------------------------------------------------------------------------------
# Creating the Vertical Layout

        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('City Builder')
        self.vBox = QtWidgets.QVBoxLayout()

#------------------------------------------------------------------------------------------------------------------
# Creating the widgets in the UI starting with Building Density

# Label
        hboxBuildingDensity = QtWidgets.QHBoxLayout()
        self.labelBuildingDensity = QtWidgets.QLabel(
            'How many buildings would you like'
            )
        self.labelBuildingDensity.setMinimumWidth(175)
        hboxBuildingDensity.addWidget(self.labelBuildingDensity)

# Text box

        self.textInputBuildingDensity = QtWidgets.QLineEdit(self)
        self.textInputBuildingDensity.setMinimumWidth(175)
        hboxBuildingDensity.addWidget(self.textInputBuildingDensity)
        self.vBox.addLayout(hboxBuildingDensity)

#------------------------------------------------------------------------------------------------------------------
# Max Floors

# Label
        hboxMaxFloors = QtWidgets.QHBoxLayout()
        self.labelMaxFloors = QtWidgets.QLabel(
            'whats the maximum ammount of floors for a building'
            )
        self.labelMaxFloors.setMinimumWidth(175)
        hboxMaxFloors.addWidget(self.labelMaxFloors)

# Text Box

        self.textInputMaxFloors = QtWidgets.QLineEdit(self)
        self.textInputMaxFloors.setMinimumWidth(175)
        hboxMaxFloors.addWidget(self.textInputMaxFloors)
        self.vBox.addLayout(hboxMaxFloors)

#------------------------------------------------------------------------------------------------------------------
# Min Floors

# Label
        hboxMinFloors = QtWidgets.QHBoxLayout()
        self.labelMinFloors = QtWidgets.QLabel(
            'what are the minimum ammount of floors for a building'
            )
        self.labelMinFloors.setMinimumWidth(175)
        hboxMinFloors.addWidget(self.labelMinFloors)

# Text Box

        self.TextInputMinFloors = QtWidgets.QLineEdit(self)
        self.TextInputMinFloors.setMinimumWidth(175)
        hboxMinFloors.addWidget(self.TextInputMinFloors)
        self.vBox.addLayout(hboxMinFloors)

#------------------------------------------------------------------------------------------------------------------
# Location

# Label
        hboxLocation = QtWidgets.QHBoxLayout()
        self.LabelLocation = QtWidgets.QLabel(
            'where would you like to placce the city'
            )
        self.LabelLocation.setMinimumWidth(175)
        hboxLocation.addWidget(self.LabelLocation)

# X location
        self.textInputLocationX = QtWidgets.QLineEdit(self)
        self.textInputLocationX.setMinimumWidth(50)

# Y Location
        self.textInputLocationY = QtWidgets.QLineEdit(self)
        self.textInputLocationY.setMinimumWidth(50)

# Z Location
        self.textInputLocationZ = QtWidgets.QLineEdit(self)
        self.textInputLocationZ.setMinimumWidth(50)
        
        hboxLocation.addWidget(self.textInputLocationX)
        hboxLocation.addWidget(self.textInputLocationY)
        hboxLocation.addWidget(self.textInputLocationZ)
        self.vBox.addLayout(hboxLocation)

#------------------------------------------------------------------------------------------------------------------
# Snap to ground
        '''
# Label
        
        hboxSnap = QtWidgets.QHBoxLayout()
        self.LabelSnap = QtWidgets.QLabel(
            'snap to ground?'
            )
        self.LabelSnap.setMinimumWidth(25)
        hboxSnap.addWidget(self.LabelSnap)

#check box
        self.checkBoxSnap = QtWidgets.QCheckBox()
        self.checkBoxSnap.setMinimumWidth(25)
        hboxSnap.addWidget(self.checkBoxSnap)
        self.vBox.addLayout(hboxSnap)     
        '''   

#label
        hboxSnapMenu = QtWidgets.QHBoxLayout()
        self.ddlLabel = QtWidgets.QLabel(
            'object to snap to'
        )
        self.ddlLabel.setMinimumWidth(175)
        hboxSnapMenu.addWidget(self.ddlLabel)
        
#drop down
        self.DdlSnap = QtWidgets.QComboBox()
        self.DdlSnap.addItem('None')
        self.DdlSnap.addItem('One')
        self.DdlSnap.addItem('two')
        self.DdlSnap.setMinimumWidth(175)
        hboxSnapMenu.addWidget(self.DdlSnap)
        self.vBox.addLayout(hboxSnapMenu)


#------------------------------------------------------------------------------------------------------------------
#Presets

#buttons
        hboxPresets = QtWidgets.QHBoxLayout()
        self.loadPresetBtn = QtWidgets.QPushButton('Load Preset', self)
        self.savePresetBtn = QtWidgets.QPushButton('Save Preset', self)
        hboxPresets.addWidget(self.loadPresetBtn)
        hboxPresets.addWidget(self.savePresetBtn)
        self.vBox.addLayout(hboxPresets)


#-------------------------------------------------------------------------------------------------------------------
#BuildProject

        hboxBuildProject = QtWidgets.QHBoxLayout()
        self.buildProjectBtn = QtWidgets.QPushButton("Build", self)
        self.buildProjectBtn.clicked.connect(self.buildProject)
        hboxBuildProject.addWidget(self.buildProjectBtn)
        self.vBox.addLayout(hboxBuildProject)


#-------------------------------------------------------------------------------------------------------------------
#Defines
        self.setLayout(self.vBox)

    def textHasChangedBuildingDensity(self):
        buildingDensity = self.textInputBuildingDensity.text()

    def textHasChangedMaxFloors(self):
        maxFloors = self.textInputMaxFloors.text()

    def textHasChangedMinFloors(self):
        minFloors = self.TextInputMinFloors.text()

    def textHasChangedLocationX(self):
        locationX = self.textInputLocationX.text()

    def textHasChangedLocationY(self):
        locationY = self.textInputLocationY.text()

    def textHasChangedLocationZ(self):
        locationZ = self.textInputLocationZ.text()
    
    def stateHasChangedSnapObj(self):
        snapObj = self.DdlSnap

    def stateHasChangedLoadPreset(self):
        loadPreset = self.loadPresetBtn

    def stateHasChangedSavePreset(self):
        savePreset =  self.SavePresetBtn

    def buildProject(self):
#-------------------------------------------------------------------------------------------------------------------
#Main Function
            
        #Variables

        buildingDensity = self.textInputBuildingDensity.text()
        maxFloors = self.textInputMaxFloors.text()
        minFloors = self.TextInputMinFloors.text()
        locationX = self.textInputLocationX.text()
        locationY = self.textInputLocationY.text()
        locationZ = self.textInputLocationZ.text()
        snapObj = self.DdlSnap
        loadPreset = self.loadPresetBtn
        savePreset =  self.savePresetBtn
        timesran = 0
        lowerFloorHeight = 2.7
        heigherFloorHeight = 3.5
            
        myObj = hou.node('/obj')
        geo = myObj.createNode("geo", 'city')
        myGeo = hou.node('/obj/city')
        subnet = myGeo.createNode("subnet", 'city')
        mySub = hou.node('/obj/city/city')
        merge = mySub.createNode("merge", 'merge1')



        for i in range(int(buildingDensity)):
            lowerTranslateX = random.randint(-100, 100)
            lowerTranslateZ  = random.randint(-100, 100)



            timesran += 1
            box = mySub.createNode("box", f'building{timesran}')
            transform = mySub.createNode("xform", f'tranform{timesran}')
            transform.setInput(0, box)
            randomFloors = random.randint((int(minFloors)), (int(maxFloors)))
            randomFloorHeight = random.uniform(lowerFloorHeight, heigherFloorHeight)
            boxHeight = randomFloorHeight * randomFloors


            boxTranslateX = transform.parm('tx')
            boxTranslateY = transform.parm('ty')
            boxTranslateZ = transform.parm('tz')
            boxHeightY = transform.parm('sy')
            boxWidthX = transform.parm('sx')
            boxWidthZ = transform.parm('sz')

            boxTranslateX.set(int(locationX) + lowerTranslateX)
            boxTranslateZ.set(int(locationY) + lowerTranslateZ)
            boxTranslateY.set(int(locationY) + (int(boxHeight)/2))
            boxHeightY.set(boxHeight)
            boxWidthX.set(random.randint(8, 12))
            boxWidthZ.set(random.randint(8, 12))

            merge.setInput(timesran, transform)
            box.setInput(0, mySub.indirectInputs()[0])
            print("test")
            print(randomFloors)

dialog = cityBuilder()
dialog.show()
'''
             )  
          ( /(  
   (      )\()) 
   )\    ((_)\  
  ((_)    _((_) 
 _ | |   | || | 
| || | _ | __ | 
 \__/ (_)|_||_| 
'''              
```
</div>

</details>

 &nbsp; <br>

## To-Do <br>

⋅⋅* JSON Integration for saving and exporting presets
⋅⋅* Collision Detection
⋅⋅* Snapping to object

<!-- Warning -->
 &nbsp; <br>
> [!WARNING]
> this is a university project and probobly not safe for industry use



<!-- Logo -->

 &nbsp; <br>
 &nbsp; <br>
 &nbsp; <br>
 
<div align="center">
<img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/KuiLogo.png?raw=true" width="150"> <br>

<sub>[created by kuisux](https://github.com/kuisux)</sub>
</div>

