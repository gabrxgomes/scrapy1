from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)


"""
LIDANDO COM IRMÃOS

 Esse código tem como saída todas as linhas de produtos da tabela, exceto a
 primeira linha com os títulos. Por que a linha com títulos é ignorada?
 Objetos não podem ser irmãos deles mesmos. Sempre que os irmãos de um
 objeto forem obtidos, o próprio objeto não estará incluído na lista. Como
 implica o nome da função, ela chama somente os próximos (next) irmãos.
 Se uma linha no meio da lista, por exemplo, fosse selecionada, e
 next_siblings fosse chamada, somente os irmãos subsequentes seriam
 devolvidos. Assim, ao selecionar a linha de títulos e chamar next_siblings,
 podemos selecionar todas as linhas da tabela, sem selecionar a própria
 linha de títulos.


"""