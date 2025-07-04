# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import (
    prepare_data_rowise,
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
## Summer means of transport
lst = df.loc[:, "P7_1":"P7_14"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport = prepare_data_columnswise(
    df=df, f="P7_1", t="P7_14", mapping=mappings.column_names_to_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=transport,
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
fig.savefig(PNG / "per_transport-summer.png")
if __name__ != "__main__":
    plt.show()
summer_means_transport = transport.set_index("group")
# %%
## Winter means of transport
lst = df.loc[:, "P7b_1":"P7b_14"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport = prepare_data_columnswise(
    df=df, f="P7b_1", t="P7b_14", mapping=mappings.column_names_to_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=transport,
    x="group",
    y="count_population",
    padding=1,
    labels=False,
    percenteges=True,
)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_transport-winter.png")
if __name__ != "__main__":
    plt.show()

winter_means_transport = transport.set_index("group")
# %%
## Summer dominant means of transport
lst = ["P8"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport_dominant = prepare_data_rowise(
    df=df, key="P8", mapping=mappings.variable_value_labels, weight=True
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
    "Główny środek lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

summer_dominant_means_transport = transport_dominant.set_index("group")
# %%
## Winter dominant means of transport
lst = ["P8b"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport_dominant = prepare_data_rowise(
    df=df, key="P8b", mapping=mappings.variable_value_labels, weight=True
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
    "Główny środek lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

winter_dominant_means_transport = transport_dominant.set_index("group")
## %
for _, role in ndf.groupby("role"):
    ## SUMMER MEANS OF TRANSPORT

    lst = role.loc[:, "P7_1":"P7_14"].columns
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    transport = prepare_data_columnswise(
        df=role,
        f="P7_1",
        t="P7_14",
        mapping=mappings.column_names_to_labels,
        weight=True,
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=transport,
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
    fig.savefig(PNG / f"per_{_}_transport-summer.png")
    if __name__ != "__main__":
        plt.show()
    summer_means_transport = summer_means_transport.join(
        transport.set_index("group"), rsuffix=f" {_}"
    )

    ## WINTER MEANS OF TRANSPORT

    lst = role.loc[:, "P7b_1":"P7b_14"].columns
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    transport = prepare_data_columnswise(
        df=role,
        f="P7b_1",
        t="P7b_14",
        mapping=mappings.column_names_to_labels,
        weight=True,
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=transport,
        x="group",
        y="count_population",
        padding=1,
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rodzaje środków lokomocji (semestr zimowy)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_transport-winter.png")
    if __name__ != "__main__":
        plt.show()

    winter_means_transport = winter_means_transport.join(
        transport.set_index("group"), rsuffix=f" {_}"
    )

    ## SUMMER DOMINANT MEANS OF TRANSPORT

    lst = ["P8"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    transport_dominant = prepare_data_rowise(
        df=role, key="P8", mapping=mappings.variable_value_labels, weight=True
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
        "Główny środek lokomocji (semestr letni)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_transport-dominant-summer.png")
    if __name__ != "__main__":
        plt.show()
    summer_dominant_means_transport = summer_dominant_means_transport.join(
        transport_dominant.set_index("group"), rsuffix=f" {_}"
    )

    ## WINTER DOMINANT MEANS OF TRANSPORT

    lst = ["P8b"]
    n = (
        role.query(" or ".join([f"{item} == {item}" for item in lst]))
        .loc[:, "WAGA"]
        .sum()
    )
    transport_dominant = prepare_data_rowise(
        df=role, key="P8b", mapping=mappings.variable_value_labels, weight=True
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
        "Główny środek lokomocji (semestr zimowy)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_transport-dominant-winter.png")
    if __name__ != "__main__":
        plt.show()

    winter_dominant_means_transport = winter_dominant_means_transport.join(
        transport_dominant.set_index("group"), rsuffix=f" {_}"
    )
# %%
## SUMMER MEANS OF TRANSPORT
(
    summer_means_transport.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P7.xlsx", index=False)
)
# %%
## WINTER MEANS OF TRANSPORT
(
    winter_means_transport.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P7b.xlsx", index=False)
)
# %%
## SUMMER DOMINANT MEANS OF TRANSPORT
(
    summer_dominant_means_transport.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P8.xlsx", index=False)
)
# %%
## WINTER DOMINANT MEANS OF TRANSPORT
(
    winter_dominant_means_transport.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Środek transportu"})
    .fillna(0)
    .to_excel(EXCEL / "P8b.xlsx", index=False)
)
