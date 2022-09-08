import requests  # 导入requests包
from bs4 import BeautifulSoup
import re
import time
for x in range(1,10):
    url = 'http://pic.gimhoy.com/acg'
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('body > div > center:nth-child(6)')
    bb = str(data)
    pattern = re.compile(r'<[^>]+>', re.S)
    dd = pattern.sub('', bb)
    out = dd.replace('[', '').replace(']', '')
    print(out)

    with open('wen.txt','a',encoding='utf-8') as f:
        f.write(f'{out}')
        f.write("\n")
    time.sleep(1)

