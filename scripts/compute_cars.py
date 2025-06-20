# %%
import pyreadstat
from pejk import RAW

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
