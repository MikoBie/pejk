# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise, prepare_data_columnswise
from pejk.plots import plot_barhplot
import numpy as np

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

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
