from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

site = sys.argv[1]

html = urlopen(site)
bs = BeautifulSoup(html, 'html.parser')

#print(bs.prettify())


linhas = bs.find_all('p', {'class':'paragraph inline-placeholder'})

with open('/tmp/original.txt', 'w') as arquivo:
	for i in linhas:
		textoextraido = i.text
		arquivo.write(textoextraido)
		#print(textoextraido)
		break