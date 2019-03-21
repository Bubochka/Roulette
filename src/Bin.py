# -*- coding: utf-8 -*-
#Define a class which has an attribute that holds the collection. We’re wrapping an existing data structure in a new class.

#class Bin:
#    def __init__(self, outcomes):
#        self.outcomes= frozenset(outcomes)

#Define a class which is the collection. We’re extending an existing data structure.
class Bin(frozenset):
    pass

#Bin contains a collection of Outcomes which reflect the winning bets that are paid for a particular bin on a Roulette
#wheel. In Roulette, each spin of the wheel has a number of Outcomes. Example: A spin of 1, selects the “1” bin
#with the following winning Outcomes: “1” , “Red” , “Odd” , “Low” , “Column 1” , “Dozen 1-12” , “Split 1-2” ,
#“Split 1-4” , “Street 1-2-3” , “Corner 1-2-4-5” , “Five Bet” , “Line 1-2-3-4-5-6” , “00-0-1-2-3” , “Dozen 1” , “Low”
#and “Column 1” . These are collected into a single Bin .

#      Python Bin Construction    
#five= Outcome( "00-0-1-2-3", 6 )
#zero= Bin( [Outcome("0",35), five] )
#zerozero= Bin( [Outcome("00",35), five] )

#           Methods
#bin1 = Bin( {outcome1, outcome2, outcome3} )