"""
CECS 450 Data Visualization
Fall 2025
Project 1: Emergency Department Burden Visualization
Due Date: October 6, 2025

Team 4:
- Isabella Alvarez (ID: )
- Brizeyda Hernandez (ID:)
- Anh Pham (ID: 030877663)
- Salvador Sanchez (ID:)
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
# - Calculate Burden Ratio = Tot_ED_NmbVsts / EDStations
# - Group data as needed (by County, Year, Category)

# Example:
# df["Burden_Ratio"] = df["Tot_ED_NmbVsts"] / df["EDStations"]

# ================================
# 2. Graph Setup 
# ================================
# TODO:
# - Create initial bar chart
# - X-axis: County
# - Y-axis: Burden Ratio
# - Color: shortage (Yes/No) OR keep it uniform
# - Set title, axis labels, layout

# Example:
# fig = px.bar(df, x="CountyName", y="Burden_Ratio", color="PrimaryCareShortageArea")

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

# Example: fig.show() to test locally
