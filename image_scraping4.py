import requests
import parsel

# target url :
base_url= 'https://murine-modelling.com.hk/models/lera/'
# create fake user-agent
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

# send requests to target
response = requests.get(url=base_url, headers= headers)
html = response.text

selector = parsel.Selector(html)
divs = selector.xpath('//div[@id="gallery-1"]/figure')

for div in divs:
    pic_title = div.xpath('.//a/@href').get()  # path of url
    pic_url = div.xpath('.//a/@href').get()  # path of url
    img_data = requests.get(url=pic_url, headers=headers).content
    file_name = pic_url.split('/')[-1]

    with open(f'img/' + file_name, mode='wb') as f:
        f.write(img_data)
        print('Successfully Download: ', file_name)