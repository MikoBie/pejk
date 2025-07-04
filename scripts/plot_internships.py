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
# %%
## Participation in internships
lst = ["P12"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
internship = prepare_data_rowise(
    df=students, key="P12", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=internship,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Udział w praktykach w 2024",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internship.png")
if __name__ != "__main__":
    plt.show()
internship_all = internship.set_index("group")

# %%
## Place of internships
lst = ["P13"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
internship = prepare_data_rowise(
    df=students, key="P13", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=internship,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Miejsce praktyk",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internship-place.png")
if __name__ != "__main__":
    plt.show()
internship_place_all = internship.set_index("group")
# %%
## Days distribution of internships in Warsaw
lst = ["P14"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
internship = prepare_data_rowise(
    df=students, key="P14", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=internship,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rozkład liczby dni praktyk w Warszawie",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internship-days-distribution.png")
if __name__ != "__main__":
    plt.show()
internship_days_distribution_all = internship.set_index("group")
# %%
## Weeks distribution of internships in Warsaw
lst = ["P14b"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
internship = prepare_data_rowise(
    df=students, key="P14b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=internship,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rozkład tygodni praktyk w Warszawie",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internship-weeks-distribution.png")
if __name__ != "__main__":
    plt.show()
internship_weeks_distribution_all = internship.set_index("group")
# %%
## Means of transport distribution of internships in Warsaw
lst = ["P15"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
internship = prepare_data_rowise(
    df=students, key="P15", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=internship,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Środek dojazdu na praktyki w Warszawie",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internship-transport.png")
if __name__ != "__main__":
    plt.show()
internship_transport_all = internship.set_index("group")
# %%
## Dates of internships in Warsaw
lst = ["P17"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
internship = prepare_data_rowise(
    df=students, key="P17", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=internship,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Termin praktyk w Warszawie",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_internship-date.png")
if __name__ != "__main__":
    plt.show()
internship_dates_all = internship.set_index("group")

# %%
for _, role in ndf.groupby("role"):
    ## PARTICIPATION IN INTERNSHIPS
    lst = ["P12"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    internship = prepare_data_rowise(
        df=role, key="P12", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=internship,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Udział w praktykach w 2024",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internship.png")
    if __name__ != "__main__":
        plt.show()
    internship_all = internship_all.join(internship.set_index("group"), rsuffix=f" {_}")

    ## PLACE OF INTERNSHIPS
    lst = ["P13"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    internship = prepare_data_rowise(
        df=role, key="P13", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=internship,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Miejsce praktyk",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internship-place.png")
    if __name__ != "__main__":
        plt.show()
    internship_place_all = internship_place_all.join(
        internship.set_index("group"), rsuffix=f" {_}"
    )

    ## DAYS DISTRIBUTION OF INTERNSHIPS IN wARSAW
    lst = ["P14"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    internship = prepare_data_rowise(
        df=role, key="P14", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=internship,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rozkład liczby dni praktyk w Warszawie",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / "per_{_}_internship-days-distribution.png")
    if __name__ != "__main__":
        plt.show()
    internship_days_distribution_all = internship_days_distribution_all.join(
        internship.set_index("group"), rsuffix=f" {_}"
    )

    ## WEEKS DISTRIBUTION OF INTERNSHIPS IN WARSAW
    lst = ["P14b"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    internship = prepare_data_rowise(
        df=role, key="P14b", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=internship,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Tygodnie praktyk w Warszawie",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internship-weeks-distribution.png")
    if __name__ != "__main__":
        plt.show()
    internship_weeks_distribution_all = internship_weeks_distribution_all.join(
        internship.set_index("group"), rsuffix=f" {_}"
    )

    ## MEANS OF TRANSPORT DISTRIBUTION OF INTERNSHIPS IN WARSAW
    lst = ["P15"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    internship = prepare_data_rowise(
        df=role, key="P15", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=internship,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Środek dojazdu na praktyki w Warszawie",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internship-transport.png")
    if __name__ != "__main__":
        plt.show()
    internship_transport_all = internship_transport_all.join(
        internship.set_index("group"), rsuffix=f" {_}"
    )

    ## DATES OF INTERNSHIPS IN WARSAW
    lst = ["P17"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    internship = prepare_data_rowise(
        df=role, key="P17", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=internship,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Termin praktyk w Warszawie",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_internship-date.png")
    if __name__ != "__main__":
        plt.show()
    internship_dates_all = internship_dates_all.join(
        internship.set_index("group"), rsuffix=f" {_}"
    )
# %%
## PARTICIPATION IN INTERNSHIPS
(
    internship_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Udział w praktykach"})
    .fillna(0)
    .to_excel(EXCEL / "P12.xlsx", index=False)
)

# %%
## PLACE OF INTERNSHIPS
(
    internship_place_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Miejsce praktyk"})
    .fillna(0)
    .to_excel(EXCEL / "P13.xlsx", index=False)
)
# %%
## DAYS DISTRIBUTION OF INTERNSHIPS IN WARSAW
(
    internship_days_distribution_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba dni udziału w praktykach w Warszawie"})
    .fillna(0)
    .to_excel(EXCEL / "P14.xlsx", index=False)
)
# %%
## WEEKS DISTRIBUTION OF INTERNSHIPS IN WARSAW
(
    internship_weeks_distribution_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba tygodni udziału w praktykach w Warszawie"})
    .fillna(0)
    .to_excel(EXCEL / "P14b.xlsx", index=False)
)
# %%
## MEANS OF TRANSPORT DISTRIBUTION OF INTERNSHIPS IN WARSAW
(
    internship_transport_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Rodzaj środka transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P15.xlsx", index=False)
)
# %%
## DATES OF INTERNSHIPS IN WARSAW
(
    internship_dates_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Data"})
    .fillna(0)
    .to_excel(EXCEL / "P17.xlsx", index=False)
)
# %%
