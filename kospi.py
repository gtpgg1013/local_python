import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise")

# print(res)
# print(res.status_code)
# print(res.text)

html = BeautifulSoup(res.text, 'html.parser')

# print(html)
kospi = html.select('#KOSPI_now')
print(kospi)
kospi = html.select_one('#KOSPI_now')
print(kospi.text)

