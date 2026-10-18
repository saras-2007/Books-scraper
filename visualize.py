
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("cleaned_books.csv")

# Clean price values
df["Price"] = pd.to_numeric(
    df["Price"].astype(str).str.replace(
        r"[^0-9.]", "", regex=True
    ),
    errors="coerce"
)

df = df.dropna(subset=["Price"])

# Chart 1: Book rating distribution
rating_order = ["One", "Two", "Three", "Four", "Five"]
rating_counts = (
    df["Rating"].value_counts()
    .reindex(rating_order, fill_value=0)
)

rating_counts.plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()
plt.close()

# Chart 2: Book price distribution
df["Price"].plot(kind="hist", bins=15)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("book_price_distribution.png")
plt.show()
plt.close()

print("Both charts created successfully!")
