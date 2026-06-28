import pandas as pd

# Load final dataset
df = pd.read_csv("data/RBI_PowerBI_Final.csv")

print("=" * 50)
print("TOTAL COMPLAINTS")
print("=" * 50)
print(len(df))

print("\n")

print("=" * 50)
print("PRODUCT DISTRIBUTION")
print("=" * 50)
print(df["product_5"].value_counts())

print("\n")

print("=" * 50)
print("TOP 20 ISSUES")
print("=" * 50)
print(df["Issue"].value_counts().head(20))

print("\n")

print("=" * 50)
print("TOP 20 STATES")
print("=" * 50)
print(df["State"].value_counts().head(20))

print("\n")

print("=" * 50)
print("TOP 20 COMPANIES")
print("=" * 50)
print(df["Company"].value_counts().head(20))

print("\n")

print("=" * 50)
print("TIMELY RESPONSE")
print("=" * 50)
print(df["Timely response?"].value_counts())

timely_percentage = (
    (df["Timely response?"] == "Yes").sum()
    / len(df)
) * 100

print(f"\nTimely Response Rate: {timely_percentage:.2f}%")
