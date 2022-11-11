import whois
import datetime

domain = "trustiseverything.de"

whois_info = whois.whois(domain)

data = str(whois_info.creation_date)
print(data)

#ano = int(data[0:4])
#mes = int(data[5:7])
#dia = int(data[8:10])


data1 = datetime.datetime(ano,mes,dia)
data2 = datetime.datetime.now()

#dif = str(data2 - data1)

print ("Ano:", ano)
print ("Dia:", dia)
print ("Mes:", mes)