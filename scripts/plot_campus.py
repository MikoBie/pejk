# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise, prepare_data_columnswise
from pejk.plots import plot_barhplot, plot_barplot
import pandas as pd

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df["P2"] = df.apply(lambda x: x.filter(regex=r"P2_\d+").sum(), axis=1)
df["P2"] = df.apply(
    lambda x: x.loc["P2_1":"P2_12"][x.loc["P2_1":"P2_12"] == 1].index[0].split("_")[-1]
    if x["P2"] == 1
    else None,
    axis=1,
).astype(float)
df["P3"] = df.apply(lambda x: x["P2"] if x["P3"] != x["P3"] else x["P3"], axis=1)
df = df.query("P4 < 8").query("P5 < 8")

df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]
df["bachelors"] = df.loc[:, "P1_1"]
df["masters"] = df.loc[:, "P1_2"]
df["five_years"] = df.loc[:, "P1_3"]
df["phds"] = df.loc[:, "P1_4"]

students = df.query("students > 0").reset_index(drop=True)
students.loc[:, "role"] = "student"
teachers = df.query("teachers > 0").reset_index(drop=True)
teachers.loc[:, "role"] = "teacher"
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)
non_teachers.loc[:, "role"] = "non_teacher"
bachelors = df.query("bachelors > 0").reset_index(drop=True)
bachelors.loc[:, "role"] = "bachelors"
masters = df.query("masters > 0").reset_index(drop=True)
masters.loc[:, "role"] = "masters"
five_years = df.query("five_years > 0").reset_index(drop=True)
five_years.loc[:, "role"] = "five_years"
phds = df.query("phds > 0").reset_index(drop=True)
phds.loc[:, "role"] = "phds"


ndf = pd.concat(
    [students, bachelors, masters, five_years, phds, teachers, non_teachers]
)

PERCENT = 100

# %%
## Popularność kampusów
lst = df.loc[:, "P2_1":"P2_12"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
campus = prepare_data_columnswise(
    df=df, f="P2_1", t="P2_12", weight=True, mapping=mappings.column_names_to_labels
).assign(count_population=lambda x: x["count"] * PERCENT / n)
fig = plot_barhplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle("Popularność kampusów", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "per_campus.png")
if __name__ != "__main__":
    plt.show()
campuses = campus.set_index("group")
# %%
## Histogram kampusów
lst = df.loc[:, "P2_1":"P2_12"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
campus = (
    df.assign(n_campus=lambda x: df.loc[:, "P2_1":"P2_12"].sum(axis=1))
    .groupby("n_campus")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"n_campus": "group", "WAGA": "count"})
    .assign(count_population=lambda x: x["count"] * PERCENT / n)
)

fig = plot_barplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby odwiedzanych kampusów uniwersyteckich",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.axes[0].xaxis.set_ticks([item for item in range(12)])
fig.savefig(PNG / "per_campus_distribution.png")
if __name__ != "__main__":
    plt.show()

histograms = campus.set_index("group")
# %%
n = df.query("P3 == P3").loc[:, "WAGA"].sum()
dominant_campus = prepare_data_rowise(
    df=df, key="P3", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=dominant_campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Główne miejsce pracy/studiowania/kształcenia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_campus-dominant.png")
if __name__ != "__main__":
    plt.show()

dominant_campuses = dominant_campus.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## POPULARITY OF CAMPUSES

    lst = role.loc[:, "P2_1":"P2_12"].columns
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    campus = prepare_data_columnswise(
        df=role,
        f="P2_1",
        t="P2_12",
        weight=True,
        mapping=mappings.column_names_to_labels,
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)
    fig = plot_barhplot(
        df=campus, x="group", y="count_population", labels=False, percenteges=True
    )
    fig.suptitle("Popularność kampusów", ha="center", fontsize=12, weight="bold")
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_campus.png")
    if __name__ != "__main__":
        plt.show()
    campuses = campuses.join(campus.set_index("group"), rsuffix=f" {_}")

    ## DISTRIBUTION OF VISITED CAMPUSES

    lst = role.loc[:, "P2_1":"P2_12"].columns
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    campus = (
        role.assign(n_campus=lambda x: role.loc[:, "P2_1":"P2_12"].sum(axis=1))
        .groupby("n_campus")["WAGA"]
        .sum()
        .reset_index()
        .rename(columns={"n_campus": "group", "WAGA": "count"})
        .assign(count_population=lambda x: x["count"] * PERCENT / n)
    )

    fig = plot_barplot(
        df=campus, x="group", y="count_population", labels=False, percenteges=True
    )
    fig.suptitle(
        "Rozkład liczby odwiedzanych kampusów uniwersyteckich",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.axes[0].xaxis.set_ticks([item for item in range(12)])
    fig.savefig(PNG / f"per_{_}_campus_distribution.png")
    if __name__ != "__main__":
        plt.show()

    histograms = histograms.join(campus.set_index("group"), rsuffix=f" {_}")

    ## DOMINANT CAMPUSES

    n = role.query("P3 == P3").loc[:, "WAGA"].sum()
    dominant_campus = prepare_data_rowise(
        df=role, key="P3", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=dominant_campus,
        x="group",
        y="count_population",
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Główne miejsce pracy/studiowania/kształcenia",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_campus-dominant.png")
    if __name__ != "__main__":
        plt.show()

    dominant_campuses = dominant_campuses.join(
        dominant_campus.set_index("group"), rsuffix=f" {_}"
    )

# %%
## POPULARITY OF CAMPUSES
(
    campuses.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Kampus"})
    .fillna(0)
    .to_excel(EXCEL / "P2.xlsx", index=False)
)
# %%
## DISTRIBUTION OF VISITED CAMPUSES
(
    histograms.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba kampusów"})
    .fillna(0)
    .to_excel(EXCEL / "P2_distribution.xlsx", index=False)
)

# %%
## DOMINANT CAMPUSES
(
    dominant_campuses.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Kampus"})
    .fillna(0)
    .to_excel(EXCEL / "P3.xlsx", index=False)
)
# %%
