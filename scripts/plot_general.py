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
(
    groups.rename(columns={"group": "Grupa", "count": "Liczebność"}).to_excel(
        EXCEL / "P1c.xlsx", index=False
    )
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
groups = (
    df.loc[:, "P1_1":"P1_7"]
    .sum(axis=1)
    .value_counts()
    .reset_index()
    .rename(columns={"index": "group"})
)
(
    groups.rename(columns={"group": "Liczba ról", "count": "Liczebność"}).to_excel(
        EXCEL / "P1b.xlsx", index=False
    )
)
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
    df=df,
    f="P33a_1",
    t="P33a_27",
    mapping=mappings.column_names_to_labels,
    abbrevations=False,
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

studies_all = studies.rename(columns={"count": "count bachelors"}).set_index("group")
# %%
## Studia drugiego stopnia
studies = prepare_data_columnswise(
    df=df,
    f="P33b_1",
    t="P33b_27",
    mapping=mappings.column_names_to_labels,
    abbrevations=False,
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

studies_all = studies_all.join(
    studies.set_index("group"), how="outer", rsuffix=" masters"
)
# %%
## Studia jednolite
studies = prepare_data_columnswise(
    df=df,
    f="P33c_1",
    t="P33c_5",
    mapping=mappings.column_names_to_labels,
    abbrevations=False,
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

studies_all = studies_all.join(
    studies.set_index("group"), how="outer", rsuffix=" five-years"
)
# %%
## Studia podyplomowe
studies = prepare_data_columnswise(
    df=df,
    f="P33e_1",
    t="P33e_18",
    mapping=mappings.column_names_to_labels,
    abbrevations=False,
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

studies_all = studies_all.join(
    studies.set_index("group"), how="outer", rsuffix=" postgraduate"
)
# %%
## Nauczyciele i nauczycielki akademiccy
studies = prepare_data_columnswise(
    df=df,
    f="P33f_1",
    t="P33f_18",
    mapping=mappings.column_names_to_labels,
    abbrevations=False,
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

studies_all = studies_all.join(
    studies.set_index("group"), how="outer", rsuffix=" teachers"
)
# %%
## Praconicy i pracownice
studies = prepare_data_columnswise(
    df=df,
    f="P33g_1",
    t="P33g_45",
    mapping=mappings.column_names_to_labels,
    abbrevations=False,
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
fig.savefig(PNG / "non-teachers.png")
if __name__ != "__main__":
    plt.show()

studies_all = studies_all.join(
    studies.set_index("group"), how="outer", rsuffix=" non_teachers"
)
# %%
## Szkoły doktorskie
phds = prepare_data_rowise(df=df, key="P33d", mapping=mappings.variable_value_labels)


fig = plot_barhplot(df=phds, x="group", y="count", padding=1)
fig.suptitle("Szkoły Doktorskie", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "phds.png")
if __name__ != "__main__":
    plt.show()

studies_all = studies_all.join(phds.set_index("group"), how="outer", rsuffix=" phds")
# %%
(
    studies_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność"
        )
    )
    .reset_index()
    .rename(columns={"group": "Jednostka"})
    .fillna(0)
    .to_excel(EXCEL / "P1.xlsx", index=False)
)

# %%
