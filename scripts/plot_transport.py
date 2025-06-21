# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import (
    prepare_data_rowise,
    prepare_data_columnswise,
    prepare_comparison_data,
)
from pejk.plots import plot_barhplot
import numpy as np
from matplotlib import ticker

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
df["non_teachers"] = df.loc[:, "P1_7"]
df["teachers"] = df.loc[:, "P1_6"]

students = df.query("students > 0").reset_index(drop=True)
teachers = df.query("teachers > 0").reset_index(drop=True)
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)
# %%
counts, bins = np.histogram(
    df.query("P6 == P6").loc[:, "P6"], bins=[item for item in range(0, 451, 2)]
)

fig = plt.figure(figsize=(10, 8))
plt.bar(bins[:-1], counts[:], width=1.5)
fig.axes[0].xaxis.set_ticks([item for item in range(0, 451, 20)])

# %%
transport = prepare_data_columnswise(
    df=df, f="P7_1", t="P7_14", mapping=mappings.column_names_to_labels, weight=False
)
transport.to_excel(EXCEL / "transport-summer.xlsx")

fig = plot_barhplot(df=transport, x="group", y="count", padding=1)
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

# %%
transport = prepare_data_columnswise(
    df=df, f="P7_1", t="P7_14", mapping=mappings.column_names_to_labels, weight=True
)

transport.to_excel(EXCEL / "transport-summer-weighted.xlsx")
fig = plot_barhplot(df=transport, x="group", y="count", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-summer-weighted.png")
if __name__ != "__main__":
    plt.show()
# %%
transport = prepare_data_columnswise(
    df=df, f="P7b_1", t="P7b_14", mapping=mappings.column_names_to_labels, weight=False
)
transport.to_excel(EXCEL / "transport-winter.xlsx")

fig = plot_barhplot(df=transport, x="group", y="count", padding=1)
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

# %%
transport = prepare_data_columnswise(
    df=df, f="P7b_1", t="P7b_14", mapping=mappings.column_names_to_labels, weight=True
)
transport.to_excel(EXCEL / "transport-winter-weighted.xlsx")

fig = plot_barhplot(df=transport, x="group", y="count", padding=1)
fig.suptitle(
    "Rodzaje środków lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-winter-weighted.png")
if __name__ != "__main__":
    plt.show()

# %%
transport_dominant = prepare_data_rowise(
    df=df, key="P8", mapping=mappings.variable_value_labels, weight=True
)
transport.to_excel(EXCEL / "transport-dominat-summer-weighted.xlsx")

fig = plot_barhplot(df=transport_dominant, x="group", y="count", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr letni)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-dominant-summer-weighted.png")
if __name__ != "__main__":
    plt.show()

# %%
transport_dominant = prepare_data_rowise(
    df=df, key="P8", mapping=mappings.variable_value_labels, weight=False
)
transport.to_excel(EXCEL / "transport-dominat-summer.xlsx")

fig = plot_barhplot(df=transport_dominant, x="group", y="count", padding=1)
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
# %%
transport_dominant = prepare_data_rowise(
    df=df, key="P8b", mapping=mappings.variable_value_labels, weight=True
)
transport.to_excel(EXCEL / "transport-dominat-winter-weighted.xlsx")

fig = plot_barhplot(df=transport_dominant, x="group", y="count", padding=1)
fig.suptitle(
    "Główny środek lokomocji (semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "transport-dominant-winter-weighted.png")
if __name__ != "__main__":
    plt.show()

# %%
transport_dominant = prepare_data_rowise(
    df=df, key="P8b", mapping=mappings.variable_value_labels, weight=False
)
transport.to_excel(EXCEL / "transport-dominat-winter.xlsx")

fig = plot_barhplot(df=transport_dominant, x="group", y="count", padding=1)
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

# %%
students_transport_dominant_summer = prepare_data_rowise(
    df=students, key="P8", mapping=mappings.variable_value_labels, weight=True
)

students_transport_dominant_winter = prepare_data_rowise(
    df=students, key="P8b", mapping=mappings.variable_value_labels, weight=True
)

students_transport_compare = prepare_comparison_data(
    new=students_transport_dominant_summer, old=students_transport_dominant_winter
)

fig = plot_barhplot(df=students_transport_compare, x="group", y="count", labels=True)

fig.axes[0].xaxis.set_major_formatter(ticker.PercentFormatter())
fig.axes[0].bar_label(
    fig.axes[0].containers[0],
    fmt=lambda x: f"{int(round(x, 0))}%",
    padding=1,
)

fig.suptitle(
    "Porównanie głównego środka lokomocji osoby studenckie (semestr letni vs. semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "students-transport-dominant-compare.png")
if __name__ != "__main__":
    plt.show()


# %%

non_teachers_transport_dominant_summer = prepare_data_rowise(
    df=non_teachers, key="P8", mapping=mappings.variable_value_labels, weight=True
)

non_teachers_transport_dominant_winter = prepare_data_rowise(
    df=non_teachers, key="P8b", mapping=mappings.variable_value_labels, weight=True
)

non_teachers_transport_compare = prepare_comparison_data(
    new=non_teachers_transport_dominant_summer,
    old=non_teachers_transport_dominant_winter,
)

fig = plot_barhplot(
    df=non_teachers_transport_compare, x="group", y="count", labels=True
)

fig.axes[0].xaxis.set_major_formatter(ticker.PercentFormatter())
fig.axes[0].bar_label(
    fig.axes[0].containers[0],
    fmt=lambda x: f"{int(round(x, 0))}%",
    padding=1,
)

fig.suptitle(
    "Porównanie głównego środka lokomocji nie osoby nauczycielskie (semestr letni vs. semestr zimowy)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "non-teachers-transport-dominant-compare.png")
if __name__ != "__main__":
    plt.show()
# %%
