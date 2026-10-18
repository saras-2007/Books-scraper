
import pandas as pd

# Load the scraped dataset
df = pd.read_csv("books.csv")

# Display the original dataset information
print("Original number of books:", len(df))
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates(subset=["Title"])

# Remove rows with missing required data
df = df.dropna(
    subset=["Title", "Price", "Rating", "Availability"]
)

# Save the cleaned dataset
df.to_csv("cleaned_books.csv", index=False)

# Display the results
print("\nData cleaning completed!")
print("Cleaned number of books:", len(df))
print("Saved as cleaned_books.csv")
