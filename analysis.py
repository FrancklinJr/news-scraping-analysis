import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def load_titles_from_csv(filename='news_titles.csv'):
    df = pd.read_csv(filename)
    return df

def generate_wordcloud(text, output_image='wordcloud.png'):
    words = text.split()
    word_freq = Counter(words)
    
    common_words = set(['the', 'and', 'to', 'of', 'a', 'in', 'for', 'on', 'with', 'at', 'by', 'an', 'be', 'as', 'that', 'from', 'this', 'is', 'it', 'its'])
    filtered_words = {word: freq for word, freq in word_freq.items() if word.lower() not in common_words}
    
    if filtered_words:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(filtered_words)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Frequência de palavras nos títulos das notícias')
        plt.savefig(output_image)
        plt.show()
        print(f"Nuvem de palavras salva em '{output_image}'")
    else:
        print("Nenhuma palavra encontrada")

if __name__ == '__main__':
    df = load_titles_from_csv()
    if not df.empty:
        text = ' '.join(df['Title'].tolist())
        generate_wordcloud(text)
    else:
        print("Nenhum título encontrado")