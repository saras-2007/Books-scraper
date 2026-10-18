
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("cleaned_books.csv")

# 1. Check total records and columns
print("Dataset Shape:", df.shape)

# 2. Display the first 5 books
print("\nFirst 5 Books:")
print(df.head())

# 3. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Check duplicate titles
print("\nDuplicate Titles:")
print(df["Title"].duplicated().sum())

# 5. Check column data types
print("\nData Types:")
print(df.dtypes)

# 6. Verify the required columns
required_columns = [
    "Title", "Price", "Rating", "Availability"
]

if all(col in df.columns for col in required_columns):
    print("\nVerification successful!")
else:
    print("\nSome required columns are missing!")
