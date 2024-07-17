from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])


#ESSE METODO NOS MOSTRA A UTILIZAÇÃO DE UMA EXPRESSÃO REGULAR ONDE A MESMA FILTRA OS LINKS PARA
#QUE VENHA APENAS OS COM AS CARACTERISTICAS ESPECIFICADAS, NO CASO SÃO OS LINKS DE ARTIGOS