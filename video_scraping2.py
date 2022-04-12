import re
import requests

url = 'https://v.huya.com/g/shixialiuxing?set_id=51'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}


response = requests.get(url=url, headers=headers)
html = response.text

video_ids = re.findall('<a href="//v.huya.com/play/(.*?).html" class="video-wrap"', html)
# print(video_ids)
for index in video_ids:
    index_url = f'https://liveapi.huya.com/moment/getMomentContent?callback=&videoId={index}&uid=&_=1649740849834'
    response_1 = requests.get(url=index_url, headers=headers)
    # title
    title = response_1.json()['data']['moment']['videoInfo']['videoTitle']
    video_tile = title.replace('\n', '')
    # definitions
    video_url = response_1.json()['data']['moment']['videoInfo']['definitions'][-1]['url']

    response_2 = requests.get(url=video_url, headers=headers)
    #print(video_tile, video_url)


    with open( f'{video_tile}.mp4', mode='wb') as f:
        f.write(response_2.content)
        print(f'successfully download {video_tile}')