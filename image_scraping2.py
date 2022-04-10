import parsel
import requests
import os

base_url = 'https://www.vmgirls.com'

headers={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
response = requests.get(url=base_url, headers=headers)
html = response.text

selector = parsel.Selector(html)
divs = selector.xpath('//div[@class="col-3 col-md-6"]')

for div in divs:
    pic_title = div.xpath('.//a/@title').get()
    pic_url = div.xpath('.//a/@href').get()

    if not os.path.exists('img\\' + pic_title):
       os.mkdir('img\\' + pic_title)

    # use xpath to minimize the path of second layer and encode the photo
    try:
        html_2 = requests.get(url=pic_url, headers=headers).text
    except:
        continue

    selector_2 = parsel.Selector(html_2)
    img_url_list = selector_2.xpath('.//div[@class="nc-light-gallery"]/a/@href').getall()
    print(img_url_list)

    for img_url in img_url_list:
        try:
            img_data = requests.get(url='https:'+img_url, headers=headers).content
        except:
            continue

        file_name = img_url.split('/')[-1]

        with open(f'img\\{pic_title}\\{file_name}' + file_name, mode='wb') as f:
           f.write(img_data)
           print('Successfully Download: ', file_name)