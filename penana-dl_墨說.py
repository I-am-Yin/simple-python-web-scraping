import os
import re
import requests
import parsel

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }


def download(novel_url):
    mkdir = input('name a new folder : ')
    os.mkdir(mkdir)
    print('remind* chapter 0 count as 1')
    page_range = int(input('input page_range : '))
    novel_url = novel_url+'issue/'
    for page in range(1, page_range+1):
        url = f'{novel_url}{page}'
        response = requests.get(url=url, headers=headers)
        html_data = response.text
        selector = parsel.Selector(html_data)
        chapter_name = re.findall('<h2 class="chaptername">(.*?)</h2>', html_data)
        title = chapter_name[0]
        f = open(f'{mkdir}\\{title}' + '.txt', mode='w', encoding='utf-8')
        content = selector.xpath('//div[@class="booktitlewrap"]/text()')
        if content is not '《病港》':
            for line in selector.xpath('//p/text()').getall():
                print(line, file=f)
        elif content == '《病港》':
            for line in selector.xpath('//span[@style="color:#1d2129;"]/text()').getall():
                print(line, file=f)
        f.close()
        print('successful downloaded'+url)

print("""

*************    

choose the command you want to use
/h  # user guild
/v  # application version
/dl # download by enter the novel url
/q  # quit the program' 

************

    """)

while 1:
      action = input('enter the command : \n')

      if action == '/h':
        print('This a tool for downloading a single novel from penana')
      elif action == '/dl':
        print('remind* e.g. https://www.penana.com/story/73989/女童軍系列-我被寄宿到糖果女孩的家中')
        novel = input('enter the novel url/link : \n')
        download(novel)

        print('finish downloading novel ! ')
      elif action == '/v':
        print('1.0.0.1')
      elif action == '/q':
        break
      else:
        print('unidentified input')

print('Process finished, welcome to use our service again')
