import requests as r

def funGenerateUrl(f1,f2):
	url=f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{f1}/{f2}.json'
	return url

def genData(c1,c2):
	url=funGenerateUrl(c1,c2)
	res=r.get(url)
	print(res.text)


cr=['inr','usd','eur']


for first in cr:

    for second in cr:

        if first==second:
            continue
        print('-----------------------------')
        print("From ",first," To ",second)
        genData(first,second)