import pandas as pd
enc = pd.read_csv("encounters.csv")
print("encounter columns:", list(enc.columns))
for col in ("ENCOUNTERCLASS", "CLASS", "TYPE"):
    if col in enc.columns:
        print(f"\n{col}:"); print(enc[col].value_counts().to_string())

sup = pd.read_csv("supplies.csv")
print("\nsupplies columns:", list(sup.columns), "| rows:", len(sup))
if "DESCRIPTION" in sup.columns:
    print(sup["DESCRIPTION"].value_counts().head(15).to_string())