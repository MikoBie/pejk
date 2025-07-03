# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise, prepare_data_columnswise
from pejk.plots import plot_barhplot, plot_barplot

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df = df.query("P4 < 8").query("P5 < 8")

df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]

students = df.query("students > 0").reset_index(drop=True)
teachers = df.query("teachers > 0").reset_index(drop=True)
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)

PERCENT = 100
# %%
## Popularność kampusów
lst = df.loc[:, "P2_1":"P2_12"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
campus = prepare_data_columnswise(
    df=df, f="P2_1", t="P2_12", weight=True, mapping=mappings.column_names_to_labels
).assign(count_population=lambda x: x["count"] * PERCENT / n)
fig = plot_barhplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle("Popularność kampusów", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "per_campus.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_campus.xlsx")
)
# %%
## Histogram kampusów
lst = df.loc[:, "P2_1":"P2_12"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
campus = (
    df.assign(n_campus=lambda x: df.loc[:, "P2_1":"P2_12"].sum(axis=1))
    .groupby("n_campus")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"n_campus": "group", "WAGA": "count"})
    .assign(count_population=lambda x: x["count"] * PERCENT / n)
)

fig = plot_barplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby odwiedzanych kampusów uniwersyteckich",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.axes[0].xaxis.set_ticks([item for item in range(12)])
fig.savefig(PNG / "per_campus_distribution.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Liczba odwiedzanych kampusów",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_campus-distribution.xlsx")
)
# %%
n = df.query("P3 == P3").loc[:, "WAGA"].sum()
dominant_campus = prepare_data_rowise(
    df=df, key="P3", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=dominant_campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Główne miejsce pracy/studiowania/kształcenia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_campus-dominant.png")
if __name__ != "__main__":
    plt.show()

(
    dominant_campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_campus-dominant.xlsx")
)

# %%
## STUDENTS
lst = students.loc[:, "P2_1":"P2_12"].columns
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
campus = prepare_data_columnswise(
    df=students,
    f="P2_1",
    t="P2_12",
    weight=True,
    mapping=mappings.column_names_to_labels,
).assign(count_population=lambda x: x["count"] * PERCENT / n)
fig = plot_barhplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle("Popularność kampusów", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "per_students-campus.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_students-campus.xlsx")
)
# %%
lst = students.loc[:, "P2_1":"P2_12"].columns
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
campus = (
    students.assign(n_campus=lambda x: students.loc[:, "P2_1":"P2_12"].sum(axis=1))
    .groupby("n_campus")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"n_campus": "group", "WAGA": "count"})
    .assign(count_population=lambda x: x["count"] * PERCENT / n)
)

fig = plot_barplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby odwiedzanych kampusów uniwersyteckich",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.axes[0].xaxis.set_ticks([item for item in range(12)])
fig.savefig(PNG / "per_students-campus_distribution.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Liczba odwiedzanych kampusów",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_students-campus-distribution.xlsx")
)
# %%
n = students.query("P3 == P3").loc[:, "WAGA"].sum()
dominant_campus = prepare_data_rowise(
    df=students, key="P3", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=dominant_campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Główne miejsce pracy/studiowania/kształcenia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_students-campus-dominant.png")
if __name__ != "__main__":
    plt.show()

(
    dominant_campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_students-campus-dominant.xlsx")
)
# %%
## TEACHERS
lst = teachers.loc[:, "P2_1":"P2_12"].columns
n = (
    teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
campus = prepare_data_columnswise(
    df=teachers,
    f="P2_1",
    t="P2_12",
    weight=True,
    mapping=mappings.column_names_to_labels,
).assign(count_population=lambda x: x["count"] * PERCENT / n)
fig = plot_barhplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle("Popularność kampusów", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "per_teachers-campus.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_teachers-campus.xlsx")
)
# %%
lst = teachers.loc[:, "P2_1":"P2_12"].columns
n = (
    teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
campus = (
    teachers.assign(n_campus=lambda x: teachers.loc[:, "P2_1":"P2_12"].sum(axis=1))
    .groupby("n_campus")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"n_campus": "group", "WAGA": "count"})
    .assign(count_population=lambda x: x["count"] * PERCENT / n)
)

fig = plot_barplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby odwiedzanych kampusów uniwersyteckich",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.axes[0].xaxis.set_ticks([item for item in range(12)])
fig.savefig(PNG / "per_teachers-campus_distribution.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Liczba odwiedzanych kampusów",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_teachers-campus-distribution.xlsx")
)
# %%
n = teachers.query("P3 == P3").loc[:, "WAGA"].sum()
dominant_campus = prepare_data_rowise(
    df=teachers, key="P3", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=dominant_campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Główne miejsce pracy/studiowania/kształcenia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_teachers-campus-dominant.png")
if __name__ != "__main__":
    plt.show()

(
    dominant_campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_teachers-campus-dominant.xlsx")
)
# %%
## NOPERCENT
lst = non_teachers.loc[:, "P2_1":"P2_12"].columns
n = (
    non_teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
campus = prepare_data_columnswise(
    df=non_teachers,
    f="P2_1",
    t="P2_12",
    weight=True,
    mapping=mappings.column_names_to_labels,
).assign(count_population=lambda x: x["count"] * PERCENT / n)
fig = plot_barhplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle("Popularność kampusów", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "per_non_teachers-campus.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_non_teachers-campus.xlsx")
)
# %%
lst = non_teachers.loc[:, "P2_1":"P2_12"].columns
n = (
    non_teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
campus = (
    non_teachers.assign(
        n_campus=lambda x: non_teachers.loc[:, "P2_1":"P2_12"].sum(axis=1)
    )
    .groupby("n_campus")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"n_campus": "group", "WAGA": "count"})
    .assign(count_population=lambda x: x["count"] * PERCENT / n)
)

fig = plot_barplot(
    df=campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Rozkład liczby odwiedzanych kampusów uniwersyteckich",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.axes[0].xaxis.set_ticks([item for item in range(12)])
fig.savefig(PNG / "per_non_teachers-campus_distribution.png")
if __name__ != "__main__":
    plt.show()

(
    campus.rename(
        columns={
            "group": "Liczba odwiedzanych kampusów",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_non_teachers-campus-distribution.xlsx")
)
# %%
n = non_teachers.query("P3 == P3").loc[:, "WAGA"].sum()
dominant_campus = prepare_data_rowise(
    df=non_teachers, key="P3", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * PERCENT / n)


fig = plot_barhplot(
    df=dominant_campus, x="group", y="count_population", labels=False, percenteges=True
)
fig.suptitle(
    "Główne miejsce pracy/studiowania/kształcenia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "per_non_teachers-campus-dominant.png")
if __name__ != "__main__":
    plt.show()

(
    dominant_campus.rename(
        columns={
            "group": "Kampus",
            "count": "Liczebność ważona",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_non_teachers-campus-dominant.xlsx")
)
