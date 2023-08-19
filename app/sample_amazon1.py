import requests
from bs4 import BeautifulSoup


# Amazonで『野菜・きのこ』をキーワード検索したときのURL
url = "https://www.amazon.co.jp/s?k=%E9%87%8E%E8%8F%9C%E3%83%BB%E3%81%8D%E3%81%AE%E3%81%93&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=SNRU9JV5SRU1&sprefix=%E9%87%8E%E8%8F%9C+%E3%81%8D%E3%81%AE%E3%81%93%2Caps%2C217&ref=nb_sb_noss_2"

# 指定URLからWebページを取得
response = requests.get(url)

# HTML解析するために、BeautifulSoup オブジェクトを作成
soup = BeautifulSoup(response.content, "html.parser")

# <body>タグ内を取得
body = soup.find('body')

# divタグでdata-index属性があるものをすべて抽出
# data-index は商品一つひとつに割り振られている番号的なもの
div_tags = body.find_all('div', attrs={'data-index': True})


# 各divタグからdata-index属性の値を取得し、表示
for tag in div_tags:
    print(tag.get('data-index'))  # div タグの data-index 属性の "1" だったり、"67" などを出力

