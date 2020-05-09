# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:44:56 2020

@author: 88690
"""

class Human():
    def __init__( self , gender , ID , weight , height , name ):
        self.gender = gender
        self.ID = ID
        self.weight = weight
        self.height = height
        self.name = name
        
    def setCountry( self , country ):
        self.country = country
        
    def BMI( self ):
        return self.weight / pow(( self.height / 100 ) , 2 )
    
class Kid(Human):
    def __init__( self , gender , ID , weight , height , name , school ):
        super().__init__( gender , ID , weight , height , name )
        self.school = school
    def School(self):
        return self.school
    
Christopher = Human( "men" , "O100000001" , 40 , 156 , "Christopher" )
print(str(Christopher.name) + str (Christopher.BMI()))    

Tom = Kid( "boy" , "K100000002" , 24 , 120 , "Tom" , "Google" )
print(str(Tom.name) + str (Tom.BMI()))    
