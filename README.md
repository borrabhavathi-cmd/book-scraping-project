# 📚 Book Scraping Project

A Python-based web scraping project that extracts book information from the Books to Scrape website and stores the collected data in a CSV dataset.

## 🎯 Project Objective

The main objective of this project is to understand the fundamentals of web scraping, HTML parsing, data extraction, and structured data storage using Python.

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- CSV

## 🔍 Data Extracted

The project collects the following information:

- 📖 Book Title
- 💰 Book Price
- 📦 Availability

## ⚙️ How It Works

1. Send an HTTP request to the target website.
2. Retrieve the webpage HTML content.
3. Parse the HTML using BeautifulSoup.
4. Locate and extract book details.
5. Store the extracted information in a Pandas DataFrame.
6. Export the final dataset as a CSV file.

## 📂 Project Files

| File | Description |
|------|-------------|
| `book_scraping (1).py` | Python source code for web scraping |
| `books_dataset.csv` | Scraped book data |
| `README.md` | Project documentation |

## ▶️ How to Run

### 1. Install required libraries

```bash
pip install requests beautifulsoup4 pandas
python "book_scraping (1).py"
