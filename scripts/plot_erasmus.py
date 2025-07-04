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
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]

students = df.query("students > 0").reset_index(drop=True)
students.loc[:, "role"] = "student"
teachers = df.query("teachers > 0").reset_index(drop=True)
teachers.loc[:, "role"] = "teacher"
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)
non_teachers.loc[:, "role"] = "non_teacher"

PERCENT = 100

ndf = pd.concat([students, teachers, non_teachers])

# %%
## Participation in erasmus
lst = ["P22"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
erasmus = prepare_data_rowise(
    df=df, key="P22", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=erasmus,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Udział w Erasmusie w 2024",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_erasmus.png")
if __name__ != "__main__":
    plt.show()
erasmus_all = erasmus.set_index("group")
# %%
## Means of transport distribution to Erasmus
lst = ["P23"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
erasmus = prepare_data_rowise(
    df=df, key="P23", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=erasmus,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Środek dojazdu na Erasmusa",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_erasmus-transport.png")
if __name__ != "__main__":
    plt.show()
erasmus_transport_all = erasmus.set_index("group")
# %%
## Days distribution of erasmus
lst = ["P26"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
erasmus = prepare_data_rowise(
    df=df, key="P26", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=erasmus,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rozkład liczby dni na Erasmusie",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_erasmus-days-distribution.png")
if __name__ != "__main__":
    plt.show()
erasmus_days_distribution_all = erasmus.set_index("group")
# %%
## Dates of erasmus
lst = ["P25"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
erasmus = prepare_data_rowise(
    df=df, key="P25", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=erasmus,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Termin Erasmusa",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_erasmus-date.png")
if __name__ != "__main__":
    plt.show()
erasmus_dates_all = erasmus.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## PARTICIPATION IN ERASMUS
    lst = ["P22"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    erasmus = prepare_data_rowise(
        df=role, key="P22", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=erasmus,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Udział w Erasmusie w 2024",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_erasmus.png")
    if __name__ != "__main__":
        plt.show()
    erasmus_all = erasmus_all.join(erasmus.set_index("group"), rsuffix=f" {_}")
    ## MEANS OF TRANSPORT DISTRIBUTION TO ERASMUS
    lst = ["P23"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    erasmus = prepare_data_rowise(
        df=role, key="P23", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=erasmus,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Środek dojazdu na Erasmusa",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_erasmus-transport.png")
    if __name__ != "__main__":
        plt.show()
    erasmus_transport_all = erasmus_transport_all.join(
        erasmus.set_index("group"), rsuffix=f" {_}"
    )

    ## DAYS DISTRIBUTION OF ERASMUS
    lst = ["P26"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    erasmus = prepare_data_rowise(
        df=role, key="P26", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=erasmus,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rozkład liczby dni na Erasmusie",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_erasmus-days-distribution.png")
    if __name__ != "__main__":
        plt.show()
    erasmus_days_distribution_all = erasmus_days_distribution_all.join(
        erasmus.set_index("group"), rsuffix=f" {_}"
    )

    ## DATES OF ERASMUS
    lst = ["P25"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    erasmus = prepare_data_rowise(
        df=role, key="P25", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=erasmus,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Termin Erasmusa",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_erasmus-date.png")
    if __name__ != "__main__":
        plt.show()
    erasmus_dates_all = erasmus_dates_all.join(
        erasmus.set_index("group"), rsuffix=f" {_}"
    )

# %%
## PARTICIPATION IN ERASMUS
(
    erasmus_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Udział w Erasmusie"})
    .fillna(0)
    .to_excel(EXCEL / "P22.xlsx", index=False)
)

# %%
## MEANS OF TRANSPORT FOR ERASMUS
(
    erasmus_transport_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Rodzaj środka transportu na Erasmusa"})
    .fillna(0)
    .to_excel(EXCEL / "P23.xlsx", index=False)
)
# %%
## DATES OF ERASMUS
(
    erasmus_dates_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Data"})
    .fillna(0)
    .to_excel(EXCEL / "P25.xlsx", index=False)
)
# %%
## DAYS DISTRIBUTION OF INTERNSHIPS IN WARSAW
(
    erasmus_days_distribution_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba dni udziału w Erasmusie"})
    .fillna(0)
    .to_excel(EXCEL / "P26.xlsx", index=False)
)

# %%
