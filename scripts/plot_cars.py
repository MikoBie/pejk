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

df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]

teachers = df.query("teachers > 0").reset_index(drop=True)
teachers.loc[:, "role"] = "teacher"
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)
non_teachers.loc[:, "role"] = "non_teacher"

PERCENT = 100

ndf = pd.concat([teachers, non_teachers])

# %%
## Using own car for work trips
lst = ["P27"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
cars = prepare_data_rowise(
    df=df, key="P27", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=cars,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Użycie własnego samochodu do podróży służbowych",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_cars.png")
if __name__ != "__main__":
    plt.show()
cars_all = cars.set_index("group")
# %%
## Type of engine
lst = ["P29"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
cars = prepare_data_rowise(
    df=df, key="P29", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=cars,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rodzaj silinika w samochodzie",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_type_cars.png")
if __name__ != "__main__":
    plt.show()
cars_engine_all = cars.set_index("group")
# %%
for _, role in ndf.groupby("role"):
    ## USING OWN CAR FOR WORK TRIPS
    lst = ["P27"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    cars = prepare_data_rowise(
        df=role, key="P27", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=cars,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Użycie własnego samochodu do podróży służbowych",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_cars.png")
    if __name__ != "__main__":
        plt.show()
    cars_all = cars_all.join(cars.set_index("group"), rsuffix=f" {_}")

    ## TYPE OF ENGINE
    lst = ["P29"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    cars = prepare_data_rowise(
        df=role, key="P29", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=cars,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rodzaj silinika w samochodzie",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_type_cars.png")
    if __name__ != "__main__":
        plt.show()
    cars_engine_all = cars_engine_all.join(cars.set_index("group"), rsuffix=f" {_}")
# %%
## USING OWN CAR FOR WORK TRIPS
(
    cars_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Użycie samochodu prywatnego do podróży służbowych"})
    .fillna(0)
    .to_excel(EXCEL / "P27.xlsx", index=False)
)
# %%
## TYPE OF ENGINE
(
    cars_engine_all.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Rodzaj slinika w samochodzie"})
    .fillna(0)
    .to_excel(EXCEL / "P29.xlsx", index=False)
)

# %%
