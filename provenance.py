import pandas as pd
pat = set(pd.read_csv("patients.csv")["Id"])
enc = set(pd.read_csv("encounters.csv")["PATIENT"])
print("patients.csv unique IDs:", len(pat))
print("encounters.csv unique patients:", len(enc))
print("overlap:", len(pat & enc))
print("encounter patients NOT in patients.csv:", len(enc - pat))