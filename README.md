# CECS 450 - Project 1: Emergency Department Burden Analysis

Due date: 10/06/2025

## Authors 
Team 4:
- Isabella Alvarez
- Brizeyda Hermandez
- Anh Pham
- Salvador Sanchez
- Silvia Tran


## Objectives
- Visualizes and analyzes the burden ratio of emergency departments across Southern California counties.
- Allow interactive filtering by year and bars segment by category.
- Enable hover tooltips to show extra details.


## About the Data
_Data Source:_ https://data.ca.gov/dataset/emergency-department-volume-and-capacity

The input data is stored at data/emergency-department-volume-and-capacity-2021-2023.xlsx

For this project, we focused on 10 Southern California counties, selected based on population data from California counties by population (2025). World Population Review. (n.d.). https://worldpopulationreview.com/us-counties/california 

The counties are listed below in descending order of population:
1. Los Angeles
2. San Diego
3. Orange
4. Riverside
5. San Bernardino
6. Ventura
7. Kern
8. Santa Barbara
9. San Luis Obispo
10. Imperial


## Requiremets
python 3.8+

pandas

plotly

openpyxl

## Project Structure
```bash
ed-volume-capacity/ # Root
│
├── .idea/ # PyCharm project settings 
|
├── data/ # Contains dataset
│ ├── data-dictionary-emergency-department-volume-and-capacity.csv
│ ├── datapackage.json
│ └── emergency-department-volume-and-capacity-2021-2023.xlsx
│
│
├── src/ # Python scripts for data processing and plotting
│ ├── pycache/
│ ├── data_loader.py
│ ├── index.html
│ └── timeline_viz.py
│
│
├── index.html
├── README.md # Project overview (this file)
└── requirements.txt # Python dependencies
```

## Project Set Up and Run Instruction
1. Clone this repository:
```bash
git clone https://github.com/silviatran/ed-volume-capacity
```

2. Navigate to the project folder:

_After cloning, make sure you are inside the project directory_
```bash
cd ed-volume-capacity
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Change directory:
```bash
cd src
```

5. Run the project
```bash
python timeline_viz.py
```
