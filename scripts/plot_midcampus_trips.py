# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise
from pejk.plots import plot_barhplot
import pandas as pd
from pejk.config import (
    N_ALL,
    N_STUDENTS,
    N_TEACHERS,
    N_NON_TEACHERS,
    N_BACHELORS,
    N_MASTERS,
    N_FIVE_YEARS,
    N_PHDS,
)

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]
df["bachelors"] = df.loc[:, "P1_1"]
df["masters"] = df.loc[:, "P1_2"]
df["five_years"] = df.loc[:, "P1_3"]
df["phds"] = df.loc[:, "P1_4"]

students = df.query("students > 0").reset_index(drop=True)
students.loc[:, "role"] = "student"
teachers = (
    df.query("teachers > 0").query("P11 != 97 and P9 != 23").reset_index(drop=True)
)
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
N_dct = {
    "all": N_ALL,
    "teacher": N_TEACHERS,
    "student": N_STUDENTS,
    "non_teacher": N_NON_TEACHERS,
    "phds": N_PHDS,
    "five_years": N_FIVE_YEARS,
    "masters": N_MASTERS - N_FIVE_YEARS,
    "bachelors": N_BACHELORS,
}

PERCENT = 100
# %%
## Midcampus trips
n = df.query("P9 == P9").loc[:, "WAGA"].sum()
midcampus = prepare_data_rowise(
    df=df, key="P9", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=midcampus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład podróży pomiędzy kampusami",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_midcampus-distribution.png")
if __name__ != "__main__":
    plt.show()

midcampus_distribution = midcampus.set_index("group")
# %%
## Midcampus trips dominant means of transport
n = df.query("P10 == P10").loc[:, "WAGA"].sum()
transport_dominant = prepare_data_rowise(
    df=df, key="P10", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=transport_dominant,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Główny środek lokomocji pomiędzy kampusami",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_midcampus-dominant-transport.png")
if __name__ != "__main__":
    plt.show()

midcampus_dominant_transport = transport_dominant.set_index("group")
# %%
## Midcampus trips dominant means of transport distance
midcampus_distance = df.query("P9 == P9").reset_index(drop=True)
n = midcampus_distance.loc[:, "WAGA"].sum()

midcampus_distance.loc[:, "km"] = midcampus_distance.loc[:, "WAGA"].multiply(
    midcampus_distance.loc[:, "P11"], axis=0
)

midcampus_distance_means = (
    midcampus_distance.groupby("P10")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P10": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P10"]})
)
fig = plot_barhplot(
    df=midcampus_distance_means,
    x="group",
    y="km_mean",
    padding=1,
    labels=True,
    percenteges=False,
)
fig.suptitle(
    "Średni dystans jednej podróży między kampusami",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "midcampus-trip-distance.png")
if __name__ != "__main__":
    plt.show()

midcampus_distance_km = midcampus_distance_means.set_index("group")

# %%
for _, role in ndf.groupby("role"):
    ## MIDCAMPUS TRIPS

    n = role.query("P9 == P9").loc[:, "WAGA"].sum()
    midcampus = prepare_data_rowise(
        df=role, key="P9", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=midcampus, x="group", y="count_population", labels=False, percenteges=True
    )
    fig.suptitle(
        "Rozkład podróży pomiędzy kampusami",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_midcampus-distribution.png")
    if __name__ != "__main__":
        plt.show()

    midcampus_distribution = midcampus_distribution.join(
        midcampus.set_index("group"), rsuffix=f" {_}"
    )

    ## MIDCAMPUS TRIPS DOMINANT MEANS OF TRANSPORT

    n = role.query("P10 == P10").loc[:, "WAGA"].sum()
    transport_dominant = prepare_data_rowise(
        df=role, key="P10", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=transport_dominant,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Główny środek lokomocji pomiędzy kampusami",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_midcampus-dominant-transport.png")
    if __name__ != "__main__":
        plt.show()

    midcampus_dominant_transport = midcampus_dominant_transport.join(
        transport_dominant.set_index("group"), rsuffix=f" {_}"
    )

    ## MIDCAMPUS TRIPS DOMINANT MEANS OF TRANSPORT DISTANCE

    midcampus_distance = role.query("P9 == P9").reset_index(drop=True)
    midcampus_distance.loc[:, "WAGA"] = 1
    n = midcampus_distance.loc[:, "WAGA"].sum()

    midcampus_distance.loc[:, "km"] = midcampus_distance.loc[:, "WAGA"].multiply(
        midcampus_distance.loc[:, "P11"], axis=0
    )

    midcampus_distance_means = (
        midcampus_distance.groupby("P10")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P10": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P10"]})
    )
    fig = plot_barhplot(
        df=midcampus_distance_means,
        x="group",
        y="km_mean",
        padding=1,
        labels=True,
        percenteges=False,
    )
    fig.suptitle(
        "Średni dystans jednej podróży pomiędzy kampusami",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"{_}_midcampus-trip-distance.png")
    if __name__ != "__main__":
        plt.show()

    midcampus_distance_km = midcampus_distance_km.join(
        midcampus_distance_means.set_index("group"), rsuffix=f" {_}"
    )

# %%
## MIDCAMPUS TRIPS
(
    midcampus_distribution.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba podróży pomiędzy kampusami"})
    .fillna(0)
    .to_excel(EXCEL / "P9.xlsx", index=False)
)
# %%
## MIDCAMPUS TRIPS DOMINANT MEANS OF TRANSPORT
(
    midcampus_dominant_transport.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Główny środek transportu pomiędzy kampusami"})
    .fillna(0)
    .to_excel(EXCEL / "P10.xlsx", index=False)
)

# %%
## MIDCAMPUS TRIPS DOMINANT MEANS OF TRANSPORT DISTANCE
(
    midcampus_distance_km.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Główny środek transportu pomiędzy kampusami"})
    .fillna(0)
    .to_excel(EXCEL / "P11.xlsx", index=False)
)
# %%
