'''RASPAGEM DE DADOS - WEB SCRAPPING'''

#Referência
'''
- https://imasters.com.br/desenvolvimento/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup/?trace=1519021197&source=single

- https://www.crummy.com/software/BeautifulSoup/

- https://www.vooo.pro/insights/guia-para-iniciantes-de-web-scraping-em-python-usando-beautifulsoup/

'''

'''
Raspagem de dados serve para reunir informações de páginas web
'''

'''
Para baixar dados HTML de um site é utilizado a API requests que é instalado pelo
pip (python), seu comando é 'pip install requests beautifulsoup4 lxml'

Após tal comando o módulo requests está disponível para ser utilizado.

Ele é importado através de 'import requests' e o download das informações do site
é feito pelo método get

site = requests.get('url do site aqui')

Se o valor do site for 200 então o site foi baixado com sucesso. Valores com
inicial 2 representam sucesso e iniciais 4 e 5 geralmente significam erro

O método content na variável cujo valor é o site (status 200) mostra toda a HTML
do site em uma única linha.
'''


