# %%
import pyreadstat
from pejk import RAW, PNG
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise, prepare_data_columnswise
from pejk.plots import plot_barhplot, plot_barplot

## plt.rc("figure.suptitle", horizontalalignment = "center")
# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
## Liczebność grup
groups = prepare_data_columnswise(
    df=df, f="P1_1", t="P1_7", mapping=mappings.column_names_to_labels
)
fig = plot_barhplot(df=groups, x="group", y="count", padding=1)
fig.suptitle(
    "Liczebności w poszczególnych grupach", ha="center", fontsize=12, weight="bold"
)
fig.tight_layout()
fig.savefig(PNG / "groups.png")
if __name__ != "__main__":
    plt.show()

# %%
## Popularność kampusów
campus = prepare_data_columnswise(
    df=df, f="P2_1", t="P2_12", weight=False, mapping=mappings.column_names_to_labels
)
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

fig = plot_barplot(df=campus, x="group", y="count", padding=1)
fig.suptitle(
    "Rozkład częstości bywania na kampusach uniwersyteckich",
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
## Studia pierwszego stopnia
studies = prepare_data_columnswise(
    df=df, f="P33a_1", t="P33a_27", mapping=mappings.column_names_to_labels
)

fig = plot_barhplot(studies, x="group", y="count", padding=1)
fig.suptitle(
    "Jednostki osób studenckich studiów I stopnia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "bachelor.png")
if __name__ != "__main__":
    plt.show()

# %%
## Studia drugiego stopnia
studies = prepare_data_columnswise(
    df=df, f="P33b_1", t="P33b_27", mapping=mappings.column_names_to_labels
)

fig = plot_barhplot(df=studies, x="group", y="count", padding=1)
fig.suptitle(
    "Jednostki osób studenckich studiów II stopnia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "masters.png")
if __name__ != "__main__":
    plt.show()
# %%
## Studia jednolite
studies = prepare_data_columnswise(
    df=df, f="P33c_1", t="P33c_5", mapping=mappings.column_names_to_labels
)


fig = plot_barhplot(df=studies, x="group", y="count", padding=1)
fig.suptitle(
    "Jednostki osób studenckich studiów jednolitych",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "masters-five-years.png")
if __name__ != "__main__":
    plt.show()

# %%
## Studia podyplomowe
studies = prepare_data_columnswise(
    df=df, f="P33e_1", t="P33e_18", mapping=mappings.column_names_to_labels
).query("count > 0")


fig = plot_barhplot(df=studies, x="group", y="count", padding=1)
fig.suptitle(
    "Jednostki osób studenckich studiów podyplomowych",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "postgraduate.png")
if __name__ != "__main__":
    plt.show()
# %%
## Nauczyciele i nauczycielki akademiccy
studies = prepare_data_columnswise(
    df=df, f="P33f_1", t="P33f_18", mapping=mappings.column_names_to_labels
)

fig = plot_barhplot(df=studies, x="group", y="count", padding=1)
fig.suptitle(
    "Jednostki osób pracujących (nauczycieli akademickich)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers.png")
if __name__ != "__main__":
    plt.show()

# %%
## Praconicy i pracownice
studies = prepare_data_columnswise(
    df=df, f="P33g_1", t="P33g_45", mapping=mappings.column_names_to_labels
)

studies = studies.groupby("group").sum().reset_index().sort_values("count")

fig = plot_barhplot(studies, x="group", y="count", padding=1)
fig.suptitle(
    "Jednostki osób parcujących (nie nauczycieli akademickich)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "no-teachers.png")
if __name__ != "__main__":
    plt.show()
# %%
## Szkoły doktorskie
phds = prepare_data_rowise(df=df, key="P33d", mapping=mappings.variable_value_labels)
fig = plot_barhplot(df=phds, x="group", y="count", padding=1)
fig.suptitle("Szkoły Doktorskie", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "phds.png")
if __name__ != "__main__":
    plt.show()

# %%
