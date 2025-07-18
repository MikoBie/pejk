# %%
import pyreadstat
from pejk import RAW, EXCEL

# %%
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
df.loc[
    :, [item for item in df.columns if "P1_" in item or "P33" in item or item == "P32"]
].rename(columns=mappings.column_names_to_labels).to_excel(
    EXCEL / "P32.xlsx", index=False
)

# %%
