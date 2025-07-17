# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import (
    prepare_data_rowise,
)
from pejk.plots import plot_barhplot
import pandas as pd

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["bachelors"] = df.loc[:, "P1_1"]
df["masters"] = df.loc[:, "P1_2"]
df["five_years"] = df.loc[:, "P1_3"]
df["postgraduate"] = df.loc[:, "P1_5"]
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
# %%
## Means of transport distribution of internships outside Warsaw
lst = ["P18"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
camps = prepare_data_rowise(
    df=students, key="P18", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=camps,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Środek dojazdu na praktyki/obozy poza Warszawą",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_camps-transport.png")
if __name__ != "__main__":
    plt.show()
camps_transport_all = camps.set_index("group")
# %%
## Dates of internships outside Warsaw
lst = ["P20"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
camps = prepare_data_rowise(
    df=students, key="P20", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=camps,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Termin praktyk/obozów poza Warszawą",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internhip-date.png")
if __name__ != "__main__":
    plt.show()
camps_dates_all = camps.set_index("group")

# %%
## Days distribution of campss outside Warsaw
lst = ["P21"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
camps = prepare_data_rowise(
    df=students, key="P21", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=camps,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rozkład liczby dni praktyk poza Warszawą",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internhip-days-distribution.png")
if __name__ != "__main__":
    plt.show()
camps_days_distribution_all = camps.set_index("group")
# %%
## Weeks distribution of campss outside Warsaw
lst = ["P21b"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
camps = prepare_data_rowise(
    df=students, key="P21b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=camps,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rozkład tygodni praktyk/obozów poza Warszawą",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internhip-weeks-distribution.png")
if __name__ != "__main__":
    plt.show()
camps_weeks_distribution_all = camps.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## MEANS OF TRANSPORT DISTRIBUTION OF INTERNSHIPS OUTSIDE WARSAW
    lst = ["P18"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    camps = prepare_data_rowise(
        df=role, key="P18", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=camps,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Środek dojazdu na praktyki/obozy poza Warszawą",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_camps-transport.png")
    if __name__ != "__main__":
        plt.show()
    camps_transport_all = camps_transport_all.join(
        camps.set_index("group"), rsuffix=f" {_}"
    )

    ## DATES OF INTERNSHIPS OUTSIDE WARSAW
    lst = ["P20"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    camps = prepare_data_rowise(
        df=role, key="P20", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=camps,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Termin praktyk/obozów poza Warszawą",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internhip-date.png")
    if __name__ != "__main__":
        plt.show()
    camps_dates_all = camps_dates_all.join(camps.set_index("group"), rsuffix=f" {_}")

    ## DAYS DISTRIBUTION OF CAMPSS OUTSIDE WARSAW
    lst = ["P21"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    camps = prepare_data_rowise(
        df=role, key="P21", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=camps,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rozkład liczby dni praktyk poza Warszawą",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internhip-days-distribution.png")
    if __name__ != "__main__":
        plt.show()
    camps_days_distribution_all = camps_days_distribution_all.join(
        camps.set_index("group"), rsuffix=f" {_}"
    )

    ## WEEKS DISTRIBUTION OF CAMPSS OUTSIDE WARSAW
    lst = ["P21b"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    camps = prepare_data_rowise(
        df=role, key="P21b", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=camps,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rozkład tygodni praktyk/obozów poza Warszawą",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internhip-weeks-distribution.png")
    if __name__ != "__main__":
        plt.show()
    camps_weeks_distribution_all = camps_weeks_distribution_all.join(
        camps.set_index("group"), rsuffix=f" {_}"
    )


# %%
## MEANS OF TRANSPORT DISTRIBUTION OF INTERNSHIPS OUTSIDE WARSAW
(
    camps_transport_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Rodzaj środka transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P18.xlsx", index=False)
)
# %%
## DATES OF INTERNSHIPS OUTSIDE WARSAW
(
    camps_dates_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Data"})
    .fillna(0)
    .to_excel(EXCEL / "P20.xlsx", index=False)
)
# %%
## DAYS DISTRIBUTION OF INTERNSHIPS OUTSIDE WARSAW
(
    camps_days_distribution_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba dni udziału w praktykach/obozach poza Warszawą"})
    .fillna(0)
    .to_excel(EXCEL / "P21.xlsx", index=False)
)
# %%
## WEEKS DISTRIBUTION OF INTERNSHIPS OUTSIDE WARSAW
(
    camps_weeks_distribution_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(
        columns={"group": "Liczba tygodni udziału w praktykach/obozach poza Warszawą"}
    )
    .fillna(0)
    .to_excel(EXCEL / "P21b.xlsx", index=False)
)
# %%
