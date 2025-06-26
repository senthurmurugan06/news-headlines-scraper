# 📰 News Headlines Web Scraper

## 📌 Objective
This project is a simple web scraper that fetches top news headlines from a public news website and saves them into a `.txt` file using Python.

---

## 🛠️ Tools & Libraries Used
- Python 3.x
- `requests` – for sending HTTP requests
- `BeautifulSoup` (`bs4`) – for parsing HTML content

---

## 🚀 How It Works
1. Sends a **GET request** to `https://www.bbc.com/news`
2. Parses the HTML content using `BeautifulSoup`
3. Extracts all `<h2>` headline tags
4. Saves the extracted headlines into a text file called `headlines.txt`

---

## 📁 Files Included
| File | Description |
|------|-------------|
| `web_scraper.py` | Python script to scrape headlines |
| `headlines.txt` | Output file containing scraped headlines |
| `README.md` | Project explanation and usage guide |

---

## ▶️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/news-headlines-scraper.git
   cd news-headlines-scraper
