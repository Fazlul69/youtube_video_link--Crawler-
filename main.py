import scrapetube

videos = scrapetube.get_channel("UC2-BOyC_u8wWPKZ0WIDJ5yw")
url = "https://www.youtube.com/watch?v="
for video in videos:
    a = video['videoId']
    b = url + str(a)
    print(b)