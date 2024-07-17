from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(int(datetime.datetime.now().timestamp()))
#cria um numero aleatorio baseado no timestamp atual


def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a',
                                                          href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) < 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    #usa o random.seed baseado no timestamp atual para pegar um numero aleatorio que é usado para selecionar um link
    #aleatorio da lista de links a cada vez que o codigo é executado
    print(newArticle)
    links = getLinks(newArticle)
