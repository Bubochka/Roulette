# -*- coding: utf-8 -*-

class Bet:
    
    def __init__(self, amount, outcome):
        
        self.amount = amount
        self.outcome = outcome
        
    def winAmount(self):
        pass
    
    def loseAmount(self):
        pass
        
    def __str__(self):
        
        return str(self.amount) + " on " + str(self.outcome)
    
    def __repr__(self):
        
        return "Bet(" + str(self.amount) + "," + str(self.outcome) + ")"
