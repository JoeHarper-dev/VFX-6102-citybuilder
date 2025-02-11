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

# Label
        hboxSnap = QtWidgets.QHBoxLayout()
        self.LabelSnap = QtWidgets.QLabel(
            'snap to ground?'
            )
        self.LabelSnap.setMinimumWidth(25)
        hboxSnap.addWidget(self.LabelSnap)

        self.checkBoxSnap = QtWidgets.QCheckBox()
        self.checkBoxSnap.setMinimumWidth(25)
        hboxSnap.addWidget(self.checkBoxSnap)
        self.vBox.addLayout(hboxSnap)
        
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
        def buildProject(self):
            print('hello world')
            
dialog = cityBuilder()
dialog.show()