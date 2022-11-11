import requests
import http.client
import whois
import datetime
import sys

domain = sys.argv[1]

########## Score #############
url = "https://api.xforce.ibmcloud.com/api/url/" + domain

headers = {
    "Accept": "application/json",
    "Authorization": "***"
}

response = requests.get(url, headers=headers)

while True:
    try:
        retorno = response.json()
        saida = retorno['result']
        score = saida['score']

        print("Domain", domain, "Score:", score)
        break
    except KeyError:
        break
