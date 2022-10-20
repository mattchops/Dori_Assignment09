'''
Created on Oct 20, 2022

@author: User
'''
from DessertPackage.CupcakeClass import *
from DessertPackage.SkittlesClass import *
from DessertPackage.BrowniesClass import *

cupcake = Cupcake("vanilla", 2)
print(cupcake.__str__())

print(cupcake.flavor) 

#Negative Test
cupcake.setPrice(-3)
#Positive Test
cupcake.setPrice(3)
print(cupcake.__str__())
