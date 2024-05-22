import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_news_titles(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao acessar a página")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all(['h3', 'h2', 'h1'])
    news_titles = [title.get_text(strip = True) for title in titles if title.get_text(strip = True) != '']

    return news_titles

def save_titles_to_csv(titles, filename='news_titles.csv'):
    df = pd.DataFrame(titles, columns=['Title'])
    df.to_csv(filename, index=False)
    print(f"Títulos salvos em '{filename}'")

if __name__ == '__main__':
    url = 'https://www.bbc.com/news/technology'
    titles = fetch_news_titles(url)

    if titles:
        save_titles_to_csv(titles)
    else:
        print("Nenhum título encontrado")