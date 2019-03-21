# -*- coding: utf-8 -*-
 
#For example, the “1” bin has the following winning Outcomes: “1”, “Red”, “Odd”, “Low”, “Column 1”, “Dozen 1-
#12”, “Split 1-2”, “Split 1-4”, “Street 1-2-3”, “Corner 1-2-4-5”, “Five Bet”, “Line 1-2-3-4-5-6”, “00-0-1-2-3”, “Dozen
#1”, “Low” and “Column 1”. All of these bets will payoff if the wheel spins a “1”
    
#Outcome.name
#Holds the name of the Outcome. Examples include "1", "Red".
#Outcome.odds
#Holds the payout odds for this Outcome. Most odds are stated as 1:1 or 17:1, we only keep the numerator (17)
#and assume the denominator is 1.       
class Outcome:
    
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds
        
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
        
    def __ne__(self, other):
        if self.name != other.name:
            return True
        else:
            return False
        
    def winAmount(self, amount):
        return amount*self.odds
       
    def __str__(self):
        return "Name" + str(self.odds) + ":1"
    
    def __repr__(self):
        return "Outcome" + str(self.name) + ", " + str(self.odds)