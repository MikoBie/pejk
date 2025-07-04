# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.plots import plot_barhplot
import pandas as pd
from textwrap import wrap

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]

students = df.query("students > 0").reset_index(drop=True)
students.loc[:, "role"] = "student"
teachers = (
    df.query("teachers > 0").query("P11 != 97 and P9 != 23").reset_index(drop=True)
)
teachers.loc[:, "role"] = "teacher"
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)
non_teachers.loc[:, "role"] = "non_teacher"


ndf = pd.concat([students, teachers, non_teachers])
# %%
## Erasmus means of transport distance
erasmus_transport_distance = students.query("P24 == P24").reset_index(drop=True)
n = erasmus_transport_distance.loc[:, "WAGA"].sum()

erasmus_transport_distance.loc[:, "km"] = erasmus_transport_distance.loc[
    :, "WAGA"
].multiply(erasmus_transport_distance.loc[:, "P24"], axis=0)

erasmus_transport_distance_means = (
    erasmus_transport_distance.groupby("P23")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P23": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P23"]})
)
fig = plot_barhplot(
    df=erasmus_transport_distance_means,
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
fig.savefig(PNG / "erasmus-transport-distance.png")
if __name__ != "__main__":
    plt.show()

erasmus_transport_distance_all = erasmus_transport_distance_means.set_index("group")
# %%
## Erasmus means of transport dates
erasmus_dates_distance = students.query("P24 == P24").reset_index(drop=True)
n = erasmus_dates_distance.loc[:, "WAGA"].sum()

erasmus_dates_distance.loc[:, "km"] = erasmus_dates_distance.loc[:, "WAGA"].multiply(
    erasmus_dates_distance.loc[:, "P24"], axis=0
)

erasmus_dates_distance_means = (
    erasmus_dates_distance.groupby("P25")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P25": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P25"]})
)
erasmus_dates_distance_means["group"] = erasmus_dates_distance_means["group"].apply(
    lambda x: "\n".join(wrap(x, 30)) if isinstance(x, str) else x
)
fig = plot_barhplot(
    df=erasmus_dates_distance_means,
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
fig.savefig(PNG / "erasmus-dates-distance.png")
if __name__ != "__main__":
    plt.show()

erasmus_dates_distance_all = erasmus_dates_distance_means.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## ERASMUS MEANS OF TRANSPORT DISTANCE
    erasmus_transport_distance = role.query("P24 == P24").reset_index(drop=True)
    n = erasmus_transport_distance.loc[:, "WAGA"].sum()

    erasmus_transport_distance.loc[:, "km"] = erasmus_transport_distance.loc[
        :, "WAGA"
    ].multiply(erasmus_transport_distance.loc[:, "P24"], axis=0)

    erasmus_transport_distance_means = (
        erasmus_transport_distance.groupby("P23")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P23": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P23"]})
    )
    fig = plot_barhplot(
        df=erasmus_transport_distance_means,
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
    fig.savefig(PNG / f"{_}_erasmus-transport-distance.png")
    if __name__ != "__main__":
        plt.show()

    erasmus_transport_distance_all = erasmus_transport_distance_all.join(
        erasmus_transport_distance_means.set_index("group"), rsuffix=f" {_}"
    )

    ## ERASMUS MEANS OF TRANSPORT DATES
    erasmus_dates_distance = role.query("P24 == P24").reset_index(drop=True)
    n = erasmus_dates_distance.loc[:, "WAGA"].sum()

    erasmus_dates_distance.loc[:, "km"] = erasmus_dates_distance.loc[
        :, "WAGA"
    ].multiply(erasmus_dates_distance.loc[:, "P24"], axis=0)

    erasmus_dates_distance_means = (
        erasmus_dates_distance.groupby("P25")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P25": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P25"]})
    )
    erasmus_dates_distance_means["group"] = erasmus_dates_distance_means["group"].apply(
        lambda x: "\n".join(wrap(x, 30)) if isinstance(x, str) else x
    )
    fig = plot_barhplot(
        df=erasmus_dates_distance_means,
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
    fig.savefig(PNG / f"{_}_erasmus-dates-distance.png")
    if __name__ != "__main__":
        plt.show()

    erasmus_dates_distance_all = erasmus_dates_distance_all.join(
        erasmus_dates_distance_means.set_index("group"), rsuffix=f" {_}"
    )
# %%
## ERASMUS MEANS OF TRANSPORT DISTANCE
(
    erasmus_transport_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Główny środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P24_transport.xlsx", index=False)
)

# %%
## ERASMUS MEANS OF TRANSPORT DATES
(
    erasmus_dates_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Data"})
    .fillna(0)
    .to_excel(EXCEL / "P24b_dates.xlsx", index=False)
)

# %%
