from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
#print(bs.div) -- percebemos que na pagina não existe nada alem do h1, nenhum h2 mas sim uma div, e se trocarmos podemos receber essa unida div na saida
