# -----------------------------------------------------------------------------------------------#
#         ,-----.,--.  ,--.               ,-----.          ,--.,--.   ,--.                       #
#        '  .--./`--',-'  '-.,--. ,--.    |  |) /_ ,--.,--.`--'|  | ,-|  | ,---. ,--.--.         #
#        |  |    ,--.'-.  .-' \  '  /     |  .-.  \|  ||  |,--.|  |' .-. || .-. :|  .--'         #
#        '  '--'\|  |  |  |    \   '      |  '--' /'  ''  '|  ||  |\ `-' |\   --.|  |            #
#         `-----'`--'  `--'  .-'  /       `------'  `----' `--'`--' `---'  `----'`--'            #
#                            `---'                                                               #
# -----------------------------------------------------------------------------------------------#
#         https://github.com/JoeHarper-dev/VFX-6102-citybuilder?tab=CC0-1.0-1-ov-file            #
#                                  Created by Joe Harper                                         #
# -----------------------------------------------------------------------------------------------#

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QInputDialog,
    QLineEdit,
    QFileDialog,
)
import hou
import json
import os
import random
from re import X

# Constants
MY_OBJ = hou.node("/obj")
GEO = MY_OBJ.createNode("geo", "city")
MY_GEO = hou.node("/obj/city")
SUBNET = MY_GEO.createNode("subnet", "city")
MY_SUB = hou.node("/obj/city/city")
MERGE = MY_SUB.createNode("merge", "merge1")


class CityBuilder(QtWidgets.QWidget):
    def __init__(self, parent=None):

        # front end
        # ------------------------------------------------------------------------------------------------------------------
        # creating the vertical layout

        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("City Builder")
        self.vBox = QtWidgets.QVBoxLayout()

        # ------------------------------------------------------------------------------------------------------------------
        # creating the widgets in the UI starting with building density

        # label
        hbox_building_density = QtWidgets.QHBoxLayout()
        self.label_building_density = QtWidgets.QLabel(
            "number of buildings"
        )
        self.label_building_density.setMinimumWidth(175)
        hbox_building_density.addWidget(self.label_building_density)

        # text box

        self.text_input_building_density = QtWidgets.QLineEdit(self)
        self.text_input_building_density.setMinimumWidth(175)
        hbox_building_density.addWidget(self.text_input_building_density)
        self.vBox.addLayout(hbox_building_density)

        # ------------------------------------------------------------------------------------------------------------------
        # max floors

        # label
        hbox_max_floors = QtWidgets.QHBoxLayout()
        self.label_max_floors = QtWidgets.QLabel(
            "maximum ammount of floors"
        )
        self.label_max_floors.setMinimumWidth(175)
        hbox_max_floors.addWidget(self.label_max_floors)

        # text box

        self.text_input_max_floors = QtWidgets.QLineEdit(self)
        self.text_input_max_floors.setMinimumWidth(175)
        hbox_max_floors.addWidget(self.text_input_max_floors)
        self.vBox.addLayout(hbox_max_floors)

        # ------------------------------------------------------------------------------------------------------------------
        # min floors

        # label
        hbox_min_floors = QtWidgets.QHBoxLayout()
        self.label_min_floors = QtWidgets.QLabel(
            "minimum ammount of floors"
        )
        self.label_min_floors.setMinimumWidth(175)
        hbox_min_floors.addWidget(self.label_min_floors)

        # text box
        self.text_input_min_floors = QtWidgets.QLineEdit(self)
        self.text_input_min_floors.setMinimumWidth(175)
        hbox_min_floors.addWidget(self.text_input_min_floors)
        self.vBox.addLayout(hbox_min_floors)

        # ------------------------------------------------------------------------------------------------------------------
        # location

        # label
        hbox_location = QtWidgets.QHBoxLayout()
        self.label_location = QtWidgets.QLabel(
            "city coordinates"
        )
        self.label_location.setMinimumWidth(175)
        hbox_location.addWidget(self.label_location)

        # X location
        self.text_input_location_X = QtWidgets.QLineEdit(self)
        self.text_input_location_X.setMinimumWidth(50)

        # Y Location
        self.text_input_location_Y = QtWidgets.QLineEdit(self)
        self.text_input_location_Y.setMinimumWidth(50)

        # Z Location
        self.text_input_location_Z = QtWidgets.QLineEdit(self)
        self.text_input_location_Z.setMinimumWidth(50)

        hbox_location.addWidget(self.text_input_location_X)
        hbox_location.addWidget(self.text_input_location_Y)
        hbox_location.addWidget(self.text_input_location_Z)
        self.vBox.addLayout(hbox_location)

        # -------------------------------------------------------------------------------------------------------------------
        # display stats
        
        # label
        hbox_stats = QtWidgets.QHBoxLayout()
        self.label_stats = QtWidgets.QLabel(
            "display stats?"
            )
        self.label_stats.setMinimumWidth(25)
        hbox_stats.addWidget(self.label_stats)

        # check box
        self.check_box_stats = QtWidgets.QCheckBox()
        self.check_box_stats.setMinimumWidth(25)
        hbox_stats.addWidget(self.check_box_stats)
        self.vBox.addLayout(hbox_stats)     
        # ------------------------------------------------------------------------------------------------------------------
        # presets

        # buttons
        hbox_presets = QtWidgets.QHBoxLayout()
        self.load_preset_btn = QtWidgets.QPushButton("Load Preset", self)
        self.save_preset_btn = QtWidgets.QPushButton("Save Preset", self)
        hbox_presets.addWidget(self.load_preset_btn)
        hbox_presets.addWidget(self.save_preset_btn)
        self.load_preset_btn.clicked.connect(self.load_preset)
        self.save_preset_btn.clicked.connect(self.save_preset)
        self.vBox.addLayout(hbox_presets)

        # -------------------------------------------------------------------------------------------------------------------
        # placeholders

        self.text_input_building_density.setPlaceholderText(
            "100"
        )
        self.text_input_max_floors.setPlaceholderText(
            "50"
        )
        self.text_input_min_floors.setPlaceholderText(
            "25"
        )
        self.text_input_location_X.setPlaceholderText(
            "0"
        )
        self.text_input_location_Y.setPlaceholderText(
            "0"
        )
        self.text_input_location_Z.setPlaceholderText(
            "0"
        )

        # -------------------------------------------------------------------------------------------------------------------
        # build project
        hbox_build_project = QtWidgets.QHBoxLayout()
        self.build_project_btn = QtWidgets.QPushButton("Build", self)
        self.build_project_btn.clicked.connect(self.build_project)
        hbox_build_project.addWidget(self.build_project_btn)
        self.vBox.addLayout(hbox_build_project)

        

        # -------------------------------------------------------------------------------------------------------------------
        # set layout
        self.setLayout(self.vBox)

    # -------------------------------------------------------------------------------------------------------------------
    # load preset
    def load_preset(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        load_file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Load Preset",
            "",
            "JSON Files (*.json);;YAML Files (*.yaml);; All Files (*)",
            options=options,
        )
        if load_file_name:
                with open(load_file_name, "r") as f:
                    preset_data = json.load(f)

                self.text_input_building_density.setText(
                    preset_data.get("building_density", "")
                )
                self.text_input_max_floors.setText(
                    preset_data.get("max_floors", "")
                )
                self.text_input_min_floors.setText(
                    preset_data.get("min_floors", "")
                )
                self.text_input_location_X.setText(
                    preset_data.get("location_X", "")
                )
                self.text_input_location_Y.setText(
                    preset_data.get("location_Y", "")
                )
                self.text_input_location_Z.setText(
                    preset_data.get("location_Z", "")
                )

                print(f"Preset loaded successfully from: {load_file_name}")


    # -------------------------------------------------------------------------------------------------------------------
    # save Preset
    def save_preset(self):
        self.load_file_nameDialog()

    def load_file_nameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        save_file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Preset",
            "City_Builder-Preset",
            "JSON Files (*.json);;YAML Files (*.yaml);; All Files (*)",
            options=options,
        )
        if save_file_name:
            print(save_file_name)

        if save_file_name:
            if not save_file_name.lower().endswith(".json"):
                save_file_name += ".json"

            preset_data = {
                "building_density": self.text_input_building_density.text(),
                "max_floors": self.text_input_max_floors.text(),
                "min_floors": self.text_input_min_floors.text(),
                "location_X": self.text_input_location_X.text(),
                "location_Y": self.text_input_location_Y.text(),
                "location_Z": self.text_input_location_Z.text(),
            }

            with open(save_file_name, "w") as f:
                json.dump(preset_data, f, indent=4)
            print(f"Preset saved successfully to: {save_file_name}")


    def build_project(self):
        # -------------------------------------------------------------------------------------------------------------------
        # back end

        # variable
        building_density = int(self.text_input_building_density.text())
        max_floors = int(self.text_input_max_floors.text())
        min_floors = int(self.text_input_min_floors.text())
        location_X = int(self.text_input_location_X.text())
        location_Y = int(self.text_input_location_Y.text())
        location_Z = int(self.text_input_location_Z.text())
        times_ran = 0
        lower_floor_height = 2.7
        higher_floor_height = 3.5
        placed_buildings = []

        # collision detection Function
        def collision_detection(new_min_x, new_max_x, new_min_z, new_max_z):
            for min_x, max_x, min_z, max_z in placed_buildings:
                if (
                    new_min_x < max_x
                    and new_max_x > min_x
                    and new_min_z < max_z
                    and new_max_z > min_z
                ):
                    return True
            return False

        for i in range(int(building_density)):

        # collision detection check
            for i in range(100):
                width_X = random.randint(8, 12)
                width_Z = random.randint(8, 12)
                lower_translate_X = random.randint(-100, 100)
                lower_translate_Z = random.randint(-100, 100)
                min_x = location_X + lower_translate_X - width_X / 2
                max_x = location_X + lower_translate_X + width_X / 2
                min_z = location_Z + lower_translate_Z - width_Z / 2
                max_z = location_Z + lower_translate_Z + width_Z / 2

                # Fix collision
                if not collision_detection(min_x, max_x, min_z, max_z):
                    placed_buildings.append(
                        (min_x, max_x, min_z, max_z)
                    )
                    break
                else:
                    continue

            # object creation
            times_ran += 1
            box = MY_SUB.createNode("box", f"building{times_ran}")
            transform = MY_SUB.createNode("xform", f"tranform{times_ran}")
            transform.setInput(0, box)
            random_floors = random.randint((int(min_floors)), (int(max_floors)))
            random_floor_height = random.uniform(
                lower_floor_height, higher_floor_height
            )
            box_height = random_floor_height * random_floors

            # define parameters 
            box_translate_X = transform.parm("tx")
            box_translate_Y = transform.parm("ty")
            box_translate_Z = transform.parm("tz")
            box_heightY = transform.parm("sy")
            box_width_X = transform.parm("sx")
            box_width_Z = transform.parm("sz")#   

            # set parameters
            box_translate_X.set(int(location_X) + lower_translate_X)
            box_translate_Z.set(int(location_Y) + lower_translate_Z)
            box_translate_Y.set(int(location_Y) + (int(box_height) / 2))
            box_width_X.set(width_X)
            box_width_Z.set(width_Z)
            box_heightY.set(box_height)

            MERGE.setInput(times_ran, transform)
            box.setInput(0, MY_SUB.indirectInputs()[0])

        if self.check_box_stats.isChecked():
            # Display the stats in the console
            print (times_ran, "buildings created")
            print("Max Floors:", max_floors)
            print("Min Floors:", min_floors)
            print("Location X:", location_X)
            print("Location Y:", location_Y)



dialog = CityBuilder()
dialog.show()

"""
Created by Joe Harper
CC0-1.0 license
"""
