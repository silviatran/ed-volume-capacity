import os
import plotly.express as px
import plotly.graph_objects as go
from data_loader import load_and_clean, get_burden_by_county_and_category

base_dir = os.path.dirname(os.path.dirname(__file__))
filepath = os.path.join(base_dir, "data", "emergency-department-volume-and-capacity-2021-2023.xlsx")
df = load_and_clean(filepath)


YEARS = ["All", 2021, 2022, 2023]
DEFAULT = "All"

# precompute datasets for each year
data_by_year = {}
cat_orders = {}   # store order per year
for yr in YEARS:
    g = get_burden_by_county_and_category(
        df, year=None if yr == "All" else yr, top_10_by_population=True
    )
    data_by_year[yr] = g.copy()

    # calculate order for this year’s dataset
    order = (
        g.groupby("Category")["Burden_Ratio"]
         .sum()
         .sort_values(ascending=True)
         .index.tolist()
    )
    cat_orders[yr] = order

# fix the county order
counties = list(data_by_year[DEFAULT]["CountyName"].unique())

# create the figure
fig = go.Figure()
trace_meta = []  # track (year, category)


all_categories = sorted(df["Category"].dropna().unique())
palette = px.colors.qualitative.Plotly + px.colors.qualitative.Set3[:5]
color_map = {cat: palette[i % len(palette)] for i, cat in enumerate(all_categories)}


def add_year_traces(yr, visible=False):
    g = data_by_year[yr]
    cat_order = cat_orders[yr]  # dynamic per year

    for cat in cat_order:
        vals = []
        for c in counties:
            v = g.loc[(g["CountyName"] == c) & (g["Category"] == cat), "Burden_Ratio"]
            vals.append(float(v.iloc[0]) if len(v) else 0.0)

        fig.add_bar(
            x=counties,
            y=vals,
            name=str(cat),
            marker_color=color_map[cat],
            visible=visible,
            hovertemplate="<br>Condition: " + str(cat) +
                          "<br>Burden Ratio: %{y:.2f}<extra></extra> ED visits per station"
        )
        trace_meta.append((yr, cat))


for yr in YEARS:
    add_year_traces(yr, visible=(yr == DEFAULT))

# create the dropdown buttons
buttons = []
total_traces = len(fig.data)

for yr in YEARS:
    vis = [False] * total_traces
    for i, (t_year, _cat) in enumerate(trace_meta):
        if t_year == yr:
            vis[i] = True

    title_text = f"Burden Ratio by County (Top 10 by Population) — {('2021–2023' if yr=='All' else yr)}"
    buttons.append(dict(
        label=("2021–2023" if yr == "All" else str(yr)),
        method="update",
        args=[{"visible": vis}, {"title": title_text}]
    ))

# visualization layout
fig.update_layout(
    barmode="stack",
    title=f"Burden Ratio by County (Top 10 by Population) — {('2021–2023' if DEFAULT=='All' else DEFAULT)}",
    xaxis=dict(title="County", tickangle=-45),
    yaxis=dict(title="Burden Ratio", separatethousands=True),
    legend_title_text="Health-Related Condition",
    width=1250, height=750,
    margin=dict(l=40, r=20, t=70, b=80),
    # legend
    updatemenus=[dict(
        type="dropdown",
        direction="down",
        x=1.025, y=0.4,
        xanchor="left", yanchor="top",
        showactive=True,
        buttons=buttons
    )]
)

# save and show to html
fig.write_html("index.html", include_plotlyjs=True, full_html=True)
fig.show()
print("Chart saved to index.html")
