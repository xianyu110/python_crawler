import requests
from bs4 import BeautifulSoup
import pandas as pd

# 构造请求URL
url = 'http://search.dangdang.com/?key=%B4%F3%CA%FD%BE%DD&act=input'

# 发送请求并获取HTML代码
response = requests.get(url)
html = response.text

# 解析HTML代码，提取书名、价格和购买链接等信息
soup = BeautifulSoup(html, 'html.parser')
books = soup.select('.bigimg > li')

data = []
for book in books:
    try:
        name = book.select('.name > a')[0].text.strip()
        price = book.select('.price > p > span')[0].text.strip()
        link = book.select('.pic > a')[0]['href']
        data.append([name, price, link])
    except IndexError:
        pass
    # 将数据转换为DataFrame格式
    df = pd.DataFrame(data, columns=['书名', '价格', '购买链接'])

    # 输出为表格
    df.to_csv('books.csv', index=False)