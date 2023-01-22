import requests
from lxml import html

url = 'https://www.chewy.com/b/raw-food-8424'
response = requests.get(url)

tree = html.fromstring(response.content)
prices = tree.xpath('//span[@class="css-1io094t"]/text()')
weights = tree.xpath('//span[@class="css-1q6qfh9"]/text()')
print(weights)
