# CECS 450 - Project 1: Emergency Department Burden Analysis

Due date: 10/06/2025

## Authors 
Team 4:
- Isabella Alvarez
- Brizeyda Hermandez
- Anh Pham
- Salvador Sanchez
- Silvia Tran

## Data
_Data Source:_ https://data.ca.gov/dataset/emergency-department-volume-and-capacity

The input data is stored at data/emergency-department-volume-and-capacity-2021-2023.xlsx

## Objectives
- Visualizes and analyzes the burden ratio of emergency departments across Southern California counties.
- Allow interactive filtering by year and bars segment by category.
- Enable hover tooltips to show extra details.

## Requiremets
python 3.8+

pandas

plotly

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

## Setup
1. Clone this repository:
```bash
git clone https://github.com/silviatran/ed-volume-capacity
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Change directory
```bash
cd ed-volume-capacity/src
```

4. Run the project
```bash
python timeline_viz.py
```
