import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Define headers to act like a browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Send GET request
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <h2> tags with class that contains headlines
        headlines = soup.find_all('h2')

        # Write headlines to a file
        with open("headlines.txt", "w", encoding="utf-8") as f:
            for idx, headline in enumerate(headlines):
                text = headline.get_text(strip=True)
                if text:
                    f.write(f"{idx+1}. {text}\n")

        print(" Headlines saved to 'headlines.txt' successfully.")
    else:
        print(f"Failed to retrieve webpage. Status Code: {response.status_code}")

except Exception as e:
    print(f" Error occurred: {e}")
