from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')# - padrao
html = urlopen('https://pt.aliexpress.com/w/wholesale-gamepads.html?spm=a2g0o.categorymp.0.0.4222IZF2IZF2Kz&categoryUrlParams=%7B%22q%22%3A%22gamepads%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22category_navigate%22%2C%22sg_search_params%22%3A%22%22%2C%22guide_trace%22%3A%22729998cc-ed8c-4f28-953c-2075c336d071%22%2C%22scene_id%22%3A%2237749%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22pt%22%2C%22bizScene%22%3A%22category_navigate%22%2C%22guideModule%22%3A%22category_navigate_vertical%22%2C%22postCatIds%22%3A%2244%22%2C%22scene%22%3A%22category_navigate%22%7D&isFromCategory=y')# - padrao
bs = BeautifulSoup(html.read(), 'html.parser') # - padrao
#print(bs.h1) - TEST

#nameList = bs.findAll('span', {'class':'green'}) - printa todos os span com class 'green'
#for name in nameList: -  ele far um for pra percorrer o namList e printa tudo com .get_text que nao é tao bom usar
#ele remove todas as tags e retorna um bloco de texto
#    print(name.get_text())


#PODEMOS PUXAR ASSIM
#nameList = bs.find_all(['h3']) #pesquisando pela tag
#OU ASSIM
#nameList = bs.find_all('h3', {'class':'multi--titleText--nXeOvyr'})
priceList = bs.find_all('div', {'class':'multi--price-sale--U-S0jtj'})

#FORMATAÇÃO SIMPLES

#for name in priceList:
    #print(name) # printa alguns produtos pelo h3 na pagina

#FORMATAÇÃO SIMPLES


#FORMATAÇÃO MAIS LIMPA





for price in priceList:
    currency_symbol = price.find_all('span')[0].text.strip()
    integer_part = price.find_all('span')[1].text.strip()
    decimal_part = price.find_all('span')[3].text.strip()
    formatted_price = f"{currency_symbol} {integer_part},{decimal_part}"
    print(formatted_price)














#nameList = bs.find_all(['h1','h2','h3','h4','h5','h6']) - ele da um find em todos os elementos dentro do array
#for name in nameList: -  faz um for para percorrer essa lista que vai armazenar as informações
    #print(name.get_text()) - e printar como texto um bloco do bealtifulsoup



#O argumento keyword permite selecionar tags que contenham um atributo ou um conjunto de atributos especificos
#exemplo


#title = bs.find_all(id='titleContainerundefined', class_='rax-view-v2')



#document.querySelector("#titleContainerundefined")
#<span class="rax-text-v2 prodTitle rax-text-v2--overflow-hidden rax-text-v2--singleline" style="width: 176px; line-height: 16px; font-size: 12px; color: rgb(25, 25, 25); text-overflow: ellipsis; overflow: hidden;">Xiaomi-Smartphone Redmi Note 13, Versão Global, Snapdragon 685, Display AMOLED 6.67 ", Câmera 108MP, Carregamento Rápido de 33W, 5000mAh, Novo</span>
#bs.find_all(class='green') - NÃO PODEMOS USAR ISSO É REDUNDANTE DENTRO DO PYTHON !!!!
#bs.find_all(class_='green') - FORMA CORRETA DE SE USAR O CLASS COMO KEYWORD NA BUSCA

#AS KEYWORDS FUNCIONAM COMO FILTRO !

#<div id="titleContainerundefined" class="rax-view-v2"><span class="rax-text-v2 prodTitle rax-text-v2--overflow-hidden rax-text-v2--singleline" style="width: 176px; line-height: 16px; font-size: 12px; color: rgb(25, 25, 25); text-overflow: ellipsis; overflow: hidden;">Xiaomi-Smartphone Redmi Note 13, Versão Global, Snapdragon 685, Display AMOLED 6.67 ", Câmera 108MP, Carregamento Rápido de 33W, 5000mAh, Novo</span></div>




