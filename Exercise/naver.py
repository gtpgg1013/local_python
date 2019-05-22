import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

res = requests.get(url)
html = BeautifulSoup(res.text, 'html.parser')

silgum = html.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li.ah_item.ah_on > a.ah_a > span.ah_k')
sample = html
# for i in range(10):
#     search = html.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(1) > a > span.ah_k')
#     result.append(search.text)

print(silgum)

silgum2 = html.select(".ah_k ")
print(silgum2)
print(len(silgum2))