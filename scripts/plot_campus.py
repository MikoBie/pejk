# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise, prepare_data_columnswise
from pejk.plots import plot_barhplot, plot_barplot

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
## Popularność kampusów
campus = prepare_data_columnswise(
    df=df, f="P2_1", t="P2_12", weight=False, mapping=mappings.column_names_to_labels
)
campus.to_excel(EXCEL / "campus.xlsx")
fig = plot_barhplot(df=campus, x="group", y="count", padding=0.7)
fig.suptitle("Popularność kampusów", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "campus.png")
if __name__ != "__main__":
    plt.show()

# %%
## Histogram kampusów
campus = (
    df.loc[:, "P2_1":"P2_12"]
    .sum(axis=1)
    .value_counts()
    .reset_index()
    .rename(columns={"index": "group"})
)
campus.to_excel(EXCEL / "campus-distribution.xlsx")

fig = plot_barplot(df=campus, x="group", y="count", padding=1)
fig.suptitle(
    "Rozkład liczby odwiedzanych kampusów uniwersyteckich",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.axes[0].xaxis.set_ticks([item for item in range(12)])
fig.savefig(PNG / "campus_distribution.png")
if __name__ != "__main__":
    plt.show()

# %%
dominant_campus = prepare_data_rowise(
    df=df, key="P3", mapping=mappings.variable_value_labels
)

dominant_campus.to_excel(EXCEL / "campus-dominant.xlsx")

fig = plot_barhplot(df=dominant_campus, x="group", y="count", padding=1)
fig.suptitle(
    "Główne miejsce pracy/studiowania/kształcenia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "campus-dominant.png")
if __name__ != "__main__":
    plt.show()

# %%
