import urllib
import os
import requests
import lxml
from lxml import html
from lxml import etree

path = "d://music//藏歌//"
if not os.path.exists(path):
    os.makedirs(path)

geshou_url = "http://www.9ku.com/zhuanji/taste11.htm"

r = requests.get(geshou_url).content
a = etree.HTML(r)

xuhaos = a.xpath('//ol/li/span/text()')

count = 0
while (count < len(xuhaos)):
    nums = a.xpath('//li/input/@value')##歌手好听部分nums = a.xpath('//*[@id="fg"]/li/input/@value')
    print(len(nums))
    for num in nums:
        num = num[:-1] ##下载的地址序号
        # print(num)
        url = "http://www.9ku.com/down/" + num + ".htm"

        r = requests.get(url).content
        a = etree.HTML(r)
        mp3_urls = a.xpath('//div/a/@href')
        for mp3_url in mp3_urls:
            if "mp3" in mp3_url:
                i = mp3_url

        titles = a.xpath('//div/a/text()')
        for title in titles:
            if "Mp3" in title:
                j = title[:-5]

        m = requests.get(i)

        with open(path + xuhaos[count] + j + ".mp3", "wb") as f:
            f.write(m.content)
            f.close()
            print("downloaded: "+xuhaos[count]+j+".mp3")
        count += 1