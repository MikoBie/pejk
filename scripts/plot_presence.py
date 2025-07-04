# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise
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
## Liczba dnia na UW
n = df.query("P4 == P4 or P4b == P4b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=df, key="P4", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=presence, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_weekly-presence-summer.png")
if __name__ != "__main__":
    plt.show()

presence_summer_weekly = presence.set_index("group")
# %%
n = df.query("P4b == P4b").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=df, key="P4b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=presence_monthly, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_monthly-presence-summer.png")
if __name__ != "__main__":
    plt.show()

presence_summer_monthly = presence_monthly.set_index("group")

# %%
n = df.query("P5 == P5 or P5b == P5b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=df, key="P5", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)

fig = plot_barhplot(
    df=presence, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_weekly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

presence_winter_weekly = presence.set_index("group")
# %%
n = df.query("P5b == P5b").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=df, key="P5b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=presence_monthly, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_monthly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

presence_winter_monthly = presence_monthly.set_index("group")

# %%
for _, role in ndf.groupby("role"):
    ## PRESENCE SUMMER WEEKLY

    n = role.query("P4 == P4 or P4b == P4b").loc[:, "WAGA"].sum()
    presence = prepare_data_rowise(
        df=role, key="P4", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=presence, x="group", y="count_population", labels=False, percenteges=True
    )
    fig.suptitle(
        "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr letni)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_weekly-presence-summer.png")
    if __name__ != "__main__":
        plt.show()

    presence_summer_weekly = presence_summer_weekly.join(
        presence.set_index("group"), rsuffix=f" {_}"
    )

    ## PRESENCE SUMMER MONTHLY

    n = role.query("P4b == P4b").loc[:, "WAGA"].sum()
    presence_monthly = prepare_data_rowise(
        df=role, key="P4b", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=presence_monthly,
        x="group",
        y="count_population",
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr letni)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_monthly-presence-summer.png")
    if __name__ != "__main__":
        plt.show()

    presence_summer_monthly = presence_summer_monthly.join(
        presence_monthly.set_index("group"), rsuffix=f" {_}"
    )

    ## PRESENCE WINTER WEEKLY

    n = role.query("P5 == P5 or P5b == P5b").loc[:, "WAGA"].sum()
    presence = prepare_data_rowise(
        df=role, key="P5", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=presence, x="group", y="count_population", labels=False, percenteges=True
    )
    fig.suptitle(
        "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr zimowy)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_weekly-presence-winter.png")
    if __name__ != "__main__":
        plt.show()

    presence_winter_weekly = presence_winter_weekly.join(
        presence.set_index("group"), rsuffix=f" {_}"
    )

    ## PRESENCE WINTER MONTHLY

    n = role.query("P5b == P5b").loc[:, "WAGA"].sum()
    presence_monthly = prepare_data_rowise(
        df=role, key="P5b", mapping=mappings.variable_value_labels, weight=True
    ).assign(count_population=lambda x: x["count"] * PERCENT / n)

    fig = plot_barhplot(
        df=presence_monthly,
        x="group",
        y="count_population",
        labels=False,
        percenteges=True,
    )
    fig.suptitle(
        "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr zimowy)",
        ha="center",
        fontsize=12,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(PNG / f"per_{_}_monthly-presence-winter.png")
    if __name__ != "__main__":
        plt.show()

    presence_winter_monthly = presence_winter_monthly.join(
        presence_monthly.set_index("group"), rsuffix=f" {_}"
    )

# %%
## PRESENCE SUMMER WEEKLY
(
    presence_summer_weekly.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba dni na UW"})
    .fillna(0)
    .to_excel(EXCEL / "P4.xlsx", index=False)
)
# %%
## PRESENCE SUMMER MONTHLY
(
    presence_summer_monthly.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba dni na UW"})
    .fillna(0)
    .to_excel(EXCEL / "P4b.xlsx", index=False)
)
# %%
## PRESENCE WINTER WEEKLY
(
    presence_winter_weekly.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba dni na UW"})
    .fillna(0)
    .to_excel(EXCEL / "P5.xlsx", index=False)
)
# %%
## PRESENCE WINTER MONTHLY
(
    presence_winter_monthly.rename(
        columns=lambda x: x.replace("count_population", "Procent").replace(
            "count", "Liczebność ważona"
        )
    )
    .reset_index()
    .rename(columns={"group": "Liczba dni na UW"})
    .fillna(0)
    .to_excel(EXCEL / "P5b.xlsx", index=False)
)

# %%
