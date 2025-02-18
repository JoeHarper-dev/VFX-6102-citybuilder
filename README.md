
# City Builder



<!-- Image -->

![citescape catppuccin](https://github.com/JoeHarper-tech/VFX-6102-citybuilder/blob/main/pictures/cat_evening-sky.png?raw=true)

<!-- Title -->

## A tool for sideFX Houdini that creates a template city
&nbsp; <br>

<!-- Warning -->

> [!WARNING]
> this is a university project and probobly not safe for industry use
&nbsp; <br>
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
 Press the script tab, then paste the script into the box <br>
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
</details>

<!-- Code -->
<details align="center">
<summary>Code</summary>
    
```python
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


        def ddlCheckBox(self, toggle):
            if toggle == QtCore.Qt.Checked:
                self.DdlSnap.setDisabled(False)
            else:
                self.DdlSnap.setDisabled(True)
#------------------------------------------------------------------------------------------------------------------
#Presets

#buttons
        hboxPresets = QtWidgets.QHBoxLayout()
        self.loadPreset = QtWidgets.QPushButton('Load Preset', self)
        self.savePreset = QtWidgets.QPushButton('Save Preset', self)
        hboxPresets.addWidget(self.loadPreset)
        hboxPresets.addWidget(self.savePreset)
        self.vBox.addLayout(hboxPresets)


        self.setLayout(self.vBox)

def onStateChanged(self):
        if self.checkBoxSnap.isChecked():
             self.DdlSnap.setItemDisabled(False)
        else:
                self.DdlSnap.setItemDisabled(True)
                
        # end def
def buildProject(self):
        print('hello world')
            
dialog = cityBuilder()
dialog.show()
```


</details>


 


<!-- Logo -->

 &nbsp; <br>
 &nbsp; <br>
 &nbsp; <br>
 
<div align="center">
<img src="https://github.com/kuisux/VFX-6102-citybuilder/blob/main/pictures/KuiLogo.png?raw=true" width="150"> <br>

<sub>[created by kuisux](https://github.com/kuisux)</sub>
</div>


