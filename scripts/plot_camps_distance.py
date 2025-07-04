# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.plots import plot_barhplot
import pandas as pd
from pejk.config import (
    N_BACHELORS,
    N_MASTERS,
    N_STUDENTS,
    N_WEEKENDERS,
    N_FIVE_YEARS,
    N_PHDS,
)
from textwrap import wrap

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

df["students"] = df.loc[:, "P1_1":"P1_4"].sum(axis=1)
df["bachelors"] = df.loc[:, "P1_1"]
df["masters"] = df.loc[:, "P1_2"]
df["five_years"] = df.loc[:, "P1_3"]
df["phds"] = df.loc[:, "P1_4"]

students = df.query("students > 0").reset_index(drop=True)
bachelors = df.query("bachelors > 0").reset_index(drop=True)
bachelors.loc[:, "role"] = "bachelors"
masters = df.query("masters > 0").reset_index(drop=True)
masters.loc[:, "role"] = "masters"
five_years = df.query("five_years > 0").reset_index(drop=True)
five_years.loc[:, "role"] = "five_years"
phds = df.query("phds > 0").reset_index(drop=True)
phds.loc[:, "role"] = "phds"

PERCENT = 100

ndf = pd.concat([bachelors, masters, five_years, phds])

N_dct = {
    "phds": N_PHDS,
    "five_years": N_FIVE_YEARS,
    "masters": N_MASTERS - N_FIVE_YEARS,
    "bachelors": N_BACHELORS,
    "all": N_STUDENTS - N_WEEKENDERS,
}

# %%
## camps means of transport distance
camps_transport_distance = students.query("P19 == P19").reset_index(drop=True)
n = camps_transport_distance.loc[:, "WAGA"].sum()

camps_transport_distance.loc[:, "km"] = camps_transport_distance.loc[
    :, "WAGA"
].multiply(camps_transport_distance.loc[:, "P19"], axis=0)

camps_transport_distance_means = (
    camps_transport_distance.groupby("P18")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P18": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P18"]})
)
fig = plot_barhplot(
    df=camps_transport_distance_means,
    x="group",
    y="km_mean",
    padding=1,
    labels=True,
    percenteges=False,
)
fig.suptitle(
    "Średni dystans jednego dojazdu na obóz/praktykę poza Warszawą",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "camps-transport-distance.png")
if __name__ != "__main__":
    plt.show()

camps_transport_distance_all = camps_transport_distance_means.set_index("group")
# %%
## camps means of transport dates
camps_dates_distance = students.query("P19 == P19").reset_index(drop=True)
n = camps_dates_distance.loc[:, "WAGA"].sum()

camps_dates_distance.loc[:, "km"] = camps_dates_distance.loc[:, "WAGA"].multiply(
    camps_dates_distance.loc[:, "P19"], axis=0
)

camps_dates_distance_means = (
    camps_dates_distance.groupby("P20")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P20": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P20"]})
)
camps_dates_distance_means["group"] = camps_dates_distance_means["group"].apply(
    lambda x: "\n".join(wrap(x, 30)) if isinstance(x, str) else x
)
fig = plot_barhplot(
    df=camps_dates_distance_means,
    x="group",
    y="km_mean",
    padding=1,
    labels=True,
    percenteges=False,
)
fig.suptitle(
    "Średni dystans jednego dojazdu na obóz/praktykę poza Warszawą",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "camps-dates-distance.png")
if __name__ != "__main__":
    plt.show()

camps_dates_distance_all = camps_dates_distance_means.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## CAMPS MEANS OF TRANSPORT DISTANCE
    camps_transport_distance = role.query("P19 == P19").reset_index(drop=True)
    n = camps_transport_distance.loc[:, "WAGA"].sum()

    camps_transport_distance.loc[:, "km"] = camps_transport_distance.loc[
        :, "WAGA"
    ].multiply(camps_transport_distance.loc[:, "P19"], axis=0)

    camps_transport_distance_means = (
        camps_transport_distance.groupby("P18")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P18": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P18"]})
    )
    fig = plot_barhplot(
        df=camps_transport_distance_means,
        x="group",
        y="km_mean",
        padding=1,
        labels=True,
        percenteges=False,
    )
    fig.suptitle(
        "Średni dystans jednego dojazdu na obóz/praktykę poza Warszawą",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"{_}_camps-transport-distance.png")
    if __name__ != "__main__":
        plt.show()

    camps_transport_distance_all = camps_transport_distance_all.join(
        camps_transport_distance_means.set_index("group"), rsuffix=f" {_}"
    )

    ## CAMPS MEANS OF TRANSPORT DATES
    camps_dates_distance = role.query("P19 == P19").reset_index(drop=True)
    n = camps_dates_distance.loc[:, "WAGA"].sum()

    camps_dates_distance.loc[:, "km"] = camps_dates_distance.loc[:, "WAGA"].multiply(
        camps_dates_distance.loc[:, "P19"], axis=0
    )

    camps_dates_distance_means = (
        camps_dates_distance.groupby("P20")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P20": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P20"]})
    )
    camps_dates_distance_means["group"] = camps_dates_distance_means["group"].apply(
        lambda x: "\n".join(wrap(x, 30)) if isinstance(x, str) else x
    )
    fig = plot_barhplot(
        df=camps_dates_distance_means,
        x="group",
        y="km_mean",
        padding=1,
        labels=True,
        percenteges=False,
    )
    fig.suptitle(
        "Średni dystans jednego dojazdu na obóz/praktykę poza Warszawą",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"{_}_camps-dates-distance.png")
    if __name__ != "__main__":
        plt.show()

    camps_dates_distance_all = camps_dates_distance_all.join(
        camps_dates_distance_means.set_index("group"), rsuffix=f" {_}"
    )
# %%
## CAMPS MEANS OF TRANSPORT DISTANCE
(
    camps_transport_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Główny środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P19_transport.xlsx", index=False)
)

# %%
## CAMPS MEANS OF TRANSPORT DATES
(
    camps_dates_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Data"})
    .fillna(0)
    .to_excel(EXCEL / "P19b_dates.xlsx", index=False)
)

# %%
