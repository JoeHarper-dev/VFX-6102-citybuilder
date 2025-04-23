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
from PySide2.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import hou
import json
import os
import random
from re import X


class cityBuilder(QtWidgets.QWidget):
    def __init__(self, parent=None):


#Front end
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
        self.loadPresetBtn.clicked.connect(self.loadPreset)
        self.savePresetBtn.clicked.connect(self.savePreset)
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


#-------------------------------------------------------------------------------------------------------------------
#load Preset|I
    def loadPreset(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        loadFileName, _ = QFileDialog.getOpenFileName(self,
            "Load Preset", 
            "","JSON Files (*.json);;YAML Files (*.yaml);; All Files (*)", 
            options=options)
        if loadFileName:
            try:
                with open(loadFileName, 'r') as f:
                    preset_data = json.load(f)
                
                self.textInputBuildingDensity.setText(preset_data.get("buildingDensity", ""))
                self.textInputMaxFloors.setText(preset_data.get("maxFloors", ""))
                self.TextInputMinFloors.setText(preset_data.get("minFloors", ""))
                self.textInputLocationX.setText(preset_data.get("locationX", ""))
                self.textInputLocationY.setText(preset_data.get("locationY", ""))
                self.textInputLocationZ.setText(preset_data.get("locationZ", ""))

                print(f"Preset loaded successfully from: {loadFileName}")

            except FileNotFoundError:
                print(f"Error: File not found - {loadFileName}")
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON from file - {loadFileName}")
            except Exception as e:
                print(f"An unexpected error occurred during loading: {e}")


#-------------------------------------------------------------------------------------------------------------------
#Save Preset
    def savePreset(self):
        self.loadFileNameDialog()

    def loadFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        saveFileName, _ = QFileDialog.getSaveFileName(self,
            "Save Preset",
            "cityBuilder-Preset","JSON Files (*.json);;YAML Files (*.yaml);; All Files (*)",
            options=options)
        if saveFileName:
            print(saveFileName)
            
        if saveFileName:
            if not saveFileName.lower().endswith('.json'):
                saveFileName += '.json'

            preset_data = {
                "buildingDensity": self.textInputBuildingDensity.text(),
                "maxFloors": self.textInputMaxFloors.text(),
                "minFloors": self.TextInputMinFloors.text(),
                "locationX": self.textInputLocationX.text(),
                "locationY": self.textInputLocationY.text(),
                "locationZ": self.textInputLocationZ.text(),
                "snapObject": self.DdlSnap.currentText()
            }

            try:
                with open(saveFileName, 'w') as f:
                    json.dump(preset_data, f, indent=4)
                print(f"Preset saved successfully to: {saveFileName}")

            except IOError as e:
                 print(f"Error: Could not write to file - {saveFileName}.")
            except Exception as e:
                print(f"An unexpected error occurred during saving")

    def buildProject(self):
#-------------------------------------------------------------------------------------------------------------------
#Back end
            
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
