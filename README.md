# SMILES Drug Analyzer 

A simple drug analyzer built in Python using *Pandas and RDkit* libraries.

Outputs a modified version of the initial dataset to the same `.csv` or a `.xlsx` file, containing the molecular weight, logP, number of hydrogen bond donors/acceptors, number of rotateable bonds and the topological polar surface area (TPSA).



## Input Format

Your input should be a `.csv` or an `.xlsx` file with a column named `SMILES` (ideally the column should contain *valid* SMILES strings):
Here's a short `.csv` example:

```csv
Name,SMILES
Aspirin,CC(=O)OC1=CC=CC=C1C(=O)O
Caffeine,CN1C=NC2=C1C(=O)N(C(=O)N2C)C
Paracetamol,CC(=O)NC1=CC=C(C=C1)O
```


## Useful info

RDKit is an open-source cheminformatics software toolkit, usually installed using a ***Conda enviornment***. For that matter, if you haven't already installed the necessary libraries for this program, I urge you to either **install** the **`enviornment.yml`** document found in this repository (follow the instructions below) or to use a *Conda enviornment* when installing RDkit ([here's a useful tutorial made by the developers of RDkit](https://www.rdkit.org/docs/Install.html)), and use **pip install** for the other libraries.


## How to use

**1) Clone or download this repository**
   
```bash
git clone https://github.com/razv4nx/drug-analyzer-pandas.git
cd drug-analyzer-pandas
```


**2) Create the environment (requires Anaconda or Miniconda)**
   
```bash
conda env create -f environment.yml
```

 
**3)  Activate the environment**

```bash
conda activate drug_analyzer_env
```


**4) Run the script**

```bash
python drug_analyzer.py input.csv
```

## Author
Made by Razvan Bauer (@razv4nx)

I'm open to all feedback and improvements!

