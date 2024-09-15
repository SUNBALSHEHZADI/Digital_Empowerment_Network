import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the web page
url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')


books = soup.find_all('article', class_='product_pod')


book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    rating = book.p['class'][1]  
    
    book_data.append({
        'Title': title,
        'Price': price,
        'Availability': availability,
        'Rating': rating
    })

# dataframe
df = pd.DataFrame(book_data)

# save data to CSV
df.to_csv('books.csv', index=False)
print("Data has been saved to books.csv")
