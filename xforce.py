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
    "Authorization": "Basic NjY2NjQxYjItYmVjZi00NjBkLTg1ZjAtYThmMTM0YTM3YmZlOmRlOTRjNjljLWUxZGItNGQ4Yi05MDEyLTBjNDU4ZDkwMzY3ZQ=="
}

response = requests.get(url, headers=headers)

while True:
    try:
        retorno = response.json()
        saida = retorno['result']
        score = saida['score']

        ########## HTTP Status #############
        #conn = http.client.HTTPConnection(domain)
        #conn.request("GET", "/")
        # fgr1 = conn.getresponse()
        #print(r1.status, r1.reason)

        ########## Saidas #############
        #print("Http Status:", r1.status)
        print("Domain", domain, "Score:", score)
        break
    except KeyError:
        break