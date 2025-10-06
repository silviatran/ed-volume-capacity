import pandas as pd

def load_and_clean(filepath, sheet_name=0):
    df = pd.read_excel(filepath, sheet_name=sheet_name)

    # keep only the relevant columns
    cols = ["CountyName", "year", "Category", "EDStations", "EDDXCount"]
    df = df[cols].dropna(subset=["CountyName", "Category", "EDStations"])

    # ensure no dividing by 0
    df = df[df["EDStations"] > 0]

    return df


def get_burden_by_county_and_category(df, year=None, top_10_by_population=True):
    # filter year
    if year is not None:
        df = df[df["year"] == year]

    # remove overall total category (not a condition)
    df = df[df["Category"].str.strip().str.lower() != "all ed visits"]

    # aggregate: County × Category
    grouped = (
        df.groupby(["CountyName", "Category"], as_index=False)
          .agg(EDDXCount=("EDDXCount", "sum"),
               EDStations=("EDStations", "sum"))
    )
    grouped["Burden_Ratio"] = grouped["EDDXCount"] / grouped["EDStations"]

    # get top 10 counties in SoCal by population
    if top_10_by_population:
        TOP10_POP = [
            "Los Angeles","San Diego","Orange","Riverside","San Bernardino", "Kern",
                        "Ventura", "Santa Barbara", "San Luis Obispo", "Imperial"
        ]
        grouped = grouped[grouped["CountyName"].isin(TOP10_POP)]
        grouped["CountyName"] = pd.Categorical(
            grouped["CountyName"], categories=TOP10_POP, ordered=True
        )
        grouped = grouped.sort_values("CountyName")

    return grouped
