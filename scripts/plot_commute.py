# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.plots import plot_barhplot
import pandas as pd
from pejk.config import N_ALL, N_STUDENTS, N_TEACHERS, N_NON_TEACHERS

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
N_dct = {
    "all": N_ALL,
    "teacher": N_TEACHERS,
    "student": N_STUDENTS,
    "non_teacher": N_NON_TEACHERS,
}
# %%
## Summer commute trips dominant means of transport distance
summer_commute_distance = df.query("P3 == P3").reset_index(drop=True)
n = summer_commute_distance.loc[:, "WAGA"].sum()

summer_commute_distance.loc[:, "km"] = summer_commute_distance.loc[:, "WAGA"].multiply(
    summer_commute_distance.loc[:, "P6"], axis=0
)

summer_commute_distance_means = (
    summer_commute_distance.groupby("P8")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P8": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P8"]})
)
fig = plot_barhplot(
    df=summer_commute_distance_means,
    x="group",
    y="km_mean",
    padding=1,
    labels=True,
    percenteges=False,
)
fig.suptitle(
    "Średni tygodniowy dystans dojazdów",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "summer-commute-distance.png")
if __name__ != "__main__":
    plt.show()

summer_commute_distance_all = summer_commute_distance_means.set_index("group")
# %%
## Winter commute trips dominant means of transport distance
winter_commute_distance = df.query("P3 == P3").reset_index(drop=True)
n = winter_commute_distance.loc[:, "WAGA"].sum()

winter_commute_distance.loc[:, "km"] = winter_commute_distance.loc[:, "WAGA"].multiply(
    winter_commute_distance.loc[:, "P6"], axis=0
)

winter_commute_distance_means = (
    winter_commute_distance.groupby("P8b")[["km", "WAGA"]]
    .sum()
    .reset_index()
    .assign(km_mean=lambda x: x["km"] / x["WAGA"])
    .rename(columns={"P8b": "group"})
    .sort_values("km_mean")
    .replace({"group": mappings.variable_value_labels["P8b"]})
)
fig = plot_barhplot(
    df=winter_commute_distance_means,
    x="group",
    y="km_mean",
    padding=1,
    labels=True,
    percenteges=False,
)
fig.suptitle(
    "Średni tygodniowy dystans dojazdów",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "winter-commute-distance.png")
if __name__ != "__main__":
    plt.show()

winter_commute_distance_all = winter_commute_distance_means.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## SUMMER COMMUTE TRIPS DOMINANT MEANS OF TRANSPORT DISTANCE
    summer_commute_distance = role.query("P3 == P3").reset_index(drop=True)
    n = summer_commute_distance.loc[:, "WAGA"].sum()

    summer_commute_distance.loc[:, "km"] = summer_commute_distance.loc[
        :, "WAGA"
    ].multiply(summer_commute_distance.loc[:, "P6"], axis=0)

    summer_commute_distance_means = (
        summer_commute_distance.groupby("P8")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P8": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P8"]})
    )
    fig = plot_barhplot(
        df=summer_commute_distance_means,
        x="group",
        y="km_mean",
        padding=1,
        labels=True,
        percenteges=False,
    )
    fig.suptitle(
        "Średni tygodniowy dystans dojazdów",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"{_}_summer-commute-distance.png")
    if __name__ != "__main__":
        plt.show()

    summer_commute_distance_all = summer_commute_distance_all.join(
        summer_commute_distance_means.set_index("group"), rsuffix=f" {_}"
    )

    ## WINTER COMMUTE TRIPS DOMINANT MEANS OF TRANSPORT DISTANCE
    winter_commute_distance = role.query("P3 == P3").reset_index(drop=True)
    n = winter_commute_distance.loc[:, "WAGA"].sum()

    winter_commute_distance.loc[:, "km"] = winter_commute_distance.loc[
        :, "WAGA"
    ].multiply(winter_commute_distance.loc[:, "P6"], axis=0)

    winter_commute_distance_means = (
        winter_commute_distance.groupby("P8b")[["km", "WAGA"]]
        .sum()
        .reset_index()
        .assign(km_mean=lambda x: x["km"] / x["WAGA"])
        .rename(columns={"P8b": "group"})
        .sort_values("km_mean")
        .replace({"group": mappings.variable_value_labels["P8b"]})
    )
    fig = plot_barhplot(
        df=winter_commute_distance_means,
        x="group",
        y="km_mean",
        padding=1,
        labels=True,
        percenteges=False,
    )
    fig.suptitle(
        "Średni tygodniowy dystans dojazdów",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"{_}_winter-commute-distance.png")
    if __name__ != "__main__":
        plt.show()

    winter_commute_distance_all = winter_commute_distance_all.join(
        winter_commute_distance_means.set_index("group"), rsuffix=f" {_}"
    )
# %%
## SUMMER COMMUTE TRIPS DOMINANT MEANS OF TRANSPORT DISTANCE
(
    summer_commute_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Główny środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P6_summer.xlsx", index=False)
)
# %%
## WINTER COMMUTE TRIPS DOMINANT MEANS OF TRANSPORT DISTANCE
(
    winter_commute_distance_all.rename(
        columns=lambda x: x.replace("km_mean", "Średnia długość jednej podróży")
        .replace("km", "Suma długości podróży w próbie")
        .replace("WAGA", "Ważona liczebność")
    )
    .reset_index()
    .rename(columns={"group": "Główny środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P6b_winter.xlsx", index=False)
)
# %%
