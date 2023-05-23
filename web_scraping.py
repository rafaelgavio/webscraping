import requests
import csv
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['titulos', 'anos', 'nota']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for filmes in soup.select('.titleColumn'):
        titulo = filmes.select_one('.titleColumn a').text.strip()
        ano = filmes.select_one('.secondaryInfo').text.strip()
        nota_element = soup.select_one('.imdbRating strong')
        nota = nota_element.text if nota_element else None

        writer.writerow({'titulos': titulo, 'anos': ano, 'nota': nota})

print('Dados extraídos e salvos em filmes.csv')