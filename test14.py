from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
              {'src': '../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())


"""

 Esse código exibirá o preço do objeto representado pela imagem no
 endereço ../img/gifts/img1.jpg (nesse caso, o preço é de 15 dólares).
 Como isso funciona? O diagrama a seguir representa a estrutura de árvore
 da parte da página HTML com a qual estamos trabalhando, com os passos
 numerados:

 • <tr>– td– td– td ❸– "$15.00" ❹– td ❷
– <img src="../img/gifts/img1.jpg"> ❶
 ❶ A tag de imagem com src="../img/gifts/img1.jpg" é inicialmente
 selecionada.
 ❷ Selecionamos o pai dessa tag (nesse caso, é a tag td).
 ❸ Selecionamos a previous_sibling da tag td (nesse caso, é a tag td que
 contém o valor do produto em dólar).
 ❹ Selecionamos o texto nessa tag: “$15.00”.

"""