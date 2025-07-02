# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise, prepare_data_columnswise
from pejk.plots import plot_barhplot, plot_barplot

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
## Liczebność grup
groups = prepare_data_columnswise(
    df=df, f="P1_1", t="P1_7", mapping=mappings.column_names_to_labels
)
groups.to_excel(EXCEL / "groups.xlsx")
fig = plot_barhplot(df=groups, x="group", y="count", padding=1)
fig.suptitle(
    "Liczebności w poszczególnych grupach", ha="center", fontsize=12, weight="bold"
)
fig.tight_layout()
fig.savefig(PNG / "groups.png")
if __name__ != "__main__":
    plt.show()

# %%

# %%
groups = (
    df.loc[:, "P1_1":"P1_7"]
    .sum(axis=1)
    .value_counts()
    .reset_index()
    .rename(columns={"index": "group"})
)
groups.to_excel(EXCEL / "roles-distribution.xlsx")
fig = plot_barplot(df=groups, x="group", y="count", padding=1)

fig.suptitle(
    "Rozkład liczby ról pełnionych na UW",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.axes[0].xaxis.set_ticks([item for item in range(4)])
fig.savefig(PNG / "roles-distribution.png")
if __name__ != "__main__":
    plt.show()

# %%
## Studia pierwszego stopnia
studies = prepare_data_columnswise(
    df=df, f="P33a_1", t="P33a_27", mapping=mappings.column_names_to_labels
)
studies.to_excel(EXCEL / "bachelor.xlsx")

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

studies.to_excel(EXCEL / "masters.xlsx")
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

studies.to_excel(EXCEL / "masters-five-years.xlsx")

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

studies.to_excel(EXCEL / "postgraduate.xlsx")

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
studies.to_excel(EXCEL / "teachers.xlsx")

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
studies.to_excel(EXCEL / "non-teachers.xlsx")

fig = plot_barhplot(studies, x="group", y="count", padding=1)
fig.suptitle(
    "Jednostki osób parcujących (nie nauczycieli akademickich)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non-teachers.png")
if __name__ != "__main__":
    plt.show()
# %%
## Szkoły doktorskie
phds = prepare_data_rowise(df=df, key="P33d", mapping=mappings.variable_value_labels)
studies.to_excel(EXCEL / "phds.xlsx")
fig = plot_barhplot(df=phds, x="group", y="count", padding=1)
fig.suptitle("Szkoły Doktorskie", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "phds.png")
if __name__ != "__main__":
    plt.show()

# %%
