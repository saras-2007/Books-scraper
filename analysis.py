
import pandas as pd

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_books.csv")

# Step 2: Convert price text to numeric safely
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(r"[^0-9.]", "", regex=True)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Remove records with invalid prices
df = df.dropna(subset=["Price"])

# Step 3: Total number of books
print("Total Books:", len(df))

# Step 4: Average book price
print("Average Price: £", round(df["Price"].mean(), 2))

# Step 5: Lowest book price
print("Lowest Price: £", round(df["Price"].min(), 2))

# Step 6: Highest book price
print("Highest Price: £", round(df["Price"].max(), 2))

# Step 7: Five most expensive books
print("\nFive Most Expensive Books:")
print(
    df.nlargest(5, "Price")[["Title", "Price"]].to_string(index=False)
)

# Step 8: Rating distribution
print("\nBook Rating Distribution:")
print(df["Rating"].value_counts())

# Step 9: Availability distribution
print("\nAvailability Distribution:")
print(df["Availability"].value_counts())

print("\nAnalysis completed successfully!")
