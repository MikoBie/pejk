# %%
import pyreadstat
from pejk import RAW, PNG, EXCEL
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_rowise
from pejk.plots import plot_barhplot

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
presence = prepare_data_rowise(df=df, key="P4", mapping=mappings.variable_value_labels)
presence.to_excel(EXCEL / "weekly-presence-summer.xlsx")


fig = plot_barhplot(df=presence, x="group", y="count", padding=1)
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

# %%
presence_monthly = prepare_data_rowise(
    df=df, key="P4b", mapping=mappings.variable_value_labels
)

presence.to_excel(EXCEL / "monthly-presence-summer.xlsx")

fig = plot_barhplot(df=presence_monthly, x="group", y="count", padding=1)
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

# %%
presence = prepare_data_rowise(df=df, key="P5", mapping=mappings.variable_value_labels)


presence.to_excel(EXCEL / "weekly-presence-winter.xlsx")
fig = plot_barhplot(df=presence, x="group", y="count", padding=1)
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

# %%
presence_monthly = prepare_data_rowise(
    df=df, key="P5b", mapping=mappings.variable_value_labels
)

presence.to_excel(EXCEL / "monthly-presence-winter.xlsx")

fig = plot_barhplot(df=presence_monthly, x="group", y="count", padding=1)
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
