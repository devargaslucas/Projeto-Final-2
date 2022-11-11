import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from rake_nltk import Rake
rake_nltk_var = Rake()
import os
import re
from datetime import datetime
import sys

local = sys.argv[1]
txt = '/mnt/d/OneDrive/Arquivos TCC/E-mails Teste/' + local

with open(txt, 'r') as entrada:
    texto = entrada.read()

#print('\n######### Texto Gerado automáticamente #########\n')
#print(texto)
#print('\n ######### Fim do texto Gerado automáticamente ######### \n')

#corpo = "### Texto Gerado Automaticamente ###\n" + texto + "\n ### Fim do Texto Gerado automaticamente ###\n"
#corpo = texto
#print(corpo)

rake_nltk_var.extract_keywords_from_text(texto)
keyword_extracted = rake_nltk_var.get_ranked_phrases()

string = ' '.join(keyword_extracted)
novastring = re.sub('\W+',' ', string )
novastring = re.sub('[^A-Za-z]+', ' ', novastring)

#print('Palavras chave: ' + novastring + '\n')
novalista = novastring.split()

n = int(len(novalista)/3)

splited = [novalista[i::n] for i in range(n)]
#print(splited)

#with open('/tmp/envio.txt', 'w') as arquivo:
#    arquivo.write(corpo)

data = datetime.today().strftime('%d-%m-%Y')

#envio = 'mail -s "Daily News ' + data + '" tcclucasvargas@gmail.com < /tmp/envio.txt'
#print(envio)
#os.system(envio)

j = 0
print('Domínios a serem avaliados: \n')

while j < n:
    string = ','.join(splited[j])
    string = string.replace(' ', ',')
    string = string.replace(',', ', ')
    
    comando = 'python3 dgn2.py --kws' + ' ' + string
    #print(comando)
    os.system(comando)
    j = j + 1