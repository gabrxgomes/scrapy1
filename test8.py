from urllib.request import urlopen
#html = urlopen('http://pythonscraping.com/pages/page1.html')
html = urlopen('https://campaign.aliexpress.com/wow/gcp-plus/ae/tupr?_immersiveMode=true&wx_navbar_hidden=true&wx_navbar_transparent=true&ignoreNavigationBar=true&wx_statusbar_hidden=true&wh_weex=true&wh_pid=300000533%2FGreat-value-deals&af=917208529&cn=68188&cv=ali&dp=a4822f629c191fa411e249f7cc17d1cf&aff_fcid=b560a469fa914784a5a30eeb556aa746-1721061396431-09079-_DF2d3rV&tt=CPS_NORMAL&aff_fsk=_DF2d3rV&aff_platform=portals-promotion&sk=_DF2d3rV&aff_trace_key=b560a469fa914784a5a30eeb556aa746-1721061396431-09079-_DF2d3rV&terminal_id=855b5dae3f234eb5bb390ba90ff22b2e')
print(html.read())

#Esse comando exibe o código HTML completo de page1, que está no URL
#http://pythonscraping.com/pages/page1.html. Para ser mais exato, ele exibe
#o arquivo HTML page1.html, que se encontra no diretório <web
#root>/pasges, no servidor localizado no domínio http://pythonscraping.com

#essa execução mais simples consegue puxar o html completo de maneira direta e sem erros, é a camada mais superfial do html