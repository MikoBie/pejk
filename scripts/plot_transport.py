# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import (
    prepare_data_rowise,
    prepare_data_columnswise,
)
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
lst = df.loc[:, "P7_1":"P7_14"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport = prepare_data_columnswise(
    df=df, f="P7_1", t="P7_14", mapping=mappings.column_names_to_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-summer.png")
if __name__ != "__main__":
    plt.show()
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "transport-summer.xlsx")
)

# %%
lst = df.loc[:, "P7b_1":"P7b_14"].columns
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport = prepare_data_columnswise(
    df=df, f="P7b_1", t="P7b_14", mapping=mappings.column_names_to_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "transport-winter.xlsx")
)
# %%
lst = ["P8"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport_dominant = prepare_data_rowise(
    df=df, key="P8", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "transport-dominat-summer.xlsx")
)
# %%
lst = ["P8b"]
n = df.query(" or ".join([f"{item} == {item}" for item in lst])).loc[:, "WAGA"].sum()
transport_dominant = prepare_data_rowise(
    df=df, key="P8b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_ALL / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "transport-dominat-winter.xlsx")
)
# %%
## Students
lst = students.loc[:, "P7_1":"P7_14"].columns
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport = prepare_data_columnswise(
    df=students,
    f="P7_1",
    t="P7_14",
    mapping=mappings.column_names_to_labels,
    weight=True,
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-transport-summer.png")
if __name__ != "__main__":
    plt.show()
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-transport-summer.xlsx")
)

# %%
lst = students.loc[:, "P7b_1":"P7b_14"].columns
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport = prepare_data_columnswise(
    df=students,
    f="P7b_1",
    t="P7b_14",
    mapping=mappings.column_names_to_labels,
    weight=True,
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-transport-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-transport-winter.xlsx")
)
# %%
lst = ["P8"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport_dominant = prepare_data_rowise(
    df=students, key="P8", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-transport-dominat-summer.xlsx")
)
# %%
lst = ["P8b"]
n = (
    students.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport_dominant = prepare_data_rowise(
    df=students, key="P8b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_STUDENTS / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students_transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "students-transport-dominat-winter.xlsx")
)
# %%
## Teachers
lst = teachers.loc[:, "P7_1":"P7_14"].columns
n = (
    teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport = prepare_data_columnswise(
    df=teachers,
    f="P7_1",
    t="P7_14",
    mapping=mappings.column_names_to_labels,
    weight=True,
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers-transport-summer.png")
if __name__ != "__main__":
    plt.show()
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-transport-summer.xlsx")
)

# %%
lst = teachers.loc[:, "P7b_1":"P7b_14"].columns
n = (
    teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport = prepare_data_columnswise(
    df=teachers,
    f="P7b_1",
    t="P7b_14",
    mapping=mappings.column_names_to_labels,
    weight=True,
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers-transport-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-transport-winter.xlsx")
)
# %%
lst = ["P8"]
n = (
    teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport_dominant = prepare_data_rowise(
    df=teachers, key="P8", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers-transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-transport-dominat-summer.xlsx")
)
# %%
lst = ["P8b"]
n = (
    teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport_dominant = prepare_data_rowise(
    df=teachers, key="P8b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_TEACHERS / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers_transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "teachers-transport-dominat-winter.xlsx")
)
# %%
## Teachers
lst = non_teachers.loc[:, "P7_1":"P7_14"].columns
n = (
    non_teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport = prepare_data_columnswise(
    df=non_teachers,
    f="P7_1",
    t="P7_14",
    mapping=mappings.column_names_to_labels,
    weight=True,
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers-transport-summer.png")
if __name__ != "__main__":
    plt.show()
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-transport-summer.xlsx")
)

# %%
lst = non_teachers.loc[:, "P7b_1":"P7b_14"].columns
n = (
    non_teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport = prepare_data_columnswise(
    df=non_teachers,
    f="P7b_1",
    t="P7b_14",
    mapping=mappings.column_names_to_labels,
    weight=True,
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)

fig = plot_barhplot(df=transport, x="group", y="count_population", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers-transport-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-transport-winter.xlsx")
)
# %%
lst = ["P8"]
n = (
    non_teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport_dominant = prepare_data_rowise(
    df=non_teachers, key="P8", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers-transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-transport-dominat-summer.xlsx")
)
# %%
lst = ["P8b"]
n = (
    non_teachers.query(" or ".join([f"{item} == {item}" for item in lst]))
    .loc[:, "WAGA"]
    .sum()
)
transport_dominant = prepare_data_rowise(
    df=non_teachers, key="P8b", mapping=mappings.variable_value_labels, weight=True
).assign(count_population=lambda x: x["count"] * N_NON_TEACHERS / n)

fig = plot_barhplot(df=transport_dominant, x="group", y="count_population", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non_teachers_transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Liczebność populacja",
        }
    ).to_excel(EXCEL / "non_teachers-transport-dominat-winter.xlsx")
)
