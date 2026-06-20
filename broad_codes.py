#Lists every diabetes-adjacent diagnosis code in Coherent (presumably) with its patient count
#This is necessary to build our DM_DX_BROAD list, whih is a list of codes
#that indicate some form of diabates, which excludes us from the control

import pandas as pd
conditions = pd.read_csv("conditions.csv")
conditions["CODE"] = conditions["CODE"].astype(str)
mask = conditions["DESCRIPTION"].str.contains(
    "diabet|prediabet|impaired|glucose|glycemia|glycaemia|glycosuria", case=False, na=False)
print(conditions[mask].groupby(["CODE","DESCRIPTION"])["PATIENT"].nunique()
      .sort_values(ascending=False).to_string())

