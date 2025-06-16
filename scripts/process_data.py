# %%
import pyreadstat
from pejk import RAW, PNG
from pejk.config import COLORS, JEDNOSTKI
import matplotlib.pyplot as plt
from pejk.utils import prepare_data_barplots

## plt.rc("figure.suptitle", horizontalalignment = "center")
# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
# %%
## Liczebność grup
groups = prepare_data_barplots(
    df=df, f="P1_1", t="P1_7", mapping=mappings.column_names_to_labels
)
fig = plt.figure(figsize=(10, 8))
plt.barh(groups["group"].tolist(), groups["count"].tolist(), color=COLORS["dark blue"])
fig.suptitle(
    "Liczebności w poszczególnych grupach", ha="center", fontsize=12, weight="bold"
)
fig.tight_layout()
fig.savefig(PNG / "groups.png")
if __name__ != "__main__":
    plt.show()

# %%
## Studia pierwszego stopnia
studies = prepare_data_barplots(
    df=df, f="P33a_1", t="P33a_27", mapping=mappings.column_names_to_labels
)

fig = plt.figure(figsize=(10, 8))
plt.barh(
    studies["group"].tolist(), studies["count"].tolist(), color=COLORS["dark blue"]
)
fig.suptitle(
    "Jednostki osób studenckich studiów I stopnia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "bachelor.png")
if __name__ != "__main__":
    plt.show()

# %%
## Studia drugiego stopnia
studies = prepare_data_barplots(
    df=df, f="P33b_1", t="P33b_27", mapping=mappings.column_names_to_labels
)

fig = plt.figure(figsize=(10, 8))
plt.barh(
    studies["group"].tolist(), studies["count"].tolist(), color=COLORS["dark blue"]
)
fig.suptitle(
    "Jednostki osób studenckich studiów II stopnia",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "masters.png")
if __name__ != "__main__":
    plt.show()
# %%
## Studia jednolite
studies = prepare_data_barplots(
    df=df, f="P33c_1", t="P33c_5", mapping=mappings.column_names_to_labels
)


fig = plt.figure(figsize=(10, 8))
plt.barh(
    studies["group"].tolist(), studies["count"].tolist(), color=COLORS["dark blue"]
)
fig.suptitle(
    "Jednostki osób studenckich studiów jednolitych",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "masters-five-years.png")
if __name__ != "__main__":
    plt.show()

# %%
## Studia podyplomowe
studies = prepare_data_barplots(
    df=df, f="P33e_1", t="P33e_18", mapping=mappings.column_names_to_labels
).query("count > 0")


fig = plt.figure(figsize=(10, 8))
plt.barh(
    studies["group"].tolist(), studies["count"].tolist(), color=COLORS["dark blue"]
)
fig.suptitle(
    "Jednostki osób studenckich studiów podyplomowych",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "postgraduate.png")
if __name__ != "__main__":
    plt.show()
# %%
## Nauczyciele i nauczycielki akademiccy
studies = prepare_data_barplots(
    df=df, f="P33f_1", t="P33f_18", mapping=mappings.column_names_to_labels
)

fig = plt.figure(figsize=(10, 8))
plt.barh(
    studies["group"].tolist(), studies["count"].tolist(), color=COLORS["dark blue"]
)
fig.suptitle(
    "Jednostki osób pracujących (nauczycieli akademickich",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "teachers.png")
if __name__ != "__main__":
    plt.show()

# %%
## Praconicy i pracownice
studies = prepare_data_barplots(
    df=df, f="P33g_1", t="P33g_45", mapping=mappings.column_names_to_labels
)

studies = studies.groupby("group").sum().reset_index().sort_values("count")

fig = plt.figure(figsize=(10, 8))
plt.barh(
    studies["group"].tolist(), studies["count"].tolist(), color=COLORS["dark blue"]
)
fig.suptitle(
    "Jednostki osób parcujących (nie nauczycieli akademickich)",
    ha="center",
    fontsize=12,
    weight="bold",
)
fig.tight_layout()
fig.savefig(PNG / "no-teachers.png")
if __name__ != "__main__":
    plt.show()
# %%
## Szkoły doktorskie
phds = (
    df["P33d"]
    .value_counts()
    .reset_index()
    .rename(columns={"P33d": "Jednostki", "count": "Liczebność"})
    .sort_values("Liczebność")
)
phds["Jednostki"] = (
    phds["Jednostki"].map(mappings.variable_value_labels["P33d"]).map(JEDNOSTKI)
)

fig = plt.figure(figsize=(10, 8))
plt.barh(
    phds["Jednostki"].tolist(), phds["Liczebność"].tolist(), color=COLORS["dark blue"]
)
fig.suptitle("Szkoły Doktorskie", ha="center", fontsize=12, weight="bold")
fig.tight_layout()
fig.savefig(PNG / "phds.png")
if __name__ != "__main__":
    plt.show()

# %%
