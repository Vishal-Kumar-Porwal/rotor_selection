import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import math as m
import numpy as np
import os
import Bio
from Bio import *
from Bio.PDB.PDBParser import PDBParser
import warnings
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)
from mpl_toolkits import mplot3d
import ast
import pylab as pl
import random
from random import randint

file_xyz = input('path of the xyz file:')

#file_xyz = str('A234.xyz')

file_connection= input('path of the file with only connection information:')

#rotors_output= input('path of the file where output of rotors will be stored:')
rotors_output= str('rotors.txt')


#file_connection= str('connection-A234.txt')

connection_dict={}
n_connection=1
with open(file_connection,'r') as something:
    
    for line in something:
        # print(line)
        line = line.split()
        
        if line!= []:
            line_1 = []
            for j in line:
                j = float(j)
                line_1.append(j)
            connection_dict[n_connection] = line_1
            n_connection=n_connection+1
            # print(structure_dict)
        else:
            break
        
structure_dict={}
n_structure=1
with open(file_xyz,'r') as something:
    
    for line in something:
        # print(line)
        line = line.split()
        if line!= []:
            structure_dict[n_structure] = line
            n_structure=n_structure+1
            # print(structure_dict)
        else:
            break

#print('structure_dict=',structure_dict)# 
#print('connection_dict=',connection_dict)

bonds_dataframe = pd.DataFrame(index=connection_dict.keys(),columns=connection_dict.keys())
#print(bonds_dataframe)

for i in connection_dict.keys():
    for j in range(len(connection_dict[i])):
        
        if j%2 == 0 and j > 0:
            bonds_dataframe.at[i,connection_dict[i][j-1]] = connection_dict[i][j]
        else:
            bonds_dataframe.at[i,connection_dict[i][j]] = 0


bonds_dataframe = bonds_dataframe.replace(np.nan,0)

#print(bonds_dataframe)        

def find_bond(dataframe,atom1):
    list_atoms=[] 
    for atom2 in dataframe.columns:
        if dataframe[atom1][atom2] >= 1:
            #print('still trying','atom1=',atom1,'atom2=',atom2)
          
            list_atoms.append(atom2)
            #return atom2
        elif dataframe[atom1][atom2] == 0:
             continue
             #print('still trying','atom1=',atom1,'atom2=',atom2)
                            
  
        else:
            continue
            #print('error: atoms indices are wrong, correctng and still trying')
    
    return list_atoms
    

    

#find_bond(bonds_dataframe,1)
         
    
hydrogen = 'H'

for i in bonds_dataframe.columns:
    for j in bonds_dataframe.columns:
        if j > i:

            if structure_dict[i][0] == hydrogen:
                continue
            elif structure_dict[j][0] == hydrogen:
                continue
            elif len(connection_dict[i]) <= 3 :
                continue
            elif len(connection_dict[j]) <= 3 :
                continue
            elif i == j:
                continue
            elif bonds_dataframe[i][j] > 1.0 :
                continue
             
            elif bonds_dataframe[i][j]!= 0:
                K = find_bond(bonds_dataframe,i) 
                L = find_bond(bonds_dataframe,j)
                k = [kk for kk in K if not kk in L and not kk in [i,j]]
                l = [ll for ll in L if not ll in K and not ll in [i,j]]
                #print(k,l) 
                #print('D',random.choice(k),i,j,random.choice(l),'S', 30, 12.0)
                something_something = str("D"+" "+str(random.choice(k))+" "+str(i)+" "+str(j)+" "+str(random.choice(l))+" "+"S"+" "+"30"+" "+"12.0")
                with open(rotors_output,'a') as f:
                    f.write(str(something_something))
                    f.write("\n")
                #find_bond(bonds_dataframe,i)
                #find_bond(bonds_dataframe,j)
            else:
                continue 
        else:
            continue

