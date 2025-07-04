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
## Internships means of transport distance
internship_transport_distance = students.query("P16 == P16").reset_index(drop=True)
n = internship_transport_distance.loc[:, "WAGA"].sum()

internship_transport_distance.loc[:, "km"] = internship_transport_distance.loc[
    :, "WAGA"
].multiply(internship_transport_distance.loc[:, "P16"], axis=0)

internship_transport_distance_means = (
    internship_transport_distance.groupby("P15")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P15": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P15"]})
)
fig = plot_barhplot(
    df=internship_transport_distance_means,
    x="group",
    y="km_mean",
    padding=1,
    labels=True,
    percenteges=False,
)
fig.suptitle(
    "Średni dystans jednego dojazdu na praktyki",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "internship-transport-distance.png")
if __name__ != "__main__":
    plt.show()

internship_transport_distance_all = internship_transport_distance_means.set_index(
    "group"
)
# %%
## Internships means of transport dates
internship_dates_distance = students.query("P16 == P16").reset_index(drop=True)
n = internship_dates_distance.loc[:, "WAGA"].sum()

internship_dates_distance.loc[:, "km"] = internship_dates_distance.loc[
    :, "WAGA"
].multiply(internship_dates_distance.loc[:, "P16"], axis=0)

internship_dates_distance_means = (
    internship_dates_distance.groupby("P17")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P17": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P17"]})
)
internship_dates_distance_means["group"] = internship_dates_distance_means[
    "group"
].apply(lambda x: "\n".join(wrap(x, 30)) if isinstance(x, str) else x)
fig = plot_barhplot(
    df=internship_dates_distance_means,
    x="group",
    y="km_mean",
    padding=1,
    labels=True,
    percenteges=False,
)
fig.suptitle(
    "Średni dystans jednego dojazdu na praktyki",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "internship-dates-distance.png")
if __name__ != "__main__":
    plt.show()

internship_dates_distance_all = internship_dates_distance_means.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## INTERNSHIPS MEANS OF TRANSPORT DISTANCE
    internship_transport_distance = role.query("P16 == P16").reset_index(drop=True)
    n = internship_transport_distance.loc[:, "WAGA"].sum()

    internship_transport_distance.loc[:, "km"] = internship_transport_distance.loc[
        :, "WAGA"
    ].multiply(internship_transport_distance.loc[:, "P16"], axis=0)

    internship_transport_distance_means = (
        internship_transport_distance.groupby("P15")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P15": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P15"]})
    )
    fig = plot_barhplot(
        df=internship_transport_distance_means,
        x="group",
        y="km_mean",
        padding=1,
        labels=True,
        percenteges=False,
    )
    fig.suptitle(
        "Średni dystans jednego dojazdu na praktyki",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"{_}_internship-transport-distance.png")
    if __name__ != "__main__":
        plt.show()

    internship_transport_distance_all = internship_transport_distance_all.join(
        internship_transport_distance_means.set_index("group"), rsuffix=f" {_}"
    )

    ## INTERNSHIPS MEANS OF TRANSPORT DATES
    internship_dates_distance = role.query("P16 == P16").reset_index(drop=True)
    n = internship_dates_distance.loc[:, "WAGA"].sum()

    internship_dates_distance.loc[:, "km"] = internship_dates_distance.loc[
        :, "WAGA"
    ].multiply(internship_dates_distance.loc[:, "P16"], axis=0)

    internship_dates_distance_means = (
        internship_dates_distance.groupby("P17")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P17": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P17"]})
    )
    internship_dates_distance_means["group"] = internship_dates_distance_means[
        "group"
    ].apply(lambda x: "\n".join(wrap(x, 30)) if isinstance(x, str) else x)
    fig = plot_barhplot(
        df=internship_dates_distance_means,
        x="group",
        y="km_mean",
        padding=1,
        labels=True,
        percenteges=False,
    )
    fig.suptitle(
        "Średni dystans jednego dojazdu na praktyki",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"{_}_internship-dates-distance.png")
    if __name__ != "__main__":
        plt.show()

    internship_dates_distance_all = internship_dates_distance_all.join(
        internship_dates_distance_means.set_index("group"), rsuffix=f" {_}"
    )
# %%
## INTERNSHIPS MEANS OF TRANSPORT DISTANCE
(
    internship_transport_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Główny środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P16_transport.xlsx", index=False)
)

# %%
## INTERNSHIPS MEANS OF TRANSPORT DATES
(
    internship_dates_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Data"})
    .fillna(0)
    .to_excel(EXCEL / "P16b_dates.xlsx", index=False)
)
