# News Scraping and Analysis

Este projeto realiza scraping de títulos de notícias de tecnologia do site da BBC e gera uma nuvem de palavras a partir dos títulos coletados.

## Estrutura do Projeto

- `main.py`: Orquestra a execução do scraping e análise.
- `scraper.py`: Coleta os títulos das notícias e salva em um arquivo CSV.
- `analysis.py`: Carrega os títulos do CSV e gera uma nuvem de palavras.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/news-scraping-analysis.git
    cd news-scraping-analysis
    ```

2. Instale as dependências:
    ```bash
    pip install requests beautifulsoup4 pandas matplotlib wordcloud
    ```

3. Execute o script principal:
    ```bash
    python main.py
    ```

## Dependências

- requests
- beautifulsoup4
- pandas
- matplotlib
- wordcloud
