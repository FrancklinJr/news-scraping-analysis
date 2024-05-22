import scraper
import analysis

def main():
    url = 'https://www.bbc.com/news/technology'
    titles = scraper.fetch_news_titles(url)

    if titles:
        scraper.save_titles_to_csv(titles)
        df = analysis.load_titles_from_csv()
        if not df.empty:
            text = ' '.join(df['Title'].tolist())
            analysis.generate_wordcloud(text)
        else:
            print("Nenhum título encontrado")
    else:
        print("Nenhum título encontrado")

if __name__ == '__main__':
    main()
