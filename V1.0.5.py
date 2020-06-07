# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QPushButton
from PyQt5.QtCore import Qt
from functools import partial
import time
import csv
import sys
import requests
import json





class Ui_FabricReport(object):

    
    list_faults = []
    entry = []
    Uniqueid=""
    def post1(self,to_do):
        
        #self.Uniqueid="1234"
        try:
            url = 'http://127.0.0.1:8000/Tables/'
            headers = {'Authorization': 'Token b8dc659452f04a71aded929b6dcbf628a674068b'}    
       
            if(to_do== "OnSaveAndProceed"):
                
                post1data = {
                    'loom_no':self.LoomEdit.text() ,
                    'piece_no':self.PieceEdit.text() ,
                    'set_no':self.SetEDit.text() ,
                    'beam_no':self.BeamEdit.text() ,
                    'Date':self.DateEdit.text(),
                    'Descrip':self.DescEdit.text(),
                    'Time':self.TimeEdit.text(),
                    'Weave':self.WeaveEdit.text(),
                    'Weft_Count':self.WeftEdit.text(),
                    'Act_Width':self.WidthEdit.text(),
                    'Warp_Count':self.WarpEdit.text(),
                    'Sound_MTRSC':self.SoundEdit.text(),
                    'DOFE_MTRS':self.DofeEdit.text(),
                    'Act_EPI':self.EPEdit.text(),
                    'Act_PPI':self.PPEdit.text(),
                    'Doffed_Shift':self.DoffEdit.text(),
                    }
                
                if(len(self.LoomEdit.text())==0 or len(self.PieceEdit.text())==0 or len(self.SetEDit.text())==0 or len(self.BeamEdit.text())==0):
                    self.ContinueButton.setEnabled(False)
                    self.messagewarn("Some text field is empty",0)
                    
                else:            
                    response = requests.post(url, headers=headers, data= post1data)
                    resp_retun=response.text
                    res = json.loads(resp_retun) 
                    self.Uniqueid= res.get('Unique_id')   # add/ pass id variable here
                    if self.Uniqueid == None:
                        self.messagewarn("Authentication failed", 0)
                    else:
                        self.fault_select("Selection")
              
            

            # print(Uniqueid)
            if(to_do=="OnBackButton"):
                for i in range(len(self.list_faults)):
                    post2data ={'Unique_id':self.Uniqueid,
                                'meter_read':self.list_faults[i][1],
                                'fault':self.list_faults[i][2]
                                } 
                    response = requests.post(url, headers=headers, data= post2data)
            #if(to_do=="OnExitButton"):   
                #post3data={'Unique_id_current': self.Uniqueid}
                #response = requests.post(url, headers=headers, data= post3data)
                    
            if(to_do=="OnContinue"): 
                self.Uniqueid=self.UIDEdit.text()
                
                post4data={'Unique_id_continue': self.Uniqueid}
                response = requests.post(url, headers=headers, data= post4data)
                resp_retun=response.text
                res = json.loads(resp_retun) 
                self.checkoncontinue= res.get('Unique_id_continue') 
                if(self.checkoncontinue=="No"):
                    self.messagewarn("UID doesn't Match", 0)
                else:
                    self.fault_select("Selection")
            
        except requests.exceptions.ConnectionError:
            # r.status_code = "Connection refused"
            self.messagewarn("Connection Error....Check Server",0)
            #print("connectionerror")                   
   
    #def Buttonenable(self):
        #if((self.LoomEdit.text()).isEmpty()):
            #self.UIDEdit.setEnabled(False)
            #self.ContinueButton.setEnabled(False)
        #else:
            #self.fault_select("Selection")
    def messagewarn(self,message,connect):
        if(connect==0):
            warning= QMessageBox()
            warning.setWindowTitle("Warning!")
            warning.setText(message)
            warning.setIcon(QMessageBox.Critical)
            warning.exec_()   
        else:
            if(len(self.UIDEdit.text()) > 0):
                self.SaveProceedButton.setEnabled(False)
                self.ContinueButton.setEnabled(True)
           
            
    def fault_select(self,fault):
        if (fault=="Selection"):
            f = open(self.Uniqueid+".csv",'a')
            f.close()          
            self.UIDlabel.setText( self.Uniqueid)
            FabricReport.setCurrentIndex(1)        
        if (fault=="Sizing"):
            FabricReport.setCurrentIndex(2)
        if (fault=="DyeYarn"):
            FabricReport.setCurrentIndex(3) 
        if (fault=="Weavers"):
            FabricReport.setCurrentIndex(4)
        if (fault=="Yarn"):
            FabricReport.setCurrentIndex(5)
        if (fault=="Machine1"):
            FabricReport.setCurrentIndex(6) 
        if (fault=="Machine2"):
            FabricReport.setCurrentIndex(7) 
        if (fault=="Machine3"):
            FabricReport.setCurrentIndex(8)
        if (fault=="Exit"):
            warn= QMessageBox()
            warn.setWindowTitle("Warning!")
            warn.setText("Do u Want to close?")
            warn.setIcon(QMessageBox.Question)
            warn.setStandardButtons(QMessageBox.Yes)
            warn.addButton( QMessageBox.No)
            warn.setDefaultButton(QMessageBox.No)
            if warn.exec_()==QMessageBox.Yes:
                app = QtWidgets.QApplication(sys.argv)
                app.closeAllWindows() 
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
                
        #Machine Faults
            if (name=="EHButton"):
                self.EHButton_value_count = self.EHButton_value_count + 1
                self.EHButton_value.setText(str(self.EHButton_value_count))
            if (name=="HButton"):
                self.HButton_value_count = self.HButton_value_count + 1
                self.HButton_value.setText(str(self.HButton_value_count))
            if (name=="LMButton"):
                self.LMButton_value_count = self.LMButton_value_count + 1
                self.LMButton_value.setText(str(self.LMButton_value_count))
            if (name=="LWPButton"):
                self.LWPButton_value_count = self.LWPButton_value_count + 1
                self.LWPButton_value.setText(str(self.LWPButton_value_count))
        
            if (name=="MBButton"):
                self.MBButton_value_count = self.MBButton_value_count + 1
                self.MBButton_value.setText(str(self.MBButton_value_count))
            if (name=="OWPButton"):
                self.OWPButton_value_count = self.OWPButton_value_count + 1
                self.OWPButton_value.setText(str(self.OWPButton_value_count))
    
                   
            if (name=="RMButton"):
                self.RMButton_value_count = self.RMButton_value_count + 1
                self.RMButton_value.setText(str(self.RMButton_value_count))
            if (name=="SMButton"):
                self.SMButton_value_count = self.SMButton_value_count + 1
                self.SMButton_value.setText(str(self.SMButton_value_count))
            if (name=="TMButton"):
                self.TMButton_value_count = self.TMButton_value_count + 1
                self.TMButton_value.setText(str(self.TMButton_value_count))
            
            #2
            if (name=="BPButton"):
                self.BPButton_value_count = self.BPButton_value_count + 1
                self.BPButton_value.setText(str(self.BPButton_value_count))
        
            if (name=="CRButton"):
                self.CRButton_value_count = self.CRButton_value_count + 1
                self.CRButton_value.setText(str(self.CRButton_value_count))
            if (name=="DEButton"):
                self.DEButton_value_count = self.DEButton_value_count + 1
                self.DEButton_value.setText(str(self.DEButton_value_count))        
                
        
            if (name=="FLButton"):
                self.FLButton_value_count = self.FLButton_value_count + 1
                self.FLButton_value.setText(str(self.FLButton_value_count))
            if (name=="LOButton"):
                self.LOButton_value_count = self.LOButton_value_count + 1
                self.LOButton_value.setText(str(self.LOButton_value_count))
            if (name=="MEButton"):
                self.MEButton_value_count = self.MEButton_value_count + 1
                self.MEButton_value.setText(str(self.MEButton_value_count))
            if (name=="SEFButton"):
                self.SEFButton_value_count = self.SEFButton_value_count + 1
                self.SEFButton_value.setText(str(self.SEFButton_value_count))
            if (name=="TERButton"):
                self.TERButton_value_count = self.TERButton_value_count + 1
                self.TERButton_value.setText(str(self.TERButton_value_count))
            if (name=="TLButton"):
                self.TLButton_value_count = self.TLButton_value_count + 1
                self.TLButton_value.setText(str(self.TLButton_value_count))       
            #3
            
            if (name=="BSButton"):
                self.BSButton_value_count = self.BSButton_value_count + 1
                self.BSButton_value.setText(str(self.BSButton_value_count))
            if (name=="BTNButton"):
                self.BTNButton_value_count = self.BTNButton_value_count + 1
                self.BTNButton_value.setText(str(self.BTNButton_value_count))             

            if (name=="DMButton"):
                self.DMButton_value_count = self.DMButton_value_count + 1
                self.DMButton_value.setText(str(self.DMButton_value_count))
            if (name=="DPButton"):
                self.DPButton_value_count = self.DPButton_value_count + 1
                self.DPButton_value.setText(str(self.DPButton_value_count))
            if (name=="OWftButton"):
                self.OWftButton_value_count = self.OWftButton_value_count + 1
                self.OWftButton_value.setText(str(self.OWftButton_value_count))       
            if (name=="TCButton"):
                self.TCButton_value_count = self.TCButton_value_count + 1
                self.TCButton_value.setText(str(self.TCButton_value_count))
            if (name=="TPButton"):
                self.TPButton_value_count = self.TPButton_value_count + 1
                self.TPButton_value.setText(str(self.TPButton_value_count))               
          
            
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
       
        #Machine Fault
    
            if (name=="EHButton"):
                self.EHButton_value_count = self.EHButton_value_count - 1
                if self.EHButton_value_count == 0 : 
                    self.EHButton_value.setText("")
                else :
                    self.EHButton_value.setText(str(self.EHButton_value_count))
            if (name=="HButton"):
                self.HButton_value_count = self.HButton_value_count - 1
                if self.HButton_value_count == 0 : 
                    self.HButton_value.setText("")
                else :
                    self.HButton_value.setText(str(self.HButton_value_count))
            if (name=="LMButton"):
                self.LMButton_value_count = self.LMButton_value_count - 1
                if self.LMButton_value_count == 0 : 
                    self.LMButton_value.setText("")
                else :
                    self.LMButton_value.setText(str(self.LMButton_value_count))
            if (name=="LWPButton"):
                self.LWPButton_value_count = self.LWPButton_value_count - 1
                if self.LWPButton_value_count == 0 : 
                    self.LWPButton_value.setText("")
                else :
                    self.LWPButton_value.setText(str(self.LWPButton_value_count))
         
            if (name=="MBButton"):
                self.MBButton_value_count = self.MBButton_value_count - 1
                if self.MBButton_value_count == 0 : 
                    self.MBButton_value.setText("")
                else :
                    self.MBButton_value.setText(str(self.MBButton_value_count))
            if (name=="OWPButton"):
                self.OWPButton_value_count = self.OWPButton_value_count - 1
                if self.OWPButton_value_count == 0 : 
                    self.OWPButton_value.setText("")
                else :
                    self.OWPButton_value.setText(str(self.OWPButton_value_count))    

       
        
            if (name=="RMButton"):
                self.RMButton_value_count = self.RMButton_value_count - 1
                if self.RMButton_value_count == 0 : 
                    self.RMButton_value.setText("")
                else :
                    self.RMButton_value.setText(str(self.RMButton_value_count))
            if (name=="SMButton"):
                self.SMButton_value_count = self.SMButton_value_count - 1
                if self.SMButton_value_count == 0 : 
                    self.SMButton_value.setText("")
                else :
                    self.SMButton_value.setText(str(self.SMButton_value_count))
            if (name=="TMButton"):
                self.TMButton_value_count = self.TMButton_value_count - 1
                if self.TMButton_value_count == 0 : 
                    self.TMButton_value.setText("")
                else :
                    self.TMButton_value.setText(str(self.TMButton_value_count))
        #2
            
            if (name=="BPButton"):
                self.BPButton_value_count = self.BPButton_value_count - 1
                if self.BPButton_value_count == 0 : 
                    self.BPButton_value.setText("")
                else :
                    self.BPButton_value.setText(str(self.BPButton_value_count))
            if (name=="CRButton"):
                self.CRButton_value_count = self.CRButton_value_count - 1
                if self.CRButton_value_count == 0 : 
                    self.CRButton_value.setText("")
                else :
                    self.CRButton_value.setText(str(self.CRButton_value_count))
            if (name=="DEButton"):
                self.DEButton_value_count = self.DEButton_value_count - 1
                if self.DEButton_value_count == 0 : 
                    self.DEButton_value.setText("")
                else :
                    self.DEButton_value.setText(str(self.DEButton_value_count))  
                    
      
            if (name=="FLButton"):
                self.FLButton_value_count = self.FLButton_value_count - 1
                if self.FLButton_value_count == 0 : 
                    self.FLButton_value.setText("")
                else :
                    self.FLButton_value.setText(str(self.FLButton_value_count))
            if (name=="LOButton"):
                self.LOButton_value_count = self.LOButton_value_count - 1
                if self.LOButton_value_count == 0 : 
                    self.LOButton_value.setText("")
                else :
                    self.LOButton_value.setText(str(self.LOButton_value_count))
            if (name=="MEButton"):
                self.MEButton_value_count = self.MEButton_value_count - 1
                if self.MEButton_value_count == 0 : 
                    self.MEButton_value.setText("")
                else :
                    self.MEButton_value.setText(str(self.MEButton_value_count))
            if (name=="SEFButton"):
                self.SEFButton_value_count = self.SEFButton_value_count - 1
                if self.SEFButton_value_count == 0 : 
                    self.SEFButton_value.setText("")
                else :
                    self.SEFButton_value.setText(str(self.SEFButton_value_count))
            if (name=="TERButton"):
                self.TERButton_value_count = self.TERButton_value_count - 1
                if self.TERButton_value_count == 0 : 
                    self.TERButton_value.setText("")
                else :
                    self.TERButton_value.setText(str(self.TERButton_value_count))
            if (name=="TLButton"):
                self.TLButton_value_count = self.TLButton_value_count - 1
                if self.TLButton_value_count == 0 : 
                    self.TLButton_value.setText("")
                else :
                    self.TLButton_value.setText(str(self.TLButton_value_count))
                    
        #3
            if (name=="BSButton"):
                self.BSButton_value_count = self.BSButton_value_count - 1
                if self.BSButton_value_count == 0 : 
                    self.BSButton_value.setText("")
                else :
                    self.BSButton_value.setText(str(self.BSButton_value_count))
            if (name=="DMButton"):
                self.DMButton_value_count = self.DMButton_value_count - 1
                if self.DMButton_value_count == 0 : 
                    self.DMButton_value.setText("")
                else :
                    self.DMButton_value.setText(str(self.DMButton_value_count))  
            
           
            if (name=="BTNButton"):
                self.BTNButton_value_count = self.BTNButton_value_count - 1
                if self.BTNButton_value_count == 0 : 
                    self.BTNButton_value.setText("")
                else :
                    self.BTNButton_value.setText(str(self.BTNButton_value_count))            
            if (name=="DPButton"):
                self.DPButton_value_count = self.DPButton_value_count - 1
                if self.DPButton_value_count == 0 : 
                    self.DPButton_value.setText("")
                else :
                    self.DPButton_value.setText(str(self.DPButton_value_count))
            if (name=="OWftButton"):
                self.OWftButton_value_count = self.OWftButton_value_count - 1
                if self.OWftButton_value_count == 0 : 
                    self.OWftButton_value.setText("")
                else :
                    self.OWftButton_value.setText(str(self.OWftButton_value_count))
            if (name=="TCButton"):
                self.TCButton_value_count = self.TCButton_value_count - 1
                if self.TCButton_value_count == 0 : 
                    self.TCButton_value.setText("")
                else :
                    self.TCButton_value.setText(str(self.TCButton_value_count))
            if (name=="TPButton"):
                self.TPButton_value_count = self.TPButton_value_count - 1
                if self.TPButton_value_count == 0 : 
                    self.TPButton_value.setText("")
                else :
                    self.TPButton_value.setText(str(self.TPButton_value_count))  
            
                    
            

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

        f = open(self.Uniqueid+".csv",'a')
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
        
    #Machin fault    
        if name == "Machine":  
            self.EHButton_value_count = 0
            self.HButton_value_count = 0
            self.LMButton_value_count = 0
            self.LWPButton_value_count = 0
            self.MBButton_value_count = 0
            self.OWPButton_value_count = 0
            self.RMButton_value_count = 0
            self.SMButton_value_count = 0            
            self.TMButton_value_count = 0 
            
            self.EHButton_value.setText("")
            self.HButton_value.setText("")
            self.LMButton_value.setText("")
            self.LWPButton_value.setText("")
            self.MBButton_value.setText("")
            self.OWPButton_value.setText("")
            self.RMButton_value.setText("")
            self.SMButton_value.setText("")
            self.TMButton_value.setText("")
            
        #if name == "Machine2":  
            self.BPButton_value_count = 0
            self.CRButton_value_count = 0
            self.DEButton_value_count = 0
            self.FLButton_value_count = 0
            self.LOButton_value_count = 0
            self.MEButton_value_count = 0
            self.SEFButton_value_count = 0
            self.TERButton_value_count = 0              
            self.TLButton_value_count = 0  
            
            self.BPButton_value.setText("")
            self.CRButton_value.setText("")
            self.DEButton_value.setText("")
            self.FLButton_value.setText("")
            self.LOButton_value.setText("")
            self.MEButton_value.setText("")
            self.SEFButton_value.setText("")
            self.TERButton_value.setText("")
            self.TLButton_value.setText("")            
            
            
            
        #if name == "Machine3":  
            self.BSButton_value_count = 0
            self.BTNButton_value_count = 0
            self.DMButton_value_count = 0
            self.DPButton_value_count = 0
            self.OWftButton_value_count = 0
            self.TCButton_value_count = 0
            self.TPButton_value_count = 0
            
            self.BSButton_value.setText("")
            self.BTNButton_value.setText("")
            self.DMButton_value.setText("")
            self.DPButton_value.setText("")
            self.OWftButton_value.setText("")
            self.TCButton_value.setText("")
            self.TPButton_value.setText("")
            
                        
                      
            
            
    #Back to Faultselection    
        FabricReport.setCurrentIndex(1)
            

# ======================================================After this QT5 UI portion generated using PyUic =============================================================================

    
    def setupUi(self, FabricReport):
        FabricReport.setObjectName("FabricReport")
        FabricReport.resize(1085, 604)
        FabricReport.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.454545 rgba(235, 148, 61, 255), stop:0.98 rgba(108, 65, 38, 255), stop:1 rgba(0, 0, 0, 0));")
        
#===============================================MainPage=============================
                
       
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.mainpagelabel = QtWidgets.QLabel(self.MainPage)
        self.mainpagelabel.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.mainpagelabel.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.mainpagelabel.setObjectName("mainpagelabel")
        self.SetEDit = QtWidgets.QLineEdit(self.MainPage)
        self.SetEDit.setGeometry(QtCore.QRect(900, 200, 141, 71))
        self.SetEDit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SetEDit.setObjectName("SetEDit")
        self.ActEPI = QtWidgets.QLabel(self.MainPage)
        self.ActEPI.setGeometry(QtCore.QRect(390, 360, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ActEPI.setFont(font)
        self.ActEPI.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.ActEPI.setLineWidth(1)
        self.ActEPI.setIndent(-1)
        self.ActEPI.setObjectName("ActEPI")
        self.DofeEdit = QtWidgets.QLineEdit(self.MainPage)
        self.DofeEdit.setGeometry(QtCore.QRect(900, 360, 141, 71))
        self.DofeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DofeEdit.setObjectName("DofeEdit")
        self.EPEdit = QtWidgets.QLineEdit(self.MainPage)
        self.EPEdit.setGeometry(QtCore.QRect(550, 360, 141, 71))
        self.EPEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EPEdit.setObjectName("EPEdit")
        self.SaveProceedButton = QtWidgets.QPushButton(self.MainPage)
        self.SaveProceedButton.setGeometry(QtCore.QRect(70, 530, 571, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 143, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.SaveProceedButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.SaveProceedButton.setFont(font)
        self.SaveProceedButton.setStyleSheet("background-color: rgb(145, 143, 168);")
        self.SaveProceedButton.setObjectName("SaveProceedButton")
        self.MTRSC = QtWidgets.QLabel(self.MainPage)
        self.MTRSC.setGeometry(QtCore.QRect(390, 440, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MTRSC.setFont(font)
        self.MTRSC.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.MTRSC.setObjectName("MTRSC")
        self.WeaveEdit = QtWidgets.QLineEdit(self.MainPage)
        self.WeaveEdit.setGeometry(QtCore.QRect(550, 200, 141, 71))
        self.WeaveEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WeaveEdit.setObjectName("WeaveEdit")
        self.Loom = QtWidgets.QLabel(self.MainPage)
        self.Loom.setGeometry(QtCore.QRect(30, 120, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Loom.setFont(font)
        self.Loom.setMouseTracking(True)
        self.Loom.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.Loom.setObjectName("Loom")
        self.DoffedShift = QtWidgets.QLabel(self.MainPage)
        self.DoffedShift.setGeometry(QtCore.QRect(30, 200, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DoffedShift.setFont(font)
        self.DoffedShift.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.DoffedShift.setLineWidth(1)
        self.DoffedShift.setIndent(-1)
        self.DoffedShift.setObjectName("DoffedShift")
        self.DoffEdit = QtWidgets.QLineEdit(self.MainPage)
        self.DoffEdit.setGeometry(QtCore.QRect(210, 200, 141, 71))
        self.DoffEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DoffEdit.setObjectName("DoffEdit")
        self.SoundEdit = QtWidgets.QLineEdit(self.MainPage)
        self.SoundEdit.setGeometry(QtCore.QRect(550, 440, 141, 71))
        self.SoundEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SoundEdit.setObjectName("SoundEdit")
        self.set = QtWidgets.QLabel(self.MainPage)
        self.set.setGeometry(QtCore.QRect(730, 200, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.set.setFont(font)
        self.set.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.set.setLineWidth(1)
        self.set.setIndent(-1)
        self.set.setObjectName("set")
        self.descr = QtWidgets.QLabel(self.MainPage)
        self.descr.setGeometry(QtCore.QRect(30, 440, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.descr.setFont(font)
        self.descr.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.descr.setObjectName("descr")
        self.BeamEdit = QtWidgets.QLineEdit(self.MainPage)
        self.BeamEdit.setGeometry(QtCore.QRect(900, 280, 141, 71))
        self.BeamEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BeamEdit.setObjectName("BeamEdit")
        self.DateEdit = QtWidgets.QLineEdit(self.MainPage)
        self.DateEdit.setGeometry(QtCore.QRect(60, 70, 141, 31))
        self.DateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DateEdit.setObjectName("DateEdit")
        
        #self.DateEdit.setText()
        
        self.actualwidth = QtWidgets.QLabel(self.MainPage)
        self.actualwidth.setGeometry(QtCore.QRect(390, 120, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actualwidth.setFont(font)
        self.actualwidth.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.actualwidth.setObjectName("actualwidth")
        self.Beamno = QtWidgets.QLabel(self.MainPage)
        self.Beamno.setGeometry(QtCore.QRect(730, 280, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Beamno.setFont(font)
        self.Beamno.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.Beamno.setObjectName("Beamno")
        self.WeftEdit = QtWidgets.QLineEdit(self.MainPage)
        self.WeftEdit.setGeometry(QtCore.QRect(210, 360, 141, 71))
        self.WeftEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WeftEdit.setObjectName("WeftEdit")
        self.PPEdit = QtWidgets.QLineEdit(self.MainPage)
        self.PPEdit.setGeometry(QtCore.QRect(550, 280, 141, 71))
        self.PPEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PPEdit.setObjectName("PPEdit")
        self.PieceEdit = QtWidgets.QLineEdit(self.MainPage)
        self.PieceEdit.setGeometry(QtCore.QRect(900, 120, 141, 71))
        self.PieceEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PieceEdit.setObjectName("PieceEdit")
        self.warpcount = QtWidgets.QLabel(self.MainPage)
        self.warpcount.setGeometry(QtCore.QRect(30, 280, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.warpcount.setFont(font)
        self.warpcount.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.warpcount.setObjectName("warpcount")
        self.MTRS = QtWidgets.QLabel(self.MainPage)
        self.MTRS.setGeometry(QtCore.QRect(730, 360, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MTRS.setFont(font)
        self.MTRS.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.MTRS.setObjectName("MTRS")
        self.actPPI = QtWidgets.QLabel(self.MainPage)
        self.actPPI.setGeometry(QtCore.QRect(390, 280, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actPPI.setFont(font)
        self.actPPI.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.actPPI.setLineWidth(1)
        self.actPPI.setIndent(-1)
        self.actPPI.setObjectName("actPPI")
        self.WidthEdit = QtWidgets.QLineEdit(self.MainPage)
        self.WidthEdit.setGeometry(QtCore.QRect(550, 120, 141, 71))
        self.WidthEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WidthEdit.setObjectName("WidthEdit")
        self.LoomEdit = QtWidgets.QLineEdit(self.MainPage)
        self.LoomEdit.setGeometry(QtCore.QRect(210, 120, 141, 71))
        self.LoomEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LoomEdit.setObjectName("LoomEdit")
        self.Date = QtWidgets.QLabel(self.MainPage)
        self.Date.setGeometry(QtCore.QRect(60, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Date.setFont(font)
        self.Date.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(243, 243, 243);")
        self.Date.setObjectName("Date")
        self.WarpEdit = QtWidgets.QLineEdit(self.MainPage)
        self.WarpEdit.setGeometry(QtCore.QRect(210, 280, 141, 71))
        self.WarpEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WarpEdit.setObjectName("WarpEdit")
        self.TimeEdit = QtWidgets.QLineEdit(self.MainPage)
        self.TimeEdit.setGeometry(QtCore.QRect(860, 70, 141, 31))
        self.TimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TimeEdit.setObjectName("TimeEdit")
        self.time = QtWidgets.QLabel(self.MainPage)
        self.time.setGeometry(QtCore.QRect(860, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(243, 243, 243);\n"
"")
        self.time.setObjectName("time")
        self.piece = QtWidgets.QLabel(self.MainPage)
        self.piece.setGeometry(QtCore.QRect(730, 120, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.piece.setFont(font)
        self.piece.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.piece.setObjectName("piece")
        self.title = QtWidgets.QLabel(self.MainPage)
        self.title.setGeometry(QtCore.QRect(240, 20, 581, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.title.setObjectName("title")
        self.DescEdit = QtWidgets.QLineEdit(self.MainPage)
        self.DescEdit.setGeometry(QtCore.QRect(210, 440, 141, 71))
        self.DescEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DescEdit.setObjectName("DescEdit")
        self.weave = QtWidgets.QLabel(self.MainPage)
        self.weave.setGeometry(QtCore.QRect(390, 200, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.weave.setFont(font)
        self.weave.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.weave.setObjectName("weave")
        self.weftcount = QtWidgets.QLabel(self.MainPage)
        self.weftcount.setGeometry(QtCore.QRect(30, 360, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.weftcount.setFont(font)
        self.weftcount.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.weftcount.setObjectName("weftcount")
        self.ContinueButton = QtWidgets.QPushButton(self.MainPage)
        self.ContinueButton.setEnabled(False)
        self.ContinueButton.setGeometry(QtCore.QRect(730, 530, 311, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.ContinueButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.ContinueButton.setFont(font)
        self.ContinueButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.ContinueButton.setObjectName("ContinueButton")
        self.UID = QtWidgets.QLabel(self.MainPage)
        self.UID.setGeometry(QtCore.QRect(730, 450, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.UID.setFont(font)
        self.UID.setStyleSheet("background-color: rgb(64, 153, 191);\n"
"color: rgb(243, 243, 243);")
        self.UID.setObjectName("UID")
        self.UIDEdit = QtWidgets.QLineEdit(self.MainPage)
        self.UIDEdit.setGeometry(QtCore.QRect(900, 450, 141, 71))
        self.UIDEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UIDEdit.setObjectName("UIDEdit")
        self.frame = QtWidgets.QFrame(self.MainPage)
        self.frame.setGeometry(QtCore.QRect(710, 440, 351, 171))
        self.frame.setStyleSheet("background-color: rgb(145, 143, 168);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.Logoframe = QtWidgets.QFrame(self.MainPage)
        self.Logoframe.setGeometry(QtCore.QRect(220, 20, 91, 91))
        self.Logoframe.setStyleSheet("border-image: url(:/newPrefix/logo.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.Logoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Logoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logoframe.setObjectName("Logoframe") 
        
        self.mainpagelabel.raise_()
        self.SetEDit.raise_()
        self.ActEPI.raise_()
        self.DofeEdit.raise_()
        self.EPEdit.raise_()
        self.SaveProceedButton.raise_()
        self.MTRSC.raise_()
        self.WeaveEdit.raise_()
        self.Loom.raise_()
        self.DoffedShift.raise_()
        self.DoffEdit.raise_()
        self.SoundEdit.raise_()
        self.set.raise_()
        self.descr.raise_()
        self.BeamEdit.raise_()
        self.DateEdit.raise_()
        self.actualwidth.raise_()
        self.Beamno.raise_()
        self.WeftEdit.raise_()
        self.PPEdit.raise_()
        self.PieceEdit.raise_()
        self.warpcount.raise_()
        self.MTRS.raise_()
        self.actPPI.raise_()
        self.WidthEdit.raise_()
        self.LoomEdit.raise_()
        self.Date.raise_()
        self.WarpEdit.raise_()
        self.TimeEdit.raise_()
        self.time.raise_()
        self.piece.raise_()
        self.title.raise_()
        self.DescEdit.raise_()
        self.weave.raise_()
        self.weftcount.raise_()
        self.frame.raise_()
        self.UID.raise_()
        self.UIDEdit.raise_()
        self.ContinueButton.raise_()
        
        
        self.UIDEdit.textChanged.connect(partial(self.messagewarn,"",1))
               
        
        self.Logoframe.raise_()
        FabricReport.addWidget(self.MainPage)
        
        
        
#==========================================FaultSelection Page============================
                 
        self.FaultSelection = QtWidgets.QWidget()
        self.FaultSelection.setObjectName("FaultSelection")
        self.Faultlabel = QtWidgets.QLabel(self.FaultSelection)
        self.Faultlabel.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.Faultlabel.setStyleSheet("border-image: url(:/newPrefix/Capture 6.JPG);")
        self.Faultlabel.setObjectName("Faultlabel")
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
        self.Meter = QtWidgets.QLabel(self.FaultSelection)
        self.Meter.setGeometry(QtCore.QRect(710, 140, 281, 51))
        self.Meter.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.Meter.setObjectName("Meter")
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
        self.MeterEdit = QtWidgets.QLineEdit(self.FaultSelection)
        self.MeterEdit.setGeometry(QtCore.QRect(720, 200, 251, 41))
        self.MeterEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.MeterEdit.setObjectName("MeterEdit")
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
        
        self.UIDlabeltext = QtWidgets.QLabel(self.FaultSelection)
        self.UIDlabeltext.setGeometry(QtCore.QRect(460, 160, 171, 41))
        self.UIDlabeltext.setText("UID :")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.UIDlabeltext.setFont(font)
        self.UIDlabeltext.setStyleSheet("background-color: rgb(85, 170, 0);color: rgb(243, 243, 243);" )    
        self.UIDlabeltext.setObjectName("UIDlabeltext")     
        
        self.UIDlabel = QtWidgets.QLabel(self.FaultSelection)
        self.UIDlabel.setGeometry(QtCore.QRect(460, 210, 171, 41))
        #self.UIDlabel.setText("UID :")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.UIDlabel.setFont(font)
        self.UIDlabel.setStyleSheet("background-color: rgb(255, 255, 255);" )    
        self.UIDlabel.setObjectName("UIDlabel")             
        
        self.UIDlabel.setAlignment(Qt.AlignCenter)
        self.UIDlabeltext.setAlignment(Qt.AlignCenter)
        
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
        
    #values
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
        
        
        self.SizLabel = QtWidgets.QLabel(self.SizingFault)
        self.SizLabel.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.SizLabel.setStyleSheet("border-image: url(:/newPrefix/Capture.JPG);")
        self.SizLabel.setObjectName("SizLabel")
        self.undo_siz_label = QtWidgets.QFrame(self.SizingFault)
        self.undo_siz_label.setGeometry(QtCore.QRect(460, 70, 31, 21))
        self.undo_siz_label.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.undo_siz_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.undo_siz_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.undo_siz_label.setObjectName("undo_siz_label")
        self.Save_siz_frame = QtWidgets.QFrame(self.SizingFault)
        self.Save_siz_frame.setGeometry(QtCore.QRect(640, 500, 41, 31))
        self.Save_siz_frame.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.Save_siz_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Save_siz_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Save_siz_frame.setObjectName("Save_siz_frame")
        self.SizLabel.raise_()
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
        self.undo_siz_label.raise_()
        self.Save_siz_frame.raise_()
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
        self.DyeFrame = QtWidgets.QFrame(self.DyedYarnFault)
        self.DyeFrame.setGeometry(QtCore.QRect(0, 0, 1091, 611))
        self.DyeFrame.setStyleSheet("border-image: url(:/newPrefix/Capture 7.JPG);")
        self.DyeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DyeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DyeFrame.setObjectName("DyeFrame")
        self.save_dye_frame = QtWidgets.QFrame(self.DyedYarnFault)
        self.save_dye_frame.setGeometry(QtCore.QRect(650, 490, 41, 31))
        self.save_dye_frame.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.save_dye_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.save_dye_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.save_dye_frame.setObjectName("save_dye_frame")
        self.Undo_dye_Frame = QtWidgets.QFrame(self.DyedYarnFault)
        self.Undo_dye_Frame.setGeometry(QtCore.QRect(450, 90, 31, 21))
        self.Undo_dye_Frame.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.Undo_dye_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Undo_dye_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Undo_dye_Frame.setObjectName("Undo_dye_Frame")
        self.DyeFrame.raise_()
        self.backButtonDy.raise_()
        self.COVButton.raise_()
        self.STButton.raise_()
        self.STButton_value.raise_()
        self.Undo_DyeButton.raise_()
        self.COVButton_value.raise_()
        self.save_dye_frame.raise_()
        self.Undo_dye_Frame.raise_()
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
        self.WeavLabel = QtWidgets.QLabel(self.WeaveFault)
        self.WeavLabel.setGeometry(QtCore.QRect(0, -10, 1091, 611))
        self.WeavLabel.setStyleSheet("border-image: url(:/newPrefix/Capture2.JPG);")
        self.WeavLabel.setObjectName("WeavLabel")
        
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
    
        
        self.UndoWeavFrame = QtWidgets.QFrame(self.WeaveFault)
        self.UndoWeavFrame.setGeometry(QtCore.QRect(450, 60, 31, 21))
        self.UndoWeavFrame.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.UndoWeavFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UndoWeavFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UndoWeavFrame.setObjectName("UndoWeavFrame")
        self.SavWeavFrame = QtWidgets.QFrame(self.WeaveFault)
        self.SavWeavFrame.setGeometry(QtCore.QRect(650, 490, 41, 31))
        self.SavWeavFrame.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.SavWeavFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SavWeavFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SavWeavFrame.setObjectName("SavWeavFrame")
        self.WeavLabel.raise_()
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
        self.UndoWeavFrame.raise_()
        self.SavWeavFrame.raise_()
        FabricReport.addWidget(self.WeaveFault)
        
#===============================================================YarnFault======================================================        

        self.YarnFault = QtWidgets.QWidget()
        self.YarnFault.setObjectName("YarnFault")
        self.YarnLabel = QtWidgets.QLabel(self.YarnFault)
        self.YarnLabel.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.YarnLabel.setStyleSheet("border-image: url(:/newPrefix/Capture 8.JPG);")
        self.YarnLabel.setObjectName("YarnLabel")
        
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
        self.SavYarnFrame = QtWidgets.QFrame(self.YarnFault)
        self.SavYarnFrame.setGeometry(QtCore.QRect(660, 500, 41, 31))
        self.SavYarnFrame.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.SavYarnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SavYarnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SavYarnFrame.setObjectName("SavYarnFrame")
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
        self.UndoYarnframe = QtWidgets.QFrame(self.YarnFault)
        self.UndoYarnframe.setGeometry(QtCore.QRect(500, 40, 31, 21))
        self.UndoYarnframe.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.UndoYarnframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UndoYarnframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UndoYarnframe.setObjectName("UndoYarnframe")
       
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
        
        
        self.YarnLabel.raise_()
        self.ThThButton.raise_()
        self.CtnButton.raise_()
        self.backButtonYa.raise_()
        self.CWftButton.raise_()
        self.SavYarnFrame.raise_()
        self.SYButton.raise_()
        self.CMButton.raise_()
        self.CWpButton.raise_()
        self.Undo_YarnButton.raise_()
        self.CVButton.raise_()
        self.YSVButton.raise_()
        self.CtnButton_value.raise_()
        self.CWftButton_value.raise_()
        self.CVButton_value.raise_()
        self.SYButton_value.raise_()
        self.CMButton_value.raise_()
        self.ThThButton_value.raise_()
        self.CWpButton_value.raise_()
        self.YSVButton_value.raise_()
        self.UndoYarnframe.raise_()
        FabricReport.addWidget(self.YarnFault)
        
#======================================Machine Fault===========================================

        self.MachineFault_1 = QtWidgets.QWidget()
        self.MachineFault_1.setObjectName("MachineFault_1")
        self.Ma1Label = QtWidgets.QLabel(self.MachineFault_1)
        self.Ma1Label.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.Ma1Label.setStyleSheet("border-image: url(:/newPrefix/Capture 10.JPG);")
        self.Ma1Label.setObjectName("Ma1Label")
        self.LMButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.LMButton.setGeometry(QtCore.QRect(760, 180, 251, 61))
        self.LMButton.setMinimumSize(QtCore.QSize(0, 0))
        self.LMButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.LMButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LMButton.setFont(font)
        self.LMButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.LMButton.setIconSize(QtCore.QSize(30, 30))
        self.LMButton.setObjectName("LMButton")
        self.LWPButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.LWPButton.setGeometry(QtCore.QRect(760, 260, 251, 61))
        self.LWPButton.setMinimumSize(QtCore.QSize(0, 0))
        self.LWPButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.LWPButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LWPButton.setFont(font)
        self.LWPButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.LWPButton.setIconSize(QtCore.QSize(30, 30))
        self.LWPButton.setObjectName("LWPButton")
        self.SMButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.SMButton_value.setGeometry(QtCore.QRect(970, 90, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SMButton_value.setFont(font)
        self.SMButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SMButton_value.setObjectName("SMButton_value")
        self.SMButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.SMButton.setGeometry(QtCore.QRect(760, 100, 251, 61))
        self.SMButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SMButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SMButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SMButton.setFont(font)
        self.SMButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.SMButton.setIconSize(QtCore.QSize(30, 30))
        self.SMButton.setObjectName("SMButton")
        self.HButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.HButton_value.setGeometry(QtCore.QRect(670, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.HButton_value.setFont(font)
        self.HButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.HButton_value.setObjectName("HButton_value")
        self.HButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.HButton.setGeometry(QtCore.QRect(460, 340, 251, 61))
        self.HButton.setMinimumSize(QtCore.QSize(0, 0))
        self.HButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.HButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.HButton.setFont(font)
        self.HButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.HButton.setIconSize(QtCore.QSize(30, 30))
        self.HButton.setObjectName("HButton")
        self.OWPButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.OWPButton.setGeometry(QtCore.QRect(460, 100, 251, 61))
        self.OWPButton.setMinimumSize(QtCore.QSize(0, 0))
        self.OWPButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.OWPButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.OWPButton.setFont(font)
        self.OWPButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.OWPButton.setIconSize(QtCore.QSize(30, 30))
        self.OWPButton.setObjectName("OWPButton")
        self.LWPButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.LWPButton_value.setGeometry(QtCore.QRect(970, 250, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LWPButton_value.setFont(font)
        self.LWPButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.LWPButton_value.setObjectName("LWPButton_value")
        self.Undo_Machine_1 = QtWidgets.QPushButton(self.MachineFault_1)
        self.Undo_Machine_1.setGeometry(QtCore.QRect(460, 20, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_Machine_1.setFont(font)
        self.Undo_Machine_1.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Undo_Machine_1.setObjectName("Undo_Machine_1")
        self.MBButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.MBButton.setGeometry(QtCore.QRect(760, 340, 251, 61))
        self.MBButton.setMinimumSize(QtCore.QSize(0, 0))
        self.MBButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.MBButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MBButton.setFont(font)
        self.MBButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.MBButton.setIconSize(QtCore.QSize(30, 30))
        self.MBButton.setObjectName("MBButton")
        self.EHButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.EHButton.setGeometry(QtCore.QRect(460, 180, 251, 61))
        self.EHButton.setMinimumSize(QtCore.QSize(0, 0))
        self.EHButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.EHButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EHButton.setFont(font)
        self.EHButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.EHButton.setIconSize(QtCore.QSize(30, 30))
        self.EHButton.setObjectName("EHButton")
        self.TMButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.TMButton_value.setGeometry(QtCore.QRect(970, 410, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TMButton_value.setFont(font)
        self.TMButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.TMButton_value.setObjectName("TMButton_value")
        self.MBButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.MBButton_value.setGeometry(QtCore.QRect(970, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MBButton_value.setFont(font)
        self.MBButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.MBButton_value.setObjectName("MBButton_value")
        self.NextButton_1 = QtWidgets.QPushButton(self.MachineFault_1)
        self.NextButton_1.setGeometry(QtCore.QRect(760, 500, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.NextButton_1.setFont(font)
        self.NextButton_1.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.NextButton_1.setObjectName("NextButton_1")
        self.RMButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.RMButton_value.setGeometry(QtCore.QRect(670, 250, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RMButton_value.setFont(font)
        self.RMButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.RMButton_value.setObjectName("RMButton_value")
        self.RMButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.RMButton.setGeometry(QtCore.QRect(460, 260, 251, 61))
        self.RMButton.setMinimumSize(QtCore.QSize(0, 0))
        self.RMButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.RMButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RMButton.setFont(font)
        self.RMButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.RMButton.setIconSize(QtCore.QSize(30, 30))
        self.RMButton.setObjectName("RMButton")
        self.TMButton = QtWidgets.QPushButton(self.MachineFault_1)
        self.TMButton.setGeometry(QtCore.QRect(460, 420, 551, 61))
        self.TMButton.setMinimumSize(QtCore.QSize(0, 0))
        self.TMButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.TMButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TMButton.setFont(font)
        self.TMButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.TMButton.setIconSize(QtCore.QSize(30, 30))
        self.TMButton.setObjectName("TMButton")
        self.LMButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.LMButton_value.setGeometry(QtCore.QRect(970, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LMButton_value.setFont(font)
        self.LMButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.LMButton_value.setObjectName("LMButton_value")
        self.EHButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.EHButton_value.setGeometry(QtCore.QRect(670, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EHButton_value.setFont(font)
        self.EHButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.EHButton_value.setObjectName("EHButton_value")
        self.backButtonMa_1 = QtWidgets.QPushButton(self.MachineFault_1)
        self.backButtonMa_1.setGeometry(QtCore.QRect(460, 500, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backButtonMa_1.setFont(font)
        self.backButtonMa_1.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.backButtonMa_1.setObjectName("backButtonMa_1")
        self.OWPButton_value = QtWidgets.QLabel(self.MachineFault_1)
        self.OWPButton_value.setGeometry(QtCore.QRect(670, 90, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.OWPButton_value.setFont(font)
        self.OWPButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.OWPButton_value.setObjectName("OWPButton_value")
        self.UndoMac1Frame = QtWidgets.QFrame(self.MachineFault_1)
        self.UndoMac1Frame.setGeometry(QtCore.QRect(470, 40, 31, 21))
        self.UndoMac1Frame.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.UndoMac1Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UndoMac1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UndoMac1Frame.setObjectName("UndoMac1Frame")
        self.SavMa1frame = QtWidgets.QFrame(self.MachineFault_1)
        self.SavMa1frame.setGeometry(QtCore.QRect(490, 520, 41, 41))
        self.SavMa1frame.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.SavMa1frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SavMa1frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SavMa1frame.setObjectName("SavMa1frame")
        self.Ma1Label.raise_()
        self.LMButton.raise_()
        self.LWPButton.raise_()
        self.SMButton.raise_()
        self.HButton.raise_()
        self.OWPButton.raise_()
        self.LWPButton_value.raise_()
        self.Undo_Machine_1.raise_()
        self.MBButton.raise_()
        self.EHButton.raise_()
        self.MBButton_value.raise_()
        self.NextButton_1.raise_()
        self.RMButton.raise_()
        self.TMButton.raise_()
        self.LMButton_value.raise_()
        self.EHButton_value.raise_()
        self.backButtonMa_1.raise_()
        self.OWPButton_value.raise_()
        self.SMButton_value.raise_()
        self.RMButton_value.raise_()
        self.HButton_value.raise_()
        self.TMButton_value.raise_()
        self.UndoMac1Frame.raise_()
        self.SavMa1frame.raise_()
        FabricReport.addWidget(self.MachineFault_1)
        self.MachineFault_2 = QtWidgets.QWidget()
        self.MachineFault_2.setObjectName("MachineFault_2")
        self.Ma2Label = QtWidgets.QLabel(self.MachineFault_2)
        self.Ma2Label.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.Ma2Label.setStyleSheet("border-image: url(:/newPrefix/Capture 11.JPG);")
        self.Ma2Label.setObjectName("Ma2Label")
        self.SEFButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.SEFButton.setGeometry(QtCore.QRect(460, 420, 561, 61))
        self.SEFButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SEFButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.SEFButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SEFButton.setFont(font)
        self.SEFButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.SEFButton.setIconSize(QtCore.QSize(30, 30))
        self.SEFButton.setObjectName("SEFButton")
        self.SEFButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.SEFButton_value.setGeometry(QtCore.QRect(980, 410, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SEFButton_value.setFont(font)
        self.SEFButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.SEFButton_value.setObjectName("SEFButton_value")
        self.Nextbutton_2 = QtWidgets.QPushButton(self.MachineFault_2)
        self.Nextbutton_2.setGeometry(QtCore.QRect(770, 500, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Nextbutton_2.setFont(font)
        self.Nextbutton_2.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Nextbutton_2.setObjectName("Nextbutton_2")
        self.TLButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.TLButton_value.setGeometry(QtCore.QRect(670, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TLButton_value.setFont(font)
        self.TLButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.TLButton_value.setObjectName("TLButton_value")
        self.LOButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.LOButton_value.setGeometry(QtCore.QRect(980, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LOButton_value.setFont(font)
        self.LOButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.LOButton_value.setObjectName("LOButton_value")
        self.DEButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.DEButton_value.setGeometry(QtCore.QRect(980, 250, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DEButton_value.setFont(font)
        self.DEButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.DEButton_value.setObjectName("DEButton_value")
        self.backButtonMa_2 = QtWidgets.QPushButton(self.MachineFault_2)
        self.backButtonMa_2.setGeometry(QtCore.QRect(460, 500, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backButtonMa_2.setFont(font)
        self.backButtonMa_2.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.backButtonMa_2.setObjectName("backButtonMa_2")
        self.LOButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.LOButton.setGeometry(QtCore.QRect(770, 180, 251, 61))
        self.LOButton.setMinimumSize(QtCore.QSize(0, 0))
        self.LOButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.LOButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LOButton.setFont(font)
        self.LOButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.LOButton.setIconSize(QtCore.QSize(30, 30))
        self.LOButton.setObjectName("LOButton")
        self.DEButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.DEButton.setGeometry(QtCore.QRect(770, 260, 251, 61))
        self.DEButton.setMinimumSize(QtCore.QSize(0, 0))
        self.DEButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.DEButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DEButton.setFont(font)
        self.DEButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.DEButton.setIconSize(QtCore.QSize(30, 30))
        self.DEButton.setObjectName("DEButton")
        self.BPButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.BPButton.setGeometry(QtCore.QRect(770, 100, 251, 61))
        self.BPButton.setMinimumSize(QtCore.QSize(0, 0))
        self.BPButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.BPButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BPButton.setFont(font)
        self.BPButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.BPButton.setIconSize(QtCore.QSize(30, 30))
        self.BPButton.setObjectName("BPButton")
        self.Undo_Machine_2 = QtWidgets.QPushButton(self.MachineFault_2)
        self.Undo_Machine_2.setGeometry(QtCore.QRect(460, 20, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_Machine_2.setFont(font)
        self.Undo_Machine_2.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Undo_Machine_2.setObjectName("Undo_Machine_2")
        self.TERButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.TERButton.setGeometry(QtCore.QRect(460, 260, 251, 61))
        self.TERButton.setMinimumSize(QtCore.QSize(0, 0))
        self.TERButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.TERButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TERButton.setFont(font)
        self.TERButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.TERButton.setIconSize(QtCore.QSize(30, 30))
        self.TERButton.setObjectName("TERButton")
        self.FLButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.FLButton_value.setGeometry(QtCore.QRect(670, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.FLButton_value.setFont(font)
        self.FLButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.FLButton_value.setObjectName("FLButton_value")
        self.BPButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.BPButton_value.setGeometry(QtCore.QRect(980, 90, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BPButton_value.setFont(font)
        self.BPButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.BPButton_value.setObjectName("BPButton_value")
        self.FLButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.FLButton.setGeometry(QtCore.QRect(460, 180, 251, 61))
        self.FLButton.setMinimumSize(QtCore.QSize(0, 0))
        self.FLButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.FLButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.FLButton.setFont(font)
        self.FLButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.FLButton.setIconSize(QtCore.QSize(30, 30))
        self.FLButton.setObjectName("FLButton")
        self.TERButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.TERButton_value.setGeometry(QtCore.QRect(670, 260, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TERButton_value.setFont(font)
        self.TERButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.TERButton_value.setObjectName("TERButton_value")
        self.MEButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.MEButton.setGeometry(QtCore.QRect(770, 340, 251, 61))
        self.MEButton.setMinimumSize(QtCore.QSize(0, 0))
        self.MEButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.MEButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MEButton.setFont(font)
        self.MEButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.MEButton.setIconSize(QtCore.QSize(30, 30))
        self.MEButton.setObjectName("MEButton")
        self.TLButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.TLButton.setGeometry(QtCore.QRect(460, 340, 251, 61))
        self.TLButton.setMinimumSize(QtCore.QSize(0, 0))
        self.TLButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.TLButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TLButton.setFont(font)
        self.TLButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.TLButton.setIconSize(QtCore.QSize(30, 30))
        self.TLButton.setObjectName("TLButton")
        self.CRButton = QtWidgets.QPushButton(self.MachineFault_2)
        self.CRButton.setGeometry(QtCore.QRect(460, 100, 251, 61))
        self.CRButton.setMinimumSize(QtCore.QSize(0, 0))
        self.CRButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.CRButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CRButton.setFont(font)
        self.CRButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.CRButton.setIconSize(QtCore.QSize(30, 30))
        self.CRButton.setObjectName("CRButton")
        self.CRButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.CRButton_value.setGeometry(QtCore.QRect(670, 90, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CRButton_value.setFont(font)
        self.CRButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.CRButton_value.setObjectName("CRButton_value")
        self.MEButton_value = QtWidgets.QLabel(self.MachineFault_2)
        self.MEButton_value.setGeometry(QtCore.QRect(980, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MEButton_value.setFont(font)
        self.MEButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.MEButton_value.setObjectName("MEButton_value")
        self.UndoMac2Frame = QtWidgets.QFrame(self.MachineFault_2)
        self.UndoMac2Frame.setGeometry(QtCore.QRect(470, 40, 31, 21))
        self.UndoMac2Frame.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.UndoMac2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UndoMac2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UndoMac2Frame.setObjectName("UndoMac2Frame")
        self.SavMa2frame = QtWidgets.QFrame(self.MachineFault_2)
        self.SavMa2frame.setGeometry(QtCore.QRect(490, 520, 41, 41))
        self.SavMa2frame.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.SavMa2frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SavMa2frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SavMa2frame.setObjectName("SavMa2frame")
        self.Ma2Label.raise_()
        self.SEFButton.raise_()
        self.SEFButton_value.raise_()
        self.Nextbutton_2.raise_()
        self.backButtonMa_2.raise_()
        self.LOButton.raise_()
        self.DEButton.raise_()
        self.BPButton.raise_()
        self.Undo_Machine_2.raise_()
        self.TERButton.raise_()
        self.BPButton_value.raise_()
        self.FLButton.raise_()
        self.TERButton_value.raise_()
        self.MEButton.raise_()
        self.TLButton.raise_()
        self.CRButton.raise_()
        self.CRButton_value.raise_()
        self.MEButton_value.raise_()
        self.FLButton_value.raise_()
        self.LOButton_value.raise_()
        self.DEButton_value.raise_()
        self.TLButton_value.raise_()
        self.UndoMac2Frame.raise_()
        self.SavMa2frame.raise_()
        FabricReport.addWidget(self.MachineFault_2)
        self.MachineFault_3 = QtWidgets.QWidget()
        self.MachineFault_3.setObjectName("MachineFault_3")
        self.Ma3Label = QtWidgets.QLabel(self.MachineFault_3)
        self.Ma3Label.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        self.Ma3Label.setStyleSheet("border-image: url(:/newPrefix/Capture 9.JPG);")
        self.Ma3Label.setObjectName("Ma3Label")
        self.DPButton = QtWidgets.QPushButton(self.MachineFault_3)
        self.DPButton.setGeometry(QtCore.QRect(780, 160, 251, 61))
        self.DPButton.setMinimumSize(QtCore.QSize(0, 0))
        self.DPButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.DPButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DPButton.setFont(font)
        self.DPButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.DPButton.setIconSize(QtCore.QSize(30, 30))
        self.DPButton.setObjectName("DPButton")
        self.DMButton = QtWidgets.QPushButton(self.MachineFault_3)
        self.DMButton.setGeometry(QtCore.QRect(470, 160, 251, 61))
        self.DMButton.setMinimumSize(QtCore.QSize(0, 0))
        self.DMButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.DMButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DMButton.setFont(font)
        self.DMButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.DMButton.setIconSize(QtCore.QSize(30, 30))
        self.DMButton.setObjectName("DMButton")
        self.BTNButton_value = QtWidgets.QLabel(self.MachineFault_3)
        self.BTNButton_value.setGeometry(QtCore.QRect(990, 310, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BTNButton_value.setFont(font)
        self.BTNButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.BTNButton_value.setObjectName("BTNButton_value")
        self.BSButton_value = QtWidgets.QLabel(self.MachineFault_3)
        self.BSButton_value.setGeometry(QtCore.QRect(990, 230, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BSButton_value.setFont(font)
        self.BSButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.BSButton_value.setObjectName("BSButton_value")
        self.TPButton_value = QtWidgets.QLabel(self.MachineFault_3)
        self.TPButton_value.setGeometry(QtCore.QRect(680, 310, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TPButton_value.setFont(font)
        self.TPButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.TPButton_value.setObjectName("TPButton_value")
        self.DMButton_value = QtWidgets.QLabel(self.MachineFault_3)
        self.DMButton_value.setGeometry(QtCore.QRect(680, 150, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DMButton_value.setFont(font)
        self.DMButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.DMButton_value.setObjectName("DMButton_value")
        self.BTNButton = QtWidgets.QPushButton(self.MachineFault_3)
        self.BTNButton.setGeometry(QtCore.QRect(780, 320, 251, 61))
        self.BTNButton.setMinimumSize(QtCore.QSize(0, 0))
        self.BTNButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.BTNButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BTNButton.setFont(font)
        self.BTNButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.BTNButton.setIconSize(QtCore.QSize(30, 30))
        self.BTNButton.setObjectName("BTNButton")
        self.OWftButton = QtWidgets.QPushButton(self.MachineFault_3)
        self.OWftButton.setGeometry(QtCore.QRect(470, 400, 561, 61))
        self.OWftButton.setMinimumSize(QtCore.QSize(0, 0))
        self.OWftButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.OWftButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.OWftButton.setFont(font)
        self.OWftButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.OWftButton.setIconSize(QtCore.QSize(30, 30))
        self.OWftButton.setObjectName("OWftButton")
        self.OWftButton_value = QtWidgets.QLabel(self.MachineFault_3)
        self.OWftButton_value.setGeometry(QtCore.QRect(990, 390, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.OWftButton_value.setFont(font)
        self.OWftButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.OWftButton_value.setObjectName("OWftButton_value")
        self.backButtonMa_3 = QtWidgets.QPushButton(self.MachineFault_3)
        self.backButtonMa_3.setGeometry(QtCore.QRect(590, 500, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backButtonMa_3.setFont(font)
        self.backButtonMa_3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.backButtonMa_3.setObjectName("backButtonMa_3")
        self.Undo_Machine_3 = QtWidgets.QPushButton(self.MachineFault_3)
        self.Undo_Machine_3.setGeometry(QtCore.QRect(470, 50, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_Machine_3.setFont(font)
        self.Undo_Machine_3.setStyleSheet("background-color: rgb(212, 199, 255);")
        self.Undo_Machine_3.setObjectName("Undo_Machine_3")
        self.BSButton = QtWidgets.QPushButton(self.MachineFault_3)
        self.BSButton.setGeometry(QtCore.QRect(780, 240, 251, 61))
        self.BSButton.setMinimumSize(QtCore.QSize(0, 0))
        self.BSButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.BSButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BSButton.setFont(font)
        self.BSButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.BSButton.setIconSize(QtCore.QSize(30, 30))
        self.BSButton.setObjectName("BSButton")
        self.DPButton_value = QtWidgets.QLabel(self.MachineFault_3)
        self.DPButton_value.setGeometry(QtCore.QRect(990, 150, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DPButton_value.setFont(font)
        self.DPButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.DPButton_value.setObjectName("DPButton_value")
        self.TCButton_value = QtWidgets.QLabel(self.MachineFault_3)
        self.TCButton_value.setGeometry(QtCore.QRect(680, 230, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TCButton_value.setFont(font)
        self.TCButton_value.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.TCButton_value.setObjectName("TCButton_value")
        self.TCButton = QtWidgets.QPushButton(self.MachineFault_3)
        self.TCButton.setGeometry(QtCore.QRect(470, 240, 251, 61))
        self.TCButton.setMinimumSize(QtCore.QSize(0, 0))
        self.TCButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.TCButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TCButton.setFont(font)
        self.TCButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.TCButton.setIconSize(QtCore.QSize(30, 30))
        self.TCButton.setObjectName("TCButton")
        self.TPButton = QtWidgets.QPushButton(self.MachineFault_3)
        self.TPButton.setGeometry(QtCore.QRect(470, 320, 251, 61))
        self.TPButton.setMinimumSize(QtCore.QSize(0, 0))
        self.TPButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.TPButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TPButton.setFont(font)
        self.TPButton.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(243, 243, 243);")
        self.TPButton.setIconSize(QtCore.QSize(30, 30))
        self.TPButton.setObjectName("TPButton")
        
        #Counts 
        self.EHButton_value_count = 0
        self.HButton_value_count = 0
        self.LMButton_value_count = 0
        self.LWPButton_value_count = 0
        self.MBButton_value_count = 0
        self.OWPButton_value_count = 0
        self.RMButton_value_count = 0
        self.SMButton_value_count = 0            
        self.TMButton_value_count = 0        
        
        self.BPButton_value_count = 0
        self.CRButton_value_count = 0
        self.DEButton_value_count = 0
        self.FLButton_value_count = 0
        self.LOButton_value_count = 0
        self.MEButton_value_count = 0
        self.SEFButton_value_count = 0
        self.TERButton_value_count = 0              
        self.TLButton_value_count = 0  
        
        
        self.BSButton_value_count = 0
        self.BTNButton_value_count = 0
        self.DMButton_value_count = 0
        self.DPButton_value_count = 0
        self.OWftButton_value_count = 0
        self.TCButton_value_count = 0
        self.TPButton_value_count = 0        
        
        #Center alignment
        self.EHButton_value.setAlignment(Qt.AlignCenter)
        self.HButton_value.setAlignment(Qt.AlignCenter)
        self.LMButton_value.setAlignment(Qt.AlignCenter)
        self.LWPButton_value.setAlignment(Qt.AlignCenter)
        self.MBButton_value.setAlignment(Qt.AlignCenter)
        self.OWPButton_value.setAlignment(Qt.AlignCenter)
        self.RMButton_value.setAlignment(Qt.AlignCenter)
        self.SMButton_value.setAlignment(Qt.AlignCenter)
        self.TMButton_value.setAlignment(Qt.AlignCenter) 
        
        self.BPButton_value.setAlignment(Qt.AlignCenter)
        self.CRButton_value.setAlignment(Qt.AlignCenter)
        self.DEButton_value.setAlignment(Qt.AlignCenter)
        self.FLButton_value.setAlignment(Qt.AlignCenter)
        self.LOButton_value.setAlignment(Qt.AlignCenter)
        self.MEButton_value.setAlignment(Qt.AlignCenter)
        self.SEFButton_value.setAlignment(Qt.AlignCenter)
        self.TERButton_value.setAlignment(Qt.AlignCenter)
        self.TLButton_value.setAlignment(Qt.AlignCenter)   
        
        self.BSButton_value.setAlignment(Qt.AlignCenter)
        self.BTNButton_value.setAlignment(Qt.AlignCenter)
        self.DMButton_value.setAlignment(Qt.AlignCenter)
        self.DPButton_value.setAlignment(Qt.AlignCenter)
        self.OWftButton_value.setAlignment(Qt.AlignCenter)
        self.TCButton_value.setAlignment(Qt.AlignCenter)
        self.TPButton_value.setAlignment(Qt.AlignCenter)        
        
        self.UndoMac3Frame = QtWidgets.QFrame(self.MachineFault_3)
        self.UndoMac3Frame.setGeometry(QtCore.QRect(480, 70, 31, 21))
        self.UndoMac3Frame.setStyleSheet("border-image: url(:/newPrefix/Undo-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.UndoMac3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UndoMac3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UndoMac3Frame.setObjectName("UndoMac3Frame")
        self.SavMa3frame = QtWidgets.QFrame(self.MachineFault_3)
        self.SavMa3frame.setGeometry(QtCore.QRect(630, 510, 41, 41))
        self.SavMa3frame.setStyleSheet("border-image: url(:/newPrefix/Save-icon.png);\n"
"background-color: rgb(238, 238, 236);\n"
"\n"
"\n"
"")
        self.SavMa3frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SavMa3frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SavMa3frame.setObjectName("SavMa3frame")
        self.Ma3Label.raise_()
        self.DPButton.raise_()
        self.DMButton.raise_()
        self.DMButton_value.raise_()
        self.BTNButton.raise_()
        self.OWftButton.raise_()
        self.OWftButton_value.raise_()
        self.backButtonMa_3.raise_()
        self.Undo_Machine_3.raise_()
        self.BSButton.raise_()
        self.DPButton_value.raise_()
        self.TCButton.raise_()
        self.TPButton.raise_()
        self.TCButton_value.raise_()
        self.BSButton_value.raise_()
        self.BTNButton_value.raise_()
        self.TPButton_value.raise_()
        self.UndoMac3Frame.raise_()
        self.SavMa3frame.raise_()
        FabricReport.addWidget(self.MachineFault_3)
        
# ======================================================Connecting Button click =====================================================================================================
    

    #in mainpage
        self.SaveProceedButton.clicked.connect(partial(self.post1,"OnSaveAndProceed"))
        #self.SaveProceedButton.clicked.connect(partial(self.fault_select,"Selection"))
        self.ContinueButton.clicked.connect(partial(self.post1,"OnContinue"))
        
        
    #in Faultselection
        
        #self.UIDlabel.setText("UID is")
        
        self.SizeButton.clicked.connect(partial(self.fault_select,"Sizing"))
        self.DyedButton.clicked.connect(partial(self.fault_select,"DyeYarn"))
        self.WeaversButton.clicked.connect(partial(self.fault_select,"Weavers"))
        self.YarnButton.clicked.connect(partial(self.fault_select,"Yarn"))
        self.MachineButton.clicked.connect(partial(self.fault_select,"Machine1"))
        
        self.ExitButton.clicked.connect(partial(self.post1,"OnExitButton"))
        self.ExitButton.clicked.connect(partial(self.fault_select,"Exit"))
    
    
    # in Size fault
        self.backButtonSi.clicked.connect(partial(self.post1,"OnBackButton"))
        self.backButtonSi.clicked.connect(partial(self.back_button,"Sizing"))
        self.Undo_SizeButton.clicked.connect(self.undo_list)
    
        self.SOSButton.clicked.connect(partial(self.write_to_list,"SOSButton"))
        self.SSButton.clicked.connect(partial(self.write_to_list,"SSButton"))
        self.SVButton.clicked.connect(partial(self.write_to_list,"SVButton"))
        self.SPButton.clicked.connect(partial(self.write_to_list,"SPButton"))
        
    #in dyedyarn
        self.backButtonDy.clicked.connect(partial(self.post1,"OnBackButton"))
        self.backButtonDy.clicked.connect(partial(self.back_button,"DyedYarn"))
        self.Undo_DyeButton.clicked.connect(self.undo_list)
    
        self.COVButton.clicked.connect(partial(self.write_to_list,"COVButton"))
        self.STButton.clicked.connect(partial(self.write_to_list,"STButton"))  
        
    #in Weavers
        self.backButtonWe.clicked.connect(partial(self.post1,"OnBackButton"))
        self.backButtonWe.clicked.connect(partial(self.back_button,"Weave"))
        self.Undo_WeaveButton.clicked.connect(self.undo_list)
        
        self.DOPButton.clicked.connect(partial(self.write_to_list,"DOPButton"))
        self.HSButton.clicked.connect(partial(self.write_to_list,"HSButton"))
        self.WDRButton.clicked.connect(partial(self.write_to_list,"WDRButton"))
        self.WWftButton.clicked.connect(partial(self.write_to_list,"WWftButton"))
        self.WDTButton.clicked.connect(partial(self.write_to_list,"WDTButton"))
        self.SWButton.clicked.connect(partial(self.write_to_list,"SWButton"))
                
        
        
    #in Yarn
        self.backButtonYa.clicked.connect(partial(self.post1,"OnBackButton"))
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
        
    #in Machine
        self.backButtonMa_1.clicked.connect(partial(self.post1,"OnBackButton"))
        self.backButtonMa_2.clicked.connect(partial(self.post1,"OnBackButton"))
        self.backButtonMa_3.clicked.connect(partial(self.post1,"OnBackButton"))
        
        self.NextButton_1.clicked.connect(partial(self.post1,"OnBackButton"))
        self.Nextbutton_2.clicked.connect(partial(self.post1,"OnBackButton"))
        
        self.backButtonMa_1.clicked.connect(partial(self.back_button,"Machine"))
        self.backButtonMa_2.clicked.connect(partial(self.back_button,"Machine"))
        self.backButtonMa_3.clicked.connect(partial(self.back_button,"Machine"))
        
        self.NextButton_1.clicked.connect(partial(self.back_button,"Machine"))
        self.Nextbutton_2.clicked.connect(partial(self.back_button,"Machine"))        
        
        self.NextButton_1.clicked.connect(partial(self.fault_select,"Machine2"))
        self.Nextbutton_2.clicked.connect(partial(self.fault_select,"Machine3"))
        
        self.Undo_Machine_1.clicked.connect(self.undo_list)
        self.Undo_Machine_2.clicked.connect(self.undo_list)
        self.Undo_Machine_3.clicked.connect(self.undo_list)
        
        self.EHButton.clicked.connect(partial(self.write_to_list,"EHButton"))
        self.HButton.clicked.connect(partial(self.write_to_list,"HButton"))
        self.LMButton.clicked.connect(partial(self.write_to_list,"LMButton"))
        self.LWPButton.clicked.connect(partial(self.write_to_list,"LWPButton"))
        self.MBButton.clicked.connect(partial(self.write_to_list,"MBButton"))
        
        self.OWPButton.clicked.connect(partial(self.write_to_list,"OWPButton"))
        self.RMButton.clicked.connect(partial(self.write_to_list,"RMButton"))
        self.SMButton.clicked.connect(partial(self.write_to_list,"SMButton"))
        self.TMButton.clicked.connect(partial(self.write_to_list,"TMButton"))
        
        self.BPButton.clicked.connect(partial(self.write_to_list,"BPButton"))
        
        self.CRButton.clicked.connect(partial(self.write_to_list,"CRButton"))
        self.DEButton.clicked.connect(partial(self.write_to_list,"DEButton"))
        self.FLButton.clicked.connect(partial(self.write_to_list,"FLButton"))
        self.LOButton.clicked.connect(partial(self.write_to_list,"LOButton"))
        self.MEButton.clicked.connect(partial(self.write_to_list,"MEButton"))
        
        self.SEFButton.clicked.connect(partial(self.write_to_list,"SEFButton"))
        self.TERButton.clicked.connect(partial(self.write_to_list,"TERButton"))
        self.TLButton.clicked.connect(partial(self.write_to_list,"TLButton"))
        
        self.BSButton.clicked.connect(partial(self.write_to_list,"BSButton"))
        self.BTNButton.clicked.connect(partial(self.write_to_list,"BTNButton"))
        
        self.DMButton.clicked.connect(partial(self.write_to_list,"DMButton"))
        self.DPButton.clicked.connect(partial(self.write_to_list,"DPButton"))
        self.OWftButton.clicked.connect(partial(self.write_to_list,"OWftButton"))
        self.TCButton.clicked.connect(partial(self.write_to_list,"TCButton"))
        self.TPButton.clicked.connect(partial(self.write_to_list,"TPButton"))
        
               
        
        

        self.retranslateUi(FabricReport)
        FabricReport.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FabricReport)

    def retranslateUi(self, FabricReport):
        _translate = QtCore.QCoreApplication.translate
        FabricReport.setWindowTitle(_translate("FabricReport", "FabricReport"))
        self.mainpagelabel.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.ActEPI.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Actual EPI</span></p></body></html>"))
        self.SaveProceedButton.setText(_translate("FabricReport", "Save and  Proceed"))
        self.MTRSC.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\">Sound MTRSC</p></body></html>"))
        self.Loom.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Loom No.</span></p></body></html>"))
        self.DoffedShift.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Doffed Dt/Shift</span></p></body></html>"))
        self.set.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Set No.</span></p></body></html>"))
        self.descr.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Description</span></p></body></html>"))
        self.actualwidth.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Actual Width</span></p></body></html>"))
        self.Beamno.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Beam No.</span></p></body></html>"))
        self.warpcount.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Warp Count</span></p></body></html>"))
        self.MTRS.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\">DOFE MTRS</p></body></html>"))
        self.actPPI.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Actual PPI</span></p></body></html>"))
        self.Date.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Date</span></p></body></html>"))
        self.time.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\">Time</p></body></html>"))
        self.piece.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Piece No.</span></p></body></html>"))
        self.title.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#f3f3f3;\">Fabric Examination Report</span></p></body></html>"))
        self.weave.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Weave</span></p></body></html>"))
        self.weftcount.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Weft Count</span></p></body></html>"))
        self.ContinueButton.setText(_translate("FabricReport", "Continue with UID"))
        self.UID.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\">Unique ID</p></body></html>"))
        self.weftcount.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Weft Count</span></p></body></html>"))
        self.Faultlabel.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.DyedButton.setText(_translate("FabricReport", "DyedYarn\n"
"Fault"))
        self.Meter.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:16pt; font-weight:600; color:#ffffff;\">Meter Reading</span></p></body></html>"))
        
        #self.UIDlabel.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:16pt; font-weight:600; color:#ffffff;\">UID is</span></p></body></html>"))
        
        
        self.YarnButton.setText(_translate("FabricReport", "Yarn\n"
"Fault"))
        self.ExitButton.setText(_translate("FabricReport", "Exit"))
        self.MachineButton.setText(_translate("FabricReport", "Machine\n"
"Fault"))
        self.WeaversButton.setText(_translate("FabricReport", "Weavers\n"
"Fault"))
        self.SizeButton.setText(_translate("FabricReport", "Sizing\n"
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
        self.SizLabel.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.backButtonDy.setText(_translate("FabricReport", "Back"))
        self.COVButton.setText(_translate("FabricReport", "C O V - Color Variation"))
        self.STButton.setText(_translate("FabricReport", "S T - Streaks"))
        self.COVButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.STButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Undo_DyeButton.setText(_translate("FabricReport", "Undo"))
        self.backButtonWe.setText(_translate("FabricReport", "Back"))
        self.WeavLabel.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
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
        self.YarnLabel.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
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
        self.Ma1Label.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.LMButton.setText(_translate("FabricReport", "L M - Loose Weft"))
        self.LWPButton.setText(_translate("FabricReport", "L W P - Loose Warp"))
        self.SMButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SMButton.setText(_translate("FabricReport", "S M - Starting Mark"))
        self.HButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.HButton.setText(_translate("FabricReport", "H - Holes"))
        self.OWPButton.setText(_translate("FabricReport", "O W P - Oily Warp"))
        self.LWPButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Undo_Machine_1.setText(_translate("FabricReport", "Undo"))
        self.MBButton.setText(_translate("FabricReport", "M B - Multiple Break"))
        self.EHButton.setText(_translate("FabricReport", "E H - Emert Hole"))
        self.TMButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.MBButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.NextButton_1.setText(_translate("FabricReport", "Next"))
        self.RMButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.RMButton.setText(_translate("FabricReport", "R M - Reed Mark"))
        self.TMButton.setText(_translate("FabricReport", "SV/TM - Temple Mark"))
        self.LMButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.EHButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.backButtonMa_1.setText(_translate("FabricReport", "Back"))
        self.OWPButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Ma2Label.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.SEFButton.setText(_translate("FabricReport", "S E F - Single End Float"))
        self.SEFButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Nextbutton_2.setText(_translate("FabricReport", "Next"))
        self.TLButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.LOButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.DEButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.backButtonMa_2.setText(_translate("FabricReport", "Back"))
        self.LOButton.setText(_translate("FabricReport", "L O - Left Off"))
        self.DEButton.setText(_translate("FabricReport", "D E- Double End"))
        self.BPButton.setText(_translate("FabricReport", "B P - Brocken Pick"))
        self.Undo_Machine_2.setText(_translate("FabricReport", "Undo"))
        self.TERButton.setText(_translate("FabricReport", "T E R - Tear"))
        self.FLButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.BPButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.FLButton.setText(_translate("FabricReport", "F L - Float"))
        self.TERButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.MEButton.setText(_translate("FabricReport", "M E - Missing End"))
        self.TLButton.setText(_translate("FabricReport", "T L - Tails"))
        self.CRButton.setText(_translate("FabricReport", "C R - Crake"))
        self.CRButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.MEButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Ma3Label.setText(_translate("FabricReport", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.DPButton.setText(_translate("FabricReport", "D P - Drop Pick"))
        self.DMButton.setText(_translate("FabricReport", "D M - Doppy Mistake"))
        self.BTNButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.BSButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TPButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.DMButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.BTNButton.setText(_translate("FabricReport", "B T N- Bad Tuck In"))
        self.OWftButton.setText(_translate("FabricReport", "O Wft - Oily Weft"))
        self.OWftButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.backButtonMa_3.setText(_translate("FabricReport", "Back"))
        self.Undo_Machine_3.setText(_translate("FabricReport", "Undo"))
        self.BSButton.setText(_translate("FabricReport", "B S - Bad Selvedge"))
        self.DPButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TCButton_value.setText(_translate("FabricReport", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TCButton.setText(_translate("FabricReport", "T C - Temple Cut"))
        self.TPButton.setText(_translate("FabricReport", "T P - Thick Plae"))
import imagetest


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FabricReport = QtWidgets.QStackedWidget()
    ui = Ui_FabricReport()
    ui.setupUi(FabricReport)
    FabricReport.show()
    sys.exit(app.exec_())
