# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from functools import partial
import time
import csv
import sys




# Things to implement 
# 1. Button click should be added to a list along with the name or ID of the button 
# 2. Undo should delete the last element of the list 
# 3. Back button click should write the list to the csvfile





class Ui_FabricReport(object):

    list_faults = []
    entry = []
    
    def fault_select(self,fault):
        if (fault=="Sizing"):
            FabricReport.setCurrentIndex(1)
        if (fault=="DyeYarn"):
            FabricReport.setCurrentIndex(2) 
        if (fault=="Weavers"):
            FabricReport.setCurrentIndex(3)
        if (fault=="Yarn"):
            FabricReport.setCurrentIndex(4)
        if (fault=="Exit"):
            app = QtWidgets.QApplication(sys.argv)
            app.closeAllWindows() 
            #QtCore.QCoreApplication.instance.quit()
    def update_label(self,name,positive):
        if positive:
        #Sizing Fault buttons
            # vars()[name+"_value_count"] = 123
            if (name=="SOSButton"):
                self.SOSButton_value_count = self.SOSButton_value_count + 1
                self.SOSButton_value.setText(str(self.SOSButton_value_count))
            if (name=="SSButton"):
                self.SSButton_value_count = self.SSButton_value_count + 1
                self.SSButton_value.setText(str(self.SSButton_value_count))
            if (name=="SPButton"):
                self.SPButton_value_count = self.SPButton_value_count + 1
                self.SPButton_value.setText(str(self.SPButton_value_count))
            if (name=="SVButton"):
                self.SVButton_value_count = self.SVButton_value_count + 1
                self.SVButton_value.setText(str(self.SVButton_value_count))
        #DyedYarn Faults buttons
            if (name=="COVButton"):
                self.COVButton_value_count = self.COVButton_value_count + 1
                self.COVButton_value.setText(str(self.COVButton_value_count))
            if (name=="STButton"):
                self.STButton_value_count = self.STButton_value_count + 1
                self.STButton_value.setText(str(self.STButton_value_count))
        #Weavers Fault buttons
                   
            if (name=="DOPButton"):
                self.DOPButton_value_count = self.DOPButton_value_count + 1
                self.DOPButton_value.setText(str(self.DOPButton_value_count))
            if (name=="HSButton"):
                self.HSButton_value_count = self.HSButton_value_count + 1
                self.HSButton_value.setText(str(self.HSButton_value_count))
            if (name=="WDRButton"):
                self.WDRButton_value_count = self.WDRButton_value_count + 1
                self.WDRButton_value.setText(str(self.WDRButton_value_count))
            if (name=="WWftButton"):
                self.WWftButton_value_count = self.WWftButton_value_count + 1
                self.WWftButton_value.setText(str(self.WWftButton_value_count))
        
            if (name=="WDTButton"):
                self.WDTButton_value_count = self.WDTButton_value_count + 1
                self.WDTButton_value.setText(str(self.WDTButton_value_count))
            if (name=="SWButton"):
                self.SWButton_value_count = self.SWButton_value_count + 1
                self.SWButton_value.setText(str(self.SWButton_value_count))        
                
        #Yarn Fault buttons
        
            if (name=="YSVButton"):
                self.YSVButton_value_count = self.YSVButton_value_count + 1
                self.YSVButton_value.setText(str(self.YSVButton_value_count))
            if (name=="CVButton"):
                self.CVButton_value_count = self.CVButton_value_count + 1
                self.CVButton_value.setText(str(self.CVButton_value_count))
            if (name=="CWftButton"):
                self.CWftButton_value_count = self.CWftButton_value_count + 1
                self.CWftButton_value.setText(str(self.CWftButton_value_count))
            if (name=="ThThButton"):
                self.ThThButton_value_count = self.ThThButton_value_count + 1
                self.ThThButton_value.setText(str(self.ThThButton_value_count))
            if (name=="CMButton"):
                self.CMButton_value_count = self.CMButton_value_count + 1
                self.CMButton_value.setText(str(self.CMButton_value_count))
            if (name=="SYButton"):
                self.SYButton_value_count = self.SYButton_value_count + 1
                self.SYButton_value.setText(str(self.SYButton_value_count))       
            if (name=="CtnButton"):
                self.CtnButton_value_count = self.CtnButton_value_count + 1
                self.CtnButton_value.setText(str(self.CtnButton_value_count))
            if (name=="CWpButton"):
                self.CWpButton_value_count = self.CWpButton_value_count + 1
                self.CWpButton_value.setText(str(self.CWpButton_value_count))                   
              
            
        else :
        #Sizing Fault buttons
            # vars()[name+"_value_count"] = 123
            if (name=="SOSButton"):
                self.SOSButton_value_count = self.SOSButton_value_count - 1
                if self.SOSButton_value_count == 0 : 
                    self.SOSButton_value.setText("")
                else :
                    self.SOSButton_value.setText(str(self.SOSButton_value_count))
            if (name=="SSButton"):
                self.SSButton_value_count = self.SSButton_value_count - 1
                if self.SSButton_value_count == 0 : 
                    self.SSButton_value.setText("")
                else :
                    self.SSButton_value.setText(str(self.SSButton_value_count))
            if (name=="SPButton"):
                self.SPButton_value_count = self.SPButton_value_count - 1
                if self.SPButton_value_count == 0 : 
                    self.SPButton_value.setText("")
                else :
                    self.SPButton_value.setText(str(self.SPButton_value_count))
            if (name=="SVButton"):
                self.SVButton_value_count = self.SVButton_value_count - 1
                if self.SVButton_value_count == 0 : 
                    self.SVButton_value.setText("")
                else :
                    self.SVButton_value.setText(str(self.SVButton_value_count))
         #DyedYarn Faults
            if (name=="COVButton"):
                self.COVButton_value_count = self.COVButton_value_count - 1
                if self.COVButton_value_count == 0 : 
                    self.COVButton_value.setText("")
                else :
                    self.COVButton_value.setText(str(self.COVButton_value_count))
            if (name=="STButton"):
                self.STButton_value_count = self.STButton_value_count - 1
                if self.STButton_value_count == 0 : 
                    self.STButton_value.setText("")
                else :
                    self.STButton_value.setText(str(self.STButton_value_count))    

        #Weavers Fault buttons
        
            if (name=="DOPButton"):
                self.DOPButton_value_count = self.DOPButton_value_count - 1
                if self.DOPButton_value_count == 0 : 
                    self.DOPButton_value.setText("")
                else :
                    self.DOPButton_value.setText(str(self.DOPButton_value_count))
            if (name=="HSButton"):
                self.HSButton_value_count = self.HSButton_value_count - 1
                if self.HSButton_value_count == 0 : 
                    self.HSButton_value.setText("")
                else :
                    self.HSButton_value.setText(str(self.HSButton_value_count))
            if (name=="WDRButton"):
                self.WDRButton_value_count = self.WDRButton_value_count - 1
                if self.WDRButton_value_count == 0 : 
                    self.WDRButton_value.setText("")
                else :
                    self.WDRButton_value.setText(str(self.WDRButton_value_count))
            if (name=="WWftButton"):
                self.WWftButton_value_count = self.WWftButton_value_count - 1
                if self.WWftButton_value_count == 0 : 
                    self.WWftButton_value.setText("")
                else :
                    self.WWftButton_value.setText(str(self.WWftButton_value_count))
            if (name=="WDTButton"):
                self.WDTButton_value_count = self.WDTButton_value_count - 1
                if self.WDTButton_value_count == 0 : 
                    self.WDTButton_value.setText("")
                else :
                    self.WDTButton_value.setText(str(self.WDTButton_value_count))
            if (name=="SWButton"):
                self.SWButton_value_count = self.SWButton_value_count - 1
                if self.SWButton_value_count == 0 : 
                    self.SWButton_value.setText("")
                else :
                    self.SWButton_value.setText(str(self.SWButton_value_count))  
                    
            
    #Yarn Fault buttons
        
            if (name=="YSVButton"):
                self.YSVButton_value_count = self.YSVButton_value_count - 1
                if self.YSVButton_value_count == 0 : 
                    self.YSVButton_value.setText("")
                else :
                    self.YSVButton_value.setText(str(self.YSVButton_value_count))
            if (name=="CVButton"):
                self.CVButton_value_count = self.CVButton_value_count - 1
                if self.CVButton_value_count == 0 : 
                    self.CVButton_value.setText("")
                else :
                    self.CVButton_value.setText(str(self.CVButton_value_count))
            if (name=="CWftButton"):
                self.CWftButton_value_count = self.CWftButton_value_count - 1
                if self.CWftButton_value_count == 0 : 
                    self.CWftButton_value.setText("")
                else :
                    self.CWftButton_value.setText(str(self.CWftButton_value_count))
            if (name=="ThThButton"):
                self.ThThButton_value_count = self.ThThButton_value_count - 1
                if self.ThThButton_value_count == 0 : 
                    self.ThThButton_value.setText("")
                else :
                    self.ThThButton_value.setText(str(self.ThThButton_value_count))
            if (name=="CMButton"):
                self.CMButton_value_count = self.CMButton_value_count - 1
                if self.CMButton_value_count == 0 : 
                    self.CMButton_value.setText("")
                else :
                    self.CMButton_value.setText(str(self.CMButton_value_count))
            if (name=="SYButton"):
                self.SYButton_value_count = self.SYButton_value_count - 1
                if self.SYButton_value_count == 0 : 
                    self.SYButton_value.setText("")
                else :
                    self.SYButton_value.setText(str(self.SYButton_value_count))
            if (name=="CtnButton"):
                self.CtnButton_value_count = self.CtnButton_value_count - 1
                if self.CtnButton_value_count == 0 : 
                    self.CtnButton_value.setText("")
                else :
                    self.CtnButton_value.setText(str(self.CtnButton_value_count))
            if (name=="CWpButton"):
                self.CWpButton_value_count = self.CWpButton_value_count - 1
                if self.CWpButton_value_count == 0 : 
                    self.CWpButton_value.setText("")
                else :
                    self.CWftButton_value.setText(str(self.CWpButton_value_count))            

    def write_to_list(self,name):
        timenow=time.asctime()
        entry = [timenow,self.MeterEdit.text(),name]
        self.list_faults.append(entry)
        print(name)
        self.update_label(name,1)
        

    
    def undo_list(self):
        if len(self.list_faults)>0 :
            self.update_label(self.list_faults[-1][2],0)
            self.list_faults = self.list_faults[:-1]


    def back_button(self,name):

        f = open("fault_DB.csv",'a')
        csv_writer = csv.writer(f)

    #write all to csv 

        for i in self.list_faults:
            csv_writer.writerow(i)

        f.close()

    #after writing to csv === reset list
        self.list_faults.clear()

        
    #Reset all the count values

    #Sizing fault
        if name == "Sizing":
            self.SVButton_value_count = 0
            self.SPButton_value_count = 0
            self.SSButton_value_count = 0
            self.SOSButton_value_count = 0
            
            self.SOSButton_value.setText("")
            self.SVButton_value.setText("")
            self.SSButton_value.setText("")
            self.SPButton_value.setText("")
            
            
    #Dyedyarn fault
        if name == "DyedYarn":
            self.COVButton_value_count = 0
            self.STButton_value_count = 0
            
            self.COVButton_value.setText("")
            self.STButton_value.setText("")
                    
        
    #Weave fault
        if name == "Weave":
            self.DOPButton_value_count = 0
            self.HSButton_value_count = 0
            self.WDRButton_value_count = 0
            self.WWftButton_value_count = 0     
            self.WDTButton_value_count = 0
            self.SWButton_value_count = 0 
            
            self.DOPButton_value.setText("")
            self.WDRButton_value.setText("")
            self.HSButton_value.setText("")
            self.WWftButton_value.setText("")
            self.WDTButton_value.setText("")
            self.SWButton_value.setText("")            
            
            
    #Yarn fault
        if name == "Yarn":
            self.YSVButton_value_count = 0
            self.CVButton_value_count = 0
            self.CWftButton_value_count = 0
            self.ThThButton_value_count = 0     
            self.CMButton_value_count = 0
            self.SYButton_value_count = 0 
            self.CtnButton_value_count = 0
            self.CWpButton_value_count = 0
            
            self.YSVButton_value.setText("")
            self.CVButton_value.setText("")
            self.CWftButton_value.setText("")
            self.ThThButton_value.setText("")
            self.CMButton_value.setText("")
            self.SYButton_value.setText("")   
            self.CtnButton_value.setText("")
            self.CWpButton_value.setText("")               
    #Back to Faultselection    
        FabricReport.setCurrentIndex(0)
            

# ======================================================After this QT5 UI portion generated using PyUic =============================================================================

    def setupUi(self, FabricReport):
        FabricReport.setObjectName("FabricReport")
        FabricReport.resize(1087, 604)
        FabricReport.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.454545 rgba(235, 148, 61, 255), stop:0.98 rgba(108, 65, 38, 255), stop:1 rgba(0, 0, 0, 0));")
        self.FaultSelection = QtWidgets.QWidget()
        self.FaultSelection.setObjectName("FaultSelection")
        self.ExitButton = QtWidgets.QPushButton(self.FaultSelection)
        self.ExitButton.setGeometry(QtCore.QRect(470, 470, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.ExitButton.setObjectName("ExitButton")
        self.frame_5 = QtWidgets.QFrame(self.FaultSelection)
        self.frame_5.setGeometry(QtCore.QRect(0, -10, 1101, 611))
        self.frame_5.setStyleSheet("border-image: url(:/newPrefix/Capture 6.JPG);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_18 = QtWidgets.QLabel(self.FaultSelection)
        self.label_18.setGeometry(QtCore.QRect(710, 140, 281, 51))
        self.label_18.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_18.setObjectName("label_18")
        self.MeterEdit = QtWidgets.QLineEdit(self.FaultSelection)
        self.MeterEdit.setGeometry(QtCore.QRect(720, 200, 251, 41))
        self.MeterEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.MeterEdit.setObjectName("MeterEdit")
        self.DyedButton = QtWidgets.QPushButton(self.FaultSelection)
        self.DyedButton.setGeometry(QtCore.QRect(670, 450, 251, 141))
        self.DyedButton.setMinimumSize(QtCore.QSize(0, 0))
        self.DyedButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.DyedButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.DyedButton.setFont(font)
        self.DyedButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.DyedButton.setIconSize(QtCore.QSize(30, 30))
        self.DyedButton.setObjectName("DyedButton")
        self.SizeButton = QtWidgets.QPushButton(self.FaultSelection)
        self.SizeButton.setGeometry(QtCore.QRect(180, 450, 251, 141))
        self.SizeButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SizeButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SizeButton.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.SizeButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.SizeButton.setFont(font)
        self.SizeButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.SizeButton.setIconSize(QtCore.QSize(30, 30))
        self.SizeButton.setObjectName("SizeButton")
        self.WeaversButton = QtWidgets.QPushButton(self.FaultSelection)
        self.WeaversButton.setGeometry(QtCore.QRect(180, 300, 251, 141))
        self.WeaversButton.setMinimumSize(QtCore.QSize(0, 0))
        self.WeaversButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.WeaversButton.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.WeaversButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.WeaversButton.setFont(font)
        self.WeaversButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.WeaversButton.setIconSize(QtCore.QSize(30, 30))
        self.WeaversButton.setObjectName("WeaversButton")
        self.YarnButton = QtWidgets.QPushButton(self.FaultSelection)
        self.YarnButton.setGeometry(QtCore.QRect(180, 150, 251, 141))
        self.YarnButton.setMinimumSize(QtCore.QSize(0, 0))
        self.YarnButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.YarnButton.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.YarnButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.YarnButton.setFont(font)
        self.YarnButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.YarnButton.setIconSize(QtCore.QSize(30, 30))
        self.YarnButton.setObjectName("YarnButton")
        self.MachineButton = QtWidgets.QPushButton(self.FaultSelection)
        self.MachineButton.setGeometry(QtCore.QRect(670, 290, 251, 141))
        self.MachineButton.setMinimumSize(QtCore.QSize(0, 0))
        self.MachineButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.MachineButton.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.MachineButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.MachineButton.setFont(font)
        self.MachineButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.MachineButton.setIconSize(QtCore.QSize(30, 30))
        self.MachineButton.setObjectName("MachineButton")
        self.frame_5.raise_()
        self.DyedButton.raise_()
        self.MeterEdit.raise_()
        self.YarnButton.raise_()
        self.WeaversButton.raise_()
        self.SizeButton.raise_()
        self.MachineButton.raise_()
        self.label_18.raise_()
        self.ExitButton.raise_()
        FabricReport.addWidget(self.FaultSelection)
        
        
# ==============================================================Sizing fault ========================================================
        self.SizingFault = QtWidgets.QWidget()
        self.SizingFault.setObjectName("SizingFault")
    
    #backbutton
        self.backButtonSi = QtWidgets.QPushButton(self.SizingFault)
        self.backButtonSi.setGeometry(QtCore.QRect(630, 490, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.backButtonSi.setFont(font)
        self.backButtonSi.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.backButtonSi.setObjectName("backButtonSi")
    
    #undobutton
        self.Undo_SizeButton = QtWidgets.QPushButton(self.SizingFault)
        self.Undo_SizeButton.setGeometry(QtCore.QRect(450, 40, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_SizeButton.setFont(font)
        self.Undo_SizeButton.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Undo_SizeButton.setObjectName("Undo_SizeButton")
        
     #Faultbuttons   
       
        self.SOSButton = QtWidgets.QPushButton(self.SizingFault)
        self.SOSButton.setGeometry(QtCore.QRect(460, 180, 261, 91))
        self.SOSButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SOSButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SOSButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SOSButton.setFont(font)
        self.SOSButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.SOSButton.setIconSize(QtCore.QSize(30, 30))
        self.SOSButton.setObjectName("SOSButton")
        
        self.SSButton = QtWidgets.QPushButton(self.SizingFault)
        self.SSButton.setGeometry(QtCore.QRect(780, 180, 261, 91))
        self.SSButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SSButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SSButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SSButton.setFont(font)
        self.SSButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.SSButton.setIconSize(QtCore.QSize(30, 30))
        self.SSButton.setObjectName("SSButton")
        
        
        self.SPButton = QtWidgets.QPushButton(self.SizingFault)
        self.SPButton.setGeometry(QtCore.QRect(780, 330, 261, 91))
        self.SPButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SPButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SPButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SPButton.setFont(font)
        self.SPButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.SPButton.setIconSize(QtCore.QSize(30, 30))
        self.SPButton.setObjectName("SPButton")
        
        
        self.SVButton = QtWidgets.QPushButton(self.SizingFault)
        self.SVButton.setGeometry(QtCore.QRect(460, 330, 261, 91))
        self.SVButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SVButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SVButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SVButton.setFont(font)
        self.SVButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.SVButton.setIconSize(QtCore.QSize(30, 30))
        self.SVButton.setObjectName("SVButton")
        
    #button_values
        self.SOSButton_value = QtWidgets.QLabel(self.SizingFault)
        self.SOSButton_value.setGeometry(QtCore.QRect(680, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SOSButton_value.setFont(font)
        self.SOSButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SOSButton_value.setObjectName("SOSButton_value")
        self.SSButton_value = QtWidgets.QLabel(self.SizingFault)
        self.SSButton_value.setGeometry(QtCore.QRect(1000, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SSButton_value.setFont(font)
        self.SSButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SSButton_value.setObjectName("SSButton_value")
        
        self.SPButton_value = QtWidgets.QLabel(self.SizingFault)
        self.SPButton_value.setGeometry(QtCore.QRect(1000, 320, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SPButton_value.setFont(font)
        self.SPButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SPButton_value.setObjectName("SPButton_value")
        
        self.SVButton_value = QtWidgets.QLabel(self.SizingFault)
        self.SVButton_value.setGeometry(QtCore.QRect(680, 320, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SVButton_value.setFont(font)
        self.SVButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SVButton_value.setObjectName("SVButton_value")
        
    #Counts
        self.SVButton_value_count = 0
        self.SPButton_value_count = 0
        self.SSButton_value_count = 0
        self.SOSButton_value_count = 0     
        
    #center align
        self.SVButton_value.setAlignment(Qt.AlignCenter)
        self.SPButton_value.setAlignment(Qt.AlignCenter)
        self.SSButton_value.setAlignment(Qt.AlignCenter)
        self.SOSButton_value.setAlignment(Qt.AlignCenter)        


        self.label_32 = QtWidgets.QLabel(self.SizingFault)
        self.label_32.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.label_32.setStyleSheet("border-image: url(:/newPrefix/Capture.JPG);")
        self.label_32.setObjectName("label_32")
        self.frame_2 = QtWidgets.QFrame(self.SizingFault)
        self.frame_2.setGeometry(QtCore.QRect(460, 70, 31, 21))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.SizingFault)
        self.frame_3.setGeometry(QtCore.QRect(640, 500, 41, 31))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_32.raise_()
        self.backButtonSi.raise_()
        self.SOSButton.raise_()
        self.Undo_SizeButton.raise_()
        self.SSButton.raise_()
        self.SPButton.raise_()
        self.SVButton.raise_()
        self.SOSButton_value.raise_()
        self.SSButton_value.raise_()
        self.SPButton_value.raise_()
        self.SVButton_value.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        FabricReport.addWidget(self.SizingFault)
        
        
#======================================================Dyedyarn===========================================================
        self.DyedYarnFault = QtWidgets.QWidget()
        self.DyedYarnFault.setObjectName("DyedYarnFault")
        
    #back button
        self.backButtonDy = QtWidgets.QPushButton(self.DyedYarnFault)
        self.backButtonDy.setGeometry(QtCore.QRect(640, 480, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backButtonDy.setFont(font)
        self.backButtonDy.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.backButtonDy.setObjectName("backButtonDy")
        
    #fault buttons
        self.COVButton = QtWidgets.QPushButton(self.DyedYarnFault)
        self.COVButton.setGeometry(QtCore.QRect(450, 250, 241, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.COVButton.setFont(font)
        self.COVButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.COVButton.setObjectName("COVButton")
        self.STButton = QtWidgets.QPushButton(self.DyedYarnFault)
        self.STButton.setGeometry(QtCore.QRect(790, 250, 241, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.STButton.setFont(font)
        self.STButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.STButton.setObjectName("STButton")
        
    #values
        self.COVButton_value = QtWidgets.QLabel(self.DyedYarnFault)
        self.COVButton_value.setGeometry(QtCore.QRect(650, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.COVButton_value.setFont(font)
        self.COVButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.COVButton_value.setObjectName("COVButton_value")
        self.STButton_value = QtWidgets.QLabel(self.DyedYarnFault)
        self.STButton_value.setGeometry(QtCore.QRect(990, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.STButton_value.setFont(font)
        self.STButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.STButton_value.setObjectName("STButton_value")
        
    #Counts
        self.COVButton_value_count = 0
        self.STButton_value_count = 0
        
    #center align
        self.COVButton_value.setAlignment(Qt.AlignCenter)
        self.STButton_value.setAlignment(Qt.AlignCenter)
                 
        
    #undo button
    
        self.Undo_DyeButton = QtWidgets.QPushButton(self.DyedYarnFault)
        self.Undo_DyeButton.setGeometry(QtCore.QRect(440, 70, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_DyeButton.setFont(font)
        self.Undo_DyeButton.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Undo_DyeButton.setObjectName("Undo_DyeButton")
        
        self.frame_9 = QtWidgets.QFrame(self.DyedYarnFault)
        self.frame_9.setGeometry(QtCore.QRect(450, 90, 31, 21))
        self.frame_9.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
              
        
        self.frame_5 = QtWidgets.QFrame(self.DyedYarnFault)
        self.frame_5.setGeometry(QtCore.QRect(650, 490, 41, 31))
        self.frame_5.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
               
        
        self.frame_6 = QtWidgets.QFrame(self.DyedYarnFault)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1091, 611))
        self.frame_6.setStyleSheet("border-image: url(:/newPrefix/Capture 7.JPG);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.raise_()
        self.backButtonDy.raise_()
        self.COVButton.raise_()
        self.STButton.raise_()
        self.STButton_value.raise_()
        self.Undo_DyeButton.raise_()
        self.COVButton_value.raise_()
        self.frame_5.raise_()
        self.frame_9.raise_() 
        FabricReport.addWidget(self.DyedYarnFault)
        
#==========================================================Weave Fault =======================================================
        self.WeaveFault = QtWidgets.QWidget()
        self.WeaveFault.setObjectName("WeaveFault")
        
    #backbutton
        self.backButtonWe = QtWidgets.QPushButton(self.WeaveFault)
        self.backButtonWe.setGeometry(QtCore.QRect(640, 480, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backButtonWe.setFont(font)
        self.backButtonWe.setStyleSheet("background-color: rgb(212, 199, 255);\n"
"")
        self.backButtonWe.setObjectName("backButtonWe")
        self.label_33 = QtWidgets.QLabel(self.WeaveFault)
        self.label_33.setGeometry(QtCore.QRect(0, -10, 1091, 611))
        self.label_33.setStyleSheet("border-image: url(:/newPrefix/Capture2.JPG);")
        self.label_33.setObjectName("label_33")
        
    #undobutton
        self.Undo_WeaveButton = QtWidgets.QPushButton(self.WeaveFault)
        self.Undo_WeaveButton.setGeometry(QtCore.QRect(440, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_WeaveButton.setFont(font)
        self.Undo_WeaveButton.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Undo_WeaveButton.setObjectName("Undo_WeaveButton")
        
    #Faultbuttons
        self.WDRButton = QtWidgets.QPushButton(self.WeaveFault)
        self.WDRButton.setGeometry(QtCore.QRect(440, 140, 301, 81))
        self.WDRButton.setMinimumSize(QtCore.QSize(0, 0))
        self.WDRButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.WDRButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WDRButton.setFont(font)
        self.WDRButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.WDRButton.setIconSize(QtCore.QSize(30, 30))
        self.WDRButton.setObjectName("WDRButton")
        self.WWftButton = QtWidgets.QPushButton(self.WeaveFault)
        self.WWftButton.setGeometry(QtCore.QRect(760, 360, 301, 81))
        self.WWftButton.setMinimumSize(QtCore.QSize(0, 0))
        self.WWftButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.WWftButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WWftButton.setFont(font)
        self.WWftButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.WWftButton.setIconSize(QtCore.QSize(30, 30))
        self.WWftButton.setObjectName("WWftButton")
        self.SWButton = QtWidgets.QPushButton(self.WeaveFault)
        self.SWButton.setGeometry(QtCore.QRect(440, 360, 301, 81))
        self.SWButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SWButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SWButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SWButton.setFont(font)
        self.SWButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.SWButton.setIconSize(QtCore.QSize(30, 30))
        self.SWButton.setObjectName("SWButton")
        self.WDTButton = QtWidgets.QPushButton(self.WeaveFault)
        self.WDTButton.setGeometry(QtCore.QRect(440, 250, 301, 81))
        self.WDTButton.setMinimumSize(QtCore.QSize(0, 0))
        self.WDTButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.WDTButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WDTButton.setFont(font)
        self.WDTButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.WDTButton.setIconSize(QtCore.QSize(30, 30))
        self.WDTButton.setObjectName("WDTButton")
        self.HSButton = QtWidgets.QPushButton(self.WeaveFault)
        self.HSButton.setGeometry(QtCore.QRect(760, 250, 301, 81))
        self.HSButton.setMinimumSize(QtCore.QSize(0, 0))
        self.HSButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.HSButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.HSButton.setFont(font)
        self.HSButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.HSButton.setIconSize(QtCore.QSize(30, 30))
        self.HSButton.setObjectName("HSButton")
        self.DOPButton = QtWidgets.QPushButton(self.WeaveFault)
        self.DOPButton.setGeometry(QtCore.QRect(760, 140, 301, 81))
        self.DOPButton.setMinimumSize(QtCore.QSize(0, 0))
        self.DOPButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.DOPButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DOPButton.setFont(font)
        self.DOPButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.DOPButton.setIconSize(QtCore.QSize(30, 30))
        self.DOPButton.setObjectName("DOPButton")
        
    #button_values
        self.WDRButton_value = QtWidgets.QLabel(self.WeaveFault)
        self.WDRButton_value.setGeometry(QtCore.QRect(700, 130, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WDRButton_value.setFont(font)
        self.WDRButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.WDRButton_value.setObjectName("WDRButton_value")
        self.WDTButton_value = QtWidgets.QLabel(self.WeaveFault)
        self.WDTButton_value.setGeometry(QtCore.QRect(700, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WDTButton_value.setFont(font)
        self.WDTButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.WDTButton_value.setObjectName("WDTButton_value")
        self.SWButton_value = QtWidgets.QLabel(self.WeaveFault)
        self.SWButton_value.setGeometry(QtCore.QRect(700, 350, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SWButton_value.setFont(font)
        self.SWButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SWButton_value.setObjectName("SWButton_value")
        self.WWftButton_value = QtWidgets.QLabel(self.WeaveFault)
        self.WWftButton_value.setGeometry(QtCore.QRect(1020, 350, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WWftButton_value.setFont(font)
        self.WWftButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.WWftButton_value.setObjectName("WWftButton_value")
        self.HSButton_value = QtWidgets.QLabel(self.WeaveFault)
        self.HSButton_value.setGeometry(QtCore.QRect(1020, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.HSButton_value.setFont(font)
        self.HSButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.HSButton_value.setObjectName("HSButton_value")
        self.DOPButton_value = QtWidgets.QLabel(self.WeaveFault)
        self.DOPButton_value.setGeometry(QtCore.QRect(1020, 130, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DOPButton_value.setFont(font)
        self.DOPButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.DOPButton_value.setObjectName("DOPButton_value")
        
    #counts
        self.DOPButton_value_count = 0
        self.HSButton_value_count = 0
        self.WDRButton_value_count = 0
        self.WWftButton_value_count = 0     
        self.WDTButton_value_count = 0
        self.SWButton_value_count = 0  
        
    #center align
        self.DOPButton_value.setAlignment(Qt.AlignCenter)
        self.HSButton_value.setAlignment(Qt.AlignCenter)
        self.WDRButton_value.setAlignment(Qt.AlignCenter)
        self.WWftButton_value.setAlignment(Qt.AlignCenter) 
        self.WDTButton_value.setAlignment(Qt.AlignCenter)
        self.SWButton_value.setAlignment(Qt.AlignCenter)         
        
        self.frame = QtWidgets.QFrame(self.WeaveFault)
        self.frame.setGeometry(QtCore.QRect(450, 60, 31, 21))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.WeaveFault)
        self.frame_4.setGeometry(QtCore.QRect(650, 490, 41, 31))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_33.raise_()
        self.backButtonWe.raise_()
        self.Undo_WeaveButton.raise_()
        self.WDRButton.raise_()
        self.WWftButton.raise_()
        self.SWButton.raise_()
        self.WDTButton.raise_()
        self.HSButton.raise_()
        self.DOPButton.raise_()
        self.WDRButton_value.raise_()
        self.WDTButton_value.raise_()
        self.SWButton_value.raise_()
        self.WWftButton_value.raise_()
        self.HSButton_value.raise_()
        self.DOPButton_value.raise_()
        self.frame.raise_()
        self.frame_4.raise_()
        FabricReport.addWidget(self.WeaveFault)
        
#===============================================================YarnFault======================================================
        self.YarnFault = QtWidgets.QWidget()
        self.YarnFault.setObjectName("YarnFault")
        self.label_34 = QtWidgets.QLabel(self.YarnFault)
        self.label_34.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.label_34.setStyleSheet("border-image: url(:/newPrefix/Capture 8.JPG);")
        self.label_34.setObjectName("label_34")
        
    #backbutton
        self.backButtonYa = QtWidgets.QPushButton(self.YarnFault)
        self.backButtonYa.setGeometry(QtCore.QRect(650, 490, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backButtonYa.setFont(font)
        self.backButtonYa.setStyleSheet("background-color: rgb(212, 199, 255);\n"
"")
        self.backButtonYa.setObjectName("backButtonYa")
        
    #undobutton
        self.Undo_YarnButton = QtWidgets.QPushButton(self.YarnFault)
        self.Undo_YarnButton.setGeometry(QtCore.QRect(490, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_YarnButton.setFont(font)
        self.Undo_YarnButton.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Undo_YarnButton.setObjectName("Undo_YarnButton")        
        
    #Faultbuttons
        self.ThThButton = QtWidgets.QPushButton(self.YarnFault)
        self.ThThButton.setGeometry(QtCore.QRect(430, 200, 301, 61))
        self.ThThButton.setMinimumSize(QtCore.QSize(0, 0))
        self.ThThButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.ThThButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ThThButton.setFont(font)
        self.ThThButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.ThThButton.setIconSize(QtCore.QSize(30, 30))
        self.ThThButton.setObjectName("ThThButton")
        self.CtnButton = QtWidgets.QPushButton(self.YarnFault)
        self.CtnButton.setGeometry(QtCore.QRect(770, 390, 301, 61))
        self.CtnButton.setMinimumSize(QtCore.QSize(0, 0))
        self.CtnButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.CtnButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CtnButton.setFont(font)
        self.CtnButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.CtnButton.setIconSize(QtCore.QSize(30, 30))
        self.CtnButton.setObjectName("CtnButton")
       
        self.CWftButton = QtWidgets.QPushButton(self.YarnFault)
        self.CWftButton.setGeometry(QtCore.QRect(770, 290, 301, 61))
        self.CWftButton.setMinimumSize(QtCore.QSize(0, 0))
        self.CWftButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.CWftButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CWftButton.setFont(font)
        self.CWftButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.CWftButton.setIconSize(QtCore.QSize(30, 30))
        self.CWftButton.setObjectName("CWftButton")
       
        self.SYButton = QtWidgets.QPushButton(self.YarnFault)
        self.SYButton.setGeometry(QtCore.QRect(770, 110, 301, 61))
        self.SYButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SYButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SYButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SYButton.setFont(font)
        self.SYButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.SYButton.setIconSize(QtCore.QSize(30, 30))
        self.SYButton.setObjectName("SYButton")
        self.CMButton = QtWidgets.QPushButton(self.YarnFault)
        self.CMButton.setGeometry(QtCore.QRect(430, 110, 301, 61))
        self.CMButton.setMinimumSize(QtCore.QSize(0, 0))
        self.CMButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.CMButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CMButton.setFont(font)
        self.CMButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.CMButton.setIconSize(QtCore.QSize(30, 30))
        self.CMButton.setObjectName("CMButton")
        self.CWpButton = QtWidgets.QPushButton(self.YarnFault)
        self.CWpButton.setGeometry(QtCore.QRect(430, 290, 301, 61))
        self.CWpButton.setMinimumSize(QtCore.QSize(0, 0))
        self.CWpButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.CWpButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CWpButton.setFont(font)
        self.CWpButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.CWpButton.setIconSize(QtCore.QSize(30, 30))
        self.CWpButton.setObjectName("CWpButton")
        
        self.frame_7 = QtWidgets.QFrame(self.YarnFault)
        self.frame_7.setGeometry(QtCore.QRect(660, 500, 41, 31))
        self.frame_7.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")        
        self.frame_8 = QtWidgets.QFrame(self.YarnFault)
        self.frame_8.setGeometry(QtCore.QRect(500, 40, 31, 21))
        self.frame_8.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        
        self.CVButton = QtWidgets.QPushButton(self.YarnFault)
        self.CVButton.setGeometry(QtCore.QRect(770, 200, 301, 61))
        self.CVButton.setMinimumSize(QtCore.QSize(0, 0))
        self.CVButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.CVButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CVButton.setFont(font)
        self.CVButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.CVButton.setIconSize(QtCore.QSize(30, 30))
        self.CVButton.setObjectName("CVButton")
        self.YSVButton = QtWidgets.QPushButton(self.YarnFault)
        self.YSVButton.setGeometry(QtCore.QRect(430, 390, 301, 61))
        self.YSVButton.setMinimumSize(QtCore.QSize(0, 0))
        self.YSVButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.YSVButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YSVButton.setFont(font)
        self.YSVButton.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(52, 101, 164);")
        self.YSVButton.setIconSize(QtCore.QSize(30, 30))
        self.YSVButton.setObjectName("YSVButton")
        
    #button_values
        self.CtnButton_value = QtWidgets.QLabel(self.YarnFault)
        self.CtnButton_value.setGeometry(QtCore.QRect(1030, 380, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CtnButton_value.setFont(font)
        self.CtnButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.CtnButton_value.setObjectName("CtnButton_value")
        self.CWftButton_value = QtWidgets.QLabel(self.YarnFault)
        self.CWftButton_value.setGeometry(QtCore.QRect(1030, 280, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CWftButton_value.setFont(font)
        self.CWftButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.CWftButton_value.setObjectName("CWftButton_value")
        self.CVButton_value = QtWidgets.QLabel(self.YarnFault)
        self.CVButton_value.setGeometry(QtCore.QRect(1030, 190, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CVButton_value.setFont(font)
        self.CVButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.CVButton_value.setObjectName("CVButton_value")
        self.SYButton_value = QtWidgets.QLabel(self.YarnFault)
        self.SYButton_value.setGeometry(QtCore.QRect(1030, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SYButton_value.setFont(font)
        self.SYButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SYButton_value.setObjectName("SYButton_value")
        self.CMButton_value = QtWidgets.QLabel(self.YarnFault)
        self.CMButton_value.setGeometry(QtCore.QRect(690, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CMButton_value.setFont(font)
        self.CMButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.CMButton_value.setObjectName("CMButton_value")
        self.ThThButton_value = QtWidgets.QLabel(self.YarnFault)
        self.ThThButton_value.setGeometry(QtCore.QRect(690, 190, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ThThButton_value.setFont(font)
        self.ThThButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.ThThButton_value.setObjectName("ThThButton_value")
        self.CWpButton_value = QtWidgets.QLabel(self.YarnFault)
        self.CWpButton_value.setGeometry(QtCore.QRect(690, 280, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CWpButton_value.setFont(font)
        self.CWpButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.CWpButton_value.setObjectName("CWpButton_value")
        self.YSVButton_value = QtWidgets.QLabel(self.YarnFault)
        self.YSVButton_value.setGeometry(QtCore.QRect(690, 380, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YSVButton_value.setFont(font)
        self.YSVButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.YSVButton_value.setObjectName("YSVButton_value")
        
    #counts
        self.YSVButton_value_count = 0
        self.CVButton_value_count = 0
        self.CWftButton_value_count = 0
        self.ThThButton_value_count = 0     
        self.CMButton_value_count = 0
        self.SYButton_value_count = 0 
        self.CtnButton_value_count = 0
        self.CWpButton_value_count = 0
        
    #center align
        self.YSVButton_value.setAlignment(Qt.AlignCenter)
        self.CVButton_value.setAlignment(Qt.AlignCenter)
        self.CWftButton_value.setAlignment(Qt.AlignCenter)
        self.ThThButton_value.setAlignment(Qt.AlignCenter) 
        self.CMButton_value.setAlignment(Qt.AlignCenter)
        self.CtnButton_value.setAlignment(Qt.AlignCenter) 
        self.SYButton_value.setAlignment(Qt.AlignCenter)
        self.CWpButton_value.setAlignment(Qt.AlignCenter)         
                  
        
        FabricReport.addWidget(self.YarnFault)
        
# ======================================================Connecting Button click =====================================================================================================
    #in Faultselection
        self.SizeButton.clicked.connect(partial(self.fault_select,"Sizing"))
        self.DyedButton.clicked.connect(partial(self.fault_select,"DyeYarn"))
        self.WeaversButton.clicked.connect(partial(self.fault_select,"Weavers"))
        self.YarnButton.clicked.connect(partial(self.fault_select,"Yarn"))
        self.ExitButton.clicked.connect(partial(self.fault_select,"Exit"))
    
    
    # in Size fault
        self.backButtonSi.clicked.connect(partial(self.back_button,"Sizing"))
        self.Undo_SizeButton.clicked.connect(self.undo_list)
    
        self.SOSButton.clicked.connect(partial(self.write_to_list,"SOSButton"))
        self.SSButton.clicked.connect(partial(self.write_to_list,"SSButton"))
        self.SVButton.clicked.connect(partial(self.write_to_list,"SVButton"))
        self.SPButton.clicked.connect(partial(self.write_to_list,"SPButton"))
        
    #in dyedyarn
        self.backButtonDy.clicked.connect(partial(self.back_button,"DyedYarn"))
        self.Undo_DyeButton.clicked.connect(self.undo_list)
    
        self.COVButton.clicked.connect(partial(self.write_to_list,"COVButton"))
        self.STButton.clicked.connect(partial(self.write_to_list,"STButton"))  
        
    #in Weavers
        self.backButtonWe.clicked.connect(partial(self.back_button,"Weave"))
        self.Undo_WeaveButton.clicked.connect(self.undo_list)
        
        self.DOPButton.clicked.connect(partial(self.write_to_list,"DOPButton"))
        self.HSButton.clicked.connect(partial(self.write_to_list,"HSButton"))
        self.WDRButton.clicked.connect(partial(self.write_to_list,"WDRButton"))
        self.WWftButton.clicked.connect(partial(self.write_to_list,"WWftButton"))
        self.WDTButton.clicked.connect(partial(self.write_to_list,"WDTButton"))
        self.SWButton.clicked.connect(partial(self.write_to_list,"SWButton"))
                
        
        
    #in Yarn
        self.backButtonYa.clicked.connect(partial(self.back_button,"Yarn"))
        self.Undo_YarnButton.clicked.connect(self.undo_list)
        
        self.YSVButton.clicked.connect(partial(self.write_to_list,"YSVButton"))
        self.CVButton.clicked.connect(partial(self.write_to_list,"CVButton"))
        self.CWftButton.clicked.connect(partial(self.write_to_list,"CWftButton"))
        self.ThThButton.clicked.connect(partial(self.write_to_list,"ThThButton"))
        self.CMButton.clicked.connect(partial(self.write_to_list,"CMButton"))
        self.SYButton.clicked.connect(partial(self.write_to_list,"SYButton"))
        self.CtnButton.clicked.connect(partial(self.write_to_list,"CtnButton"))
        self.CWpButton.clicked.connect(partial(self.write_to_list,"CWpButton"))        

        self.retranslateUi(FabricReport)
        FabricReport.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FabricReport)

    def retranslateUi(self, FabricReport):
        _translate = QtCore.QCoreApplication.translate
        FabricReport.setWindowTitle(_translate("FabricReport", "FabricReport"))
        self.ExitButton.setText(_translate("FabricReport", "Exit"))
        self.label_18.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:16pt; font-weight:600; color:#ffffff;\">Meter Reading</span></p></body></html>"))
        self.DyedButton.setText(_translate("FabricReport", "DyedYarn\n"
"Fault"))
        self.SizeButton.setText(_translate("FabricReport", "Sizing\n"
"Fault"))
        self.WeaversButton.setText(_translate("FabricReport", "Weavers\n"
"Fault"))
        self.YarnButton.setText(_translate("FabricReport", "Yarn\n"
"Fault"))
        self.MachineButton.setText(_translate("FabricReport", "Machine\n"
"Fault"))
        self.backButtonSi.setText(_translate("FabricReport", "Back"))
        self.SOSButton.setText(_translate("FabricReport", "S O S - Soft Size"))
        self.Undo_SizeButton.setText(_translate("FabricReport", "Undo"))
        self.SSButton.setText(_translate("FabricReport", "S S - Sizing Stain"))
        self.SPButton.setText(_translate("FabricReport", "S P - Size Patch"))
        self.SVButton.setText(_translate("FabricReport", "S V - Shade Variation"))
        self.SOSButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SSButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SPButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SVButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_32.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.backButtonDy.setText(_translate("FabricReport", "Back"))
        self.COVButton.setText(_translate("FabricReport", "C O V - Color Variation"))
        self.STButton.setText(_translate("FabricReport", "S T - Streaks"))
        self.COVButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.STButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Undo_DyeButton.setText(_translate("FabricReport", "Undo"))
        self.backButtonWe.setText(_translate("FabricReport", "Back"))
        self.label_33.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.Undo_WeaveButton.setText(_translate("FabricReport", "Undo"))
        self.WDRButton.setText(_translate("FabricReport", "W D R - Wrong Drawing "))
        self.WWftButton.setText(_translate("FabricReport", "W Wft - Wrong Weft "))
        self.SWButton.setText(_translate("FabricReport", "S W - Single Weft"))
        self.WDTButton.setText(_translate("FabricReport", "W D T - Wrong Denting "))
        self.HSButton.setText(_translate("FabricReport", "H S - Handing Stain"))
        self.DOPButton.setText(_translate("FabricReport", "D O P - Double Pick"))
        self.WDRButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.WDTButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SWButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.WWftButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.HSButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.DOPButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_34.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.ThThButton.setText(_translate("FabricReport", "Th Th - Thick and Thin"))
        self.CtnButton.setText(_translate("FabricReport", "Ctn - Contamination"))
        self.backButtonYa.setText(_translate("FabricReport", "Back"))
        self.CWftButton.setText(_translate("FabricReport", "C Wft - Count Weft"))
        self.SYButton.setText(_translate("FabricReport", "S Y - Slup Yarn"))
        self.CMButton.setText(_translate("FabricReport", "C M - Count Mixer"))
        self.CWpButton.setText(_translate("FabricReport", "C Wp - Cross Warp"))
        self.Undo_YarnButton.setText(_translate("FabricReport", "Undo"))
        self.CVButton.setText(_translate("FabricReport", "C V - Count Variation"))
        self.YSVButton.setText(_translate("FabricReport", "Y S V - Yarn Shade Variation"))
        self.CtnButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.CWftButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.CVButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SYButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.CMButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ThThButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.CWpButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.YSVButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
import imagetest


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    FabricReport = QtWidgets.QStackedWidget()
    ui = Ui_FabricReport()
    ui.setupUi(FabricReport)
    FabricReport.show()
    sys.exit(app.exec_())
