"""
CECS 450 Data Visualization
Fall 2025
Project 1: Emergency Department Burden Visualization
Due Date: October 6, 2025

Team 4:
- Isabella Alvarez (ID: )
- Brizeyda Hernandez (ID:)
- Anh Pham (ID: 030877663)
- Salvador Sanchez (ID: 030187961)
- Silvia Tran (ID:)

Goal:
- Visualize ED Burden Ratio (Total ED Visits / ED Stations) across counties.
- Allow interactive filtering by year and category.
- Enable hover tooltips to show extra details (raw values, shortage status, etc.).

"""

import pandas as pd
import plotly.express as px
import matplotlib as plt


# ================================
# 1. Data Preprocessing 
# ================================
# TODO:
# - Load CSV file into pandas DataFrame
# - Clean missing/invalid values
# - Ensure numeric columns (Tot_ED_NmbVsts, EDStations) are floats/ints
# - Calculate Burden Ratio 
# - Group data as needed (by County, Year, Category)
def preprocess_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)

    # Select cols that we will use later
    relevant_cols = [
        "CountyName",
        "year",
        "UrbanRuralDesi",
        "Category",
        "Tot_ED_NmbVsts",
        "EDStations",
        "PrimaryCareShortageArea",
        "Visits_Per_Station"
    ]
    df = df[relevant_cols]
    
    # Drop rows with missing values in critical fields
    df = df.dropna(subset=["Tot_ED_NmbVsts", "EDStations", "Visits_Per_Station"])
    
    # Convert numeric columns
    df["Tot_ED_NmbVsts"] = pd.to_numeric(df["Tot_ED_NmbVsts"], errors="coerce")
    df["EDStations"] = pd.to_numeric(df["EDStations"], errors="coerce")
    df["Visits_Per_Station"] = pd.to_numeric(df["Visits_Per_Station"], errors="coerce")
    
    # Calculate Burden Ratio from Total Visits and Stations, add it as a new column
    df["Burden_Ratio"] = df["Tot_ED_NmbVsts"] / df["EDStations"]
    
    # Clean PrimaryCareShortageArea column (standardize Yes/No)
    df["PrimaryCareShortageArea"] = df["PrimaryCareShortageArea"].str.strip().str.title()
        
    print(df.head()) # Print initial rows for inspection
    
    return df



# ================================
# 2. Graph Setup 
# ================================
# TODO:
# - Create initial bar chart
# - X-axis: County
# - Y-axis: Burden Ratio
# - Set title, axis labels, layout

def plot_initial_graph(df: pd.DataFrame):
    # Filter for top 10 counties in California

    # Make a list of the top 10 counties in California by population
    counties = ['Los Angeles', 'San Diego', 'Orange', 
    'Riverside', 'San Bernardino', 'Kern', 'Ventura', 'Santa Barbara', 'San Luis Obispo', 'Imperial']

    # Keep only rows for those counties
    filtered_df = df.loc[df["CountyName"].isin(counties)].copy()
    
    # Group by CountyName and calculate the mean Burden Ratio for each county
    grouped_df = filtered_df.groupby("CountyName", as_index=False)["Burden_Ratio"].mean()

    fig = px.bar(
        grouped_df,
        x="CountyName",
        y="Burden_Ratio",
        title="Burden Ratio of Hospitals by County",
        labels={"ED Burden Rate": "Burden Ratio", "CountyName": "Top 10 Counties in California"},
        color="CountyName"
    )

    fig.show()


# ================================
# 3. Filters/Slider
# ================================
# TODO (suggested, subject to change):
# - Add dropdown/slider for "Year"
# - Add dropdown for "Category"
# - Make sure graph updates when filter is applied

# Example with Plotly Express:
# fig = px.bar(
#     df[(df["year"]==2022) & (df["Category"]=="Active COVID-19")],
#     x="CountyName", y="Burden_Ratio"
# )

# ================================
# 4. Hover Tooltip Enhancement
# ================================
# TODO:
# - Customize hover data to include (suggested, subject to change):
# --- Suggested fields---------
#   * Total Visits
#   * Stations
#   * Hospital
#   * Urban/Rural
# - Format hover info neatly

# Example:
# fig = px.bar(
#     df, 
#     x="CountyName", y="Burden_Ratio",
#     hover_data=["year", "Category", "Tot_ED_NmbVsts", "EDStations"]
# )

# ================================
# 5. Integration & Testing
# ================================
# TODO:
# ***Define main function to run app***
# - Combine all parts into the final app
# - Test filters, hover effects
# - Clean up code, add comments
# - Optionally integrate with Dash (if making a web app)
# - Deliver final visualization

def main():
    # Load and preprocess data
    df = preprocess_data("..\\data\\emergency-department-volume-and-capacity-2021-2023.xlsx")
    
    # Plot initial graph
    plot_initial_graph(df)
    
    # Further steps: Add filters, enhance hover tooltips, integrate into web app if needed

if __name__ == "__main__":
    main()