import pandas as pd

df = pd.read_csv("data/RBI_PowerBI_Dataset.csv")

df["Date received"] = pd.to_datetime(df["Date received"])

df["Year"] = df["Date received"].dt.year
df["Month"] = df["Date received"].dt.month
df["Month_Name"] = df["Date received"].dt.strftime("%B")

df.to_csv("data/RBI_PowerBI_Final.csv", index=False)

print("Final dataset created successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))
