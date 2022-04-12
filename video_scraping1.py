import requests

url = 'https://videohw-platform.cdn.huya.com/1048585/1199593019326/38046687/21063532b48589417e7209f25c638634.mp4'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}


response = requests.get(url=url, headers=headers)

with open('video.mp4', mode='wb') as f:
    f.write(response.content)