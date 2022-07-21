import requests

url = 'http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/champion/Aatrox.json'
url2 = 'http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/champion/Ahri.json'
url3 = 'http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/champion/Amumu.json'
url4 = 'http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/champion/Zeri.json'

res = requests.get(url).json()
res2 = requests.get(url2).json()
res3 = requests.get(url3).json()
res4 = requests.get(url4).json()


champ_lst = (res['data']['Aatrox']['key'], res['data']['Aatrox']['name'])
champ_lst2 = (res['data']['Ahri']['key'], res['data']['Ahri']['name'])
champ_lst3 = (res['data']['Amumu']['key'], res['data']['Amumu']['name'])