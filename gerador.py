import requests
import re
import json
import sys

local = sys.argv[1]

r = requests.post(
    "https://api.deepai.org/api/text-generator",
    files={
        'text': open('/tmp/original.txt', 'rb'),
    },
    headers={'api-key': '8f4af30a-cf37-4b81-a11d-892995bbf702'}
)

dados = r.json()

saida = dados['output']

txt = '/mnt/d/OneDrive/Arquivos TCC/E-mails Teste/' + local

#print(saida)

with open(txt, 'w') as arquivo:
    arquivo.write(saida)