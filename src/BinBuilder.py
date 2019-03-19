# -*- coding: utf-8 -*-
#from src.Outcomes import Outcomes

class BinBuilder:
    
    def __init__(self):
        pass
    
    def generateStreetBets(self, wheel):      
        for binIndex in range(37):
            wheel.addOutcome(binIndex, wheel.getOutcome("Number " + str(binIndex)))
            wheel.addOutcome(37, wheel.getOutcome("Number 00"))
            
    def buildBins(self, wheel):
        BinBuilder.generateStraightBets(self, wheel)            