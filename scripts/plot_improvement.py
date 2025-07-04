# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import (
    prepare_data_columnswise,
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
## Infrastructure improvements
lst = df.loc[:, "P30_1":"P30_7"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
infra = prepare_data_columnswise(
    df=df, f="P30_1", t="P30_7", mapping=mappings.column_names_to_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=infra,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_improvement.png")
if __name__ != "__main__":
    plt.show()
infrastructure = infra.set_index("group")

# %%
for _, role in ndf.groupby("role"):
    ## INFRASTRUCTURE IMPROVEMENTS
    lst = role.loc[:, "P30_1":"P30_7"].columns
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    infra = prepare_data_columnswise(
        df=role,
        f="P30_1",
        t="P30_7",
        mapping=mappings.column_names_to_labels,
        weight=True,
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=infra,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rodzaje środków lokomocji (semestr letni)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_improvement.png")
    if __name__ != "__main__":
        plt.show()
    infrastructure = infrastructure.join(infra.set_index("group"), rsuffix=f" {_}")

# %%
## INFRASTRUCTURE IMPROVEMENTS
(
    infrastructure.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Ulepszenia"})
    .fillna(0)
    .to_excel(EXCEL / "P30.xlsx", index=False)
)
# %%
