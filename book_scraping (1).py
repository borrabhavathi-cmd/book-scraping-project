import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").get_text(strip=True)
    availability = book.select_one(".availability").get_text(" ", strip=True)

    books.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

df = pd.DataFrame(books)
df.to_csv("books_dataset.csv", index=False)

print("Book scraping completed successfully!")
print(df)
