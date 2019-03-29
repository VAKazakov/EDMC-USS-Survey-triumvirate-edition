import threading
import requests
import sys
import json
from emitter import Emitter
from debug import Debug
from debug import debug,error


'''
    { 
        "timestamp":"2018-10-07T13:03:02Z", 
        "event":"USSDrop", 
        "USSType":"$USS_Type_NonHuman;", 
        "USSType_Localised":"Non-Human signal source", 
        "USSThreat":4 
    }
'''

class NHSS(Emitter):

    fss= {}
    
    def __init__(self,cmdr, is_beta, system,entry,client):
        Emitter.__init__(self,cmdr, is_beta, system, None,None,None, entry, None,None,None,client)
        threading.Thread.__init__(self)
        self.system = system
        self.cmdr = cmdr
        self.is_beta = is_beta
        self.entry = entry.copy()
        self.client=client
        self.modelreport="nhssreports"

    def run(self):
        payload={}

        if self.entry["event"] == 'FSSSignalDiscovered':
            threatLevel=self.entry.get("ThreatLevel")
            type="FSS"
        else:
            threatLevel=self.entry.get("USSThreat")
            type="Drop"

        payload["systemName"]=self.system
        payload["cmdrName"]=self.cmdr  
        payload["nhssRawJson"]=self.entry
        payload["threatLevel"]=threatLevel
        payload["isbeta"]= self.is_beta
        payload["clientVersion"]= self.client
        payload["reportStatus"]="accepted"
        payload["reportComment"]=type

        url=self.getUrl()
        self.send(payload,url)



def submit(cmdr, is_beta, system, station, entry,client):
    
    #USS and FFS
    if entry["event"] in ("USSDrop",'FSSSignalDiscovered') and entry.get("USSType") == "$USS_Type_NonHuman;" : 
        
        # The have different names for teh same thing so normalise
        if entry["event"] == 'FSSSignalDiscovered':
            threatLevel=entry.get("ThreatLevel")
        else:
            threatLevel=entry.get("USSThreat")

        # see if you have system and threat levels store
        # Thsi will fail if it a new threat level in the current system
        try:
            globalfss=NHSS.fss.get(system)
            oldthreat=globalfss.get(threatLevel)
            #debug(globalfss)
        except:
            oldthreat=False

        if oldthreat:
            debug("Threat level already recorded here "+str(threatLevel))

        else:
            #debug("Threat {}".format(threatLevel))
            try:
                #set the threatlevel for the system
                NHSS.fss[system][threatLevel] =  True
            except:
                #we couldnt find teh system so lets define it
                NHSS.fss[system]={ threatLevel: True}

            NHSS(cmdr, is_beta, system,  entry,client).start()