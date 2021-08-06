import scrapetube

videos = scrapetube.get_channel("UCWg8IGoeU3O0PWDwJFH6DLg")
url = "https://www.youtube.com/watch?v="
for video in videos:
    name = video['title']
    a = video['videoId']
    b = url + str(a)
    print(b, name)