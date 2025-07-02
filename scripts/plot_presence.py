# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise
from pejk.plots import plot_barhplot
from pejk.config import N_ALL, N_STUDENTS, N_TEACHERS, N_NON_TEACHERS

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]

students = df.query("students > 0").reset_index(drop=True)
teachers = df.query("teachers > 0").reset_index(drop=True)
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)

# %%
## All
n = df.query("P4 == P4 or P4b == P4b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=df, key="P4", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)


fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "weekly-presence-summer.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "weekly-presence-summer.xlsx")
)
# %%
n = df.query("P4b == P4b or P4 == P4").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=df, key="P4b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "monthly-presence-summer.png")
if __name__ != "__main__":
    plt.show()
(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "monthly-presence-summer.xlsx")
)

# %%
n = df.query("P5 == P5 or P5b == P5b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=df, key="P5", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)

fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "weekly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "weekly-presence-winter.xlsx")
)

# %%
n = df.query("P5b == P5b or P5 == P5").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=df, key="P5b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "monthly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "monthly-presence-winter.xlsx")
)
# %%
## STUDENTS
n = students.query("P4 == P4 or P4b == P4b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=students, key="P4", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)


fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-weekly-presence-summer.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-weekly-presence-summer.xlsx")
)
# %%
n = students.query("P4b == P4b or P4 == P4").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=students, key="P4b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-monthly-presence-summer.png")
if __name__ != "__main__":
    plt.show()
(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-monthly-presence-summer.xlsx")
)

# %%
n = students.query("P5 == P5 or P5b == P5b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=students, key="P5", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)

fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-weekly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-weekly-presence-winter.xlsx")
)

# %%
n = students.query("P5b == P5b or P5 == P5").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=students, key="P5b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-monthly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-monthly-presence-winter.xlsx")
)
# %%
## TEACHERS
n = teachers.query("P4 == P4 or P4b == P4b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=teachers, key="P4", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)


fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers-weekly-presence-summer.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-weekly-presence-summer.xlsx")
)
# %%
n = teachers.query("P4b == P4b or P4 == P4").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=teachers, key="P4b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers-monthly-presence-summer.png")
if __name__ != "__main__":
    plt.show()
(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-monthly-presence-summer.xlsx")
)

# %%
n = teachers.query("P5 == P5 or P5b == P5b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=teachers, key="P5", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)

fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers-weekly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-weekly-presence-winter.xlsx")
)

# %%
n = teachers.query("P5b == P5b or P5 == P5").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=teachers, key="P5b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers-monthly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-monthly-presence-winter.xlsx")
)
# %%
## NON-TEACHERS
n = non_teachers.query("P4 == P4 or P4b == P4b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=non_teachers, key="P4", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)


fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers-weekly-presence-summer.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-weekly-presence-summer.xlsx")
)
# %%
n = non_teachers.query("P4b == P4b or P4 == P4").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=non_teachers, key="P4b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers-monthly-presence-summer.png")
if __name__ != "__main__":
    plt.show()
(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-monthly-presence-summer.xlsx")
)

# %%
n = non_teachers.query("P5 == P5 or P5b == P5b").loc[:, "WAGA"].sum()
presence = prepare_data_rowise(
    df=non_teachers, key="P5", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)

fig = plot_barhplot(df=presence, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w tygodniu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers-weekly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence.rename(
        columns={
            "group": "Liczba dni w tygodniu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-weekly-presence-winter.xlsx")
)

# %%
n = non_teachers.query("P5b == P5b or P5 == P5").loc[:, "WAGA"].sum()
presence_monthly = prepare_data_rowise(
    df=non_teachers, key="P5b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)


fig = plot_barhplot(df=presence_monthly, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rozkład liczby dni na uniwersytecie (w miesiącu; semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers-monthly-presence-winter.png")
if __name__ != "__main__":
    plt.show()

(
    presence_monthly.rename(
        columns={
            "group": "Liczba dni w miesiącu",
            "count": "Liczebność ważona",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-monthly-presence-winter.xlsx")
)
