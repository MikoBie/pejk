# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import (
    prepare_data_rowise,
    prepare_data_columnswise,
)
from pejk.plots import plot_barhplot

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]

students = df.query("students > 0").reset_index(drop=True)
teachers = df.query("teachers > 0").reset_index(drop=True)
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)
PERCENT = 100

# %%
## All
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
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_transport-summer.xlsx")
)

# %%
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

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_transport-winter.xlsx")
)
# %%
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

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_transport-dominat-summer.xlsx")
)
# %%
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

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_transport-dominat-winter.xlsx")
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
fig.savefig(PNG / "per_students-transport-summer.png")
if __name__ != "__main__":
    plt.show()
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_students-transport-summer.xlsx")
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
fig.savefig(PNG / "per_students-transport-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_students-transport-winter.xlsx")
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
fig.savefig(PNG / "per_students-transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_students-transport-dominat-summer.xlsx")
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
fig.savefig(PNG / "per_students_transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_students-transport-dominat-winter.xlsx")
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
fig.savefig(PNG / "per_teachers-transport-summer.png")
if __name__ != "__main__":
    plt.show()
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_teachers-transport-summer.xlsx")
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
fig.savefig(PNG / "per_teachers-transport-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_teachers-transport-winter.xlsx")
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
fig.savefig(PNG / "per_teachers-transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_teachers-transport-dominat-summer.xlsx")
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
fig.savefig(PNG / "per_teachers_transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_teachers-transport-dominat-winter.xlsx")
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
fig.savefig(PNG / "per_non_teachers-transport-summer.png")
if __name__ != "__main__":
    plt.show()
(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_non_teachers-transport-summer.xlsx")
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
fig.savefig(PNG / "per_non_teachers-transport-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_non_teachers-transport-winter.xlsx")
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
fig.savefig(PNG / "per_non_teachers-transport-dominant-summer.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_non_teachers-transport-dominat-summer.xlsx")
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
fig.savefig(PNG / "per_non_teachers_transport-dominant-winter.png")
if __name__ != "__main__":
    plt.show()

(
    transport_dominant.rename(
        columns={
            "group": "Rodzaj transportu",
            "count": "Liczebność ważona (próba)",
            "count_population": "Procent",
        }
    ).to_excel(EXCEL / "per_non_teachers-transport-dominat-winter.xlsx")
)

# %%
