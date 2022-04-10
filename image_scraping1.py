import requests
import parsel
import os

# target url : https://www.leshetu.com/
base_url= 'https://www.leshetu.com/xz/wlj'
# create fake user-agent
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

# send requests to target
response = requests.get(url=base_url, headers= headers)
html = response.text

# use xpath to minimize the path of first layer
selector = parsel.Selector(html)
divs = selector.xpath('//div[@class="row posts-wrapper"]/div')

for div in divs:
    pic_title = div.xpath('.//h2/a/text()').get() # path of booklet title
    pic_url = div.xpath('.//h2/a/@href').get() # path of booklet url
    #print(pic_title, pic_url)
    print('Downloading : ', pic_title)

    if not os.path.exists('img\\' + pic_title):
        os.mkdir('img\\' + pic_title)

    # use xpath to minimize the path of second layer and encode the photo
    try:
       html_2 = requests.get(url=pic_url, headers= headers).text
    except:
        continue

    selector_2 = parsel.Selector(html_2)
    img_url_list = selector_2.xpath('//div[@class="entry-content u-text-format u-clearfix"]//img/@data-srcset').getall()


    for img_url in img_url_list:
        try:
            img_data = requests.get(url=img_url, headers=headers).content
        except:
            continue

        file_name = img_url.split('/')[-1]

        with open(f'img\\{pic_title}\\{file_name}' + file_name, mode='wb') as f:
           f.write(img_data)
           print('Successfully Download: ', file_name)