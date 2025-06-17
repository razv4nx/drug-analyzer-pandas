#importing necessary libraries
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Crippen
from rdkit.Chem import Lipinski
from rdkit.Chem import rdMolDescriptors


#ask user for file name in order to use adequate reading command
file_name=input("input file name WITH extension:")
if file_name.endswith(".csv"):
  molecules = pd.read_csv(file_name)
elif file_name.endswith(".xlsx"):
  molecules=pd.read_excel(file_name)
else:
  print("File format not accepted!")
  

#data preview
print(molecules.head())

#initializing lists for storing properties of each molecule, they will be new columns later
MolWT=[]
logP=[]
NumH_d=[]
NumH_a=[]
rotBonds=[]
tpsa=[]

#processing each SMILES string and calculating adjacent properties
for smiles_string in molecules.SMILES:
  mol=Chem.MolFromSmiles(smiles_string)
  
  if mol:
    MolWT.append(rdkit.Chem.Descriptors.MolWt(mol))
    logP.append(rdkit.Chem.Crippen.MolLogP(mol))
    NumH_d.append(rdkit.Chem.Lipinski.NumHDonors(mol))
    NumH_a.append(rdkit.Chem.Lipinski.NumHAcceptors(mol))
    rotBonds.append(rdkit.Chem.Lipinski.NumRotatableBonds(mol))
    tpsa.append(rdkit.Chem.rdMolDescriptors.CalcTPSA(mol))

  else:   
    MolWT.append("NaN") 
    logP.append('NaN')
    NumH_d.append('NaN')
    NumH_a.append('NaN')
    rotBonds.append('NaN')
    tpsa.append('NaN')

     
#creating new columns
molecules["Molecular_Weight"]=MolWT
molecules["log P"]=logP
molecules["Num. Hydrogen Donors"]=NumH_d
molecules["Num. Hydrogen Acceptors"]=NumH_a
molecules["Rotateable Bonds"]=rotBonds
molecules["TPSA"]=tpsa

#exporting new data to the same document
if file_name.endswith(".csv"):
  molecules.to_csv(file_name, index=False)
elif file_name.endswith(".xlsx"):
  molecules.to_excel(file_name, index=False)

