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

# REPLACE WITH THE PATH TO YOUR EXCEL FILE
xls = pd.ExcelFile("C:\\Users\\sanju\\Downloads\\CSULB\\FALL2025\\CECS450\\Project1\\emergency-department-volume-and-capacity-2021-2023.xlsx", engine="openpyxl")
print(f'Sheets: {xls.sheet_names}')
df = xls.parse('ED_COMBINE_AL')
print(f'Everything else\n------\n{df.head()}')


file_path = "C:\\Users\\sanju\\Downloads\\CSULB\\FALL2025\\CECS450\\Project1\\emergency-department-volume-and-capacity-2021-2023.xlsx"
df = pd.read_excel(file_path)
print(df.head())




filtered_df = df.query("year == 2021 and CountyName in ['Los Angeles', 'San Diego', 'Orange', 'Riverside', 'San Bernardino', 'Kern', 'Ventura', 'Santa Barbara', 'San Luis Obispo', 'Imperial']")
filtered_df["ED Burden Rate"] = (filtered_df["Tot_ED_NmbVsts"] / filtered_df["EDStations"]) * 100
grouped_df = filtered_df.groupby("CountyName", as_index=False)["ED Burden Rate"].mean()


fig = px.bar(
    grouped_df,
    x="CountyName",
    y="ED Burden Rate",
    title="Burden Ratio of Hospitals by County",
    labels={"ED Burden Rate": "Burden Ratio", "CountyName": "Top 10 Counties in California"},
    color="CountyName"
)

fig.show()

# ================================
# 1. Data Preprocessing 
# ================================
# TODO:
# - Load CSV file into pandas DataFrame
# - Clean missing/invalid values
# - Ensure numeric columns (Tot_ED_NmbVsts, EDStations) are floats/ints
# - Calculate Burden Ratio 
# - Group data as needed (by County, Year, Category)



# ================================
# 2. Graph Setup 
# ================================
# TODO:
# - Create initial bar chart
# - X-axis: County
# - Y-axis: Burden Ratio
# - Set title, axis labels, layout


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



