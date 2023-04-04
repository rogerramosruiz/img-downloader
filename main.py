import requests
import os
from download import download
import concurrent.futures

def getUrls(word, numberImages):
    """
    word: Word to be searched

    return urls of images searched by an specific word
    """  
    nm = numberImages
    baseUrl = 'https://unsplash.com/napi/search/photos?query={}&per_page={}&page={}&xp='
    urls = []
    # 100 images added just in case there are repeated urls
    numberImages += 100
    perPage = 30
    # calculate the number of iterations will be needed 
    # for requesting the the images
    iterations = numberImages // perPage
    remainder = numberImages - iterations * perPage
    if iterations * perPage != numberImages:
        iterations += 1
    # request images urls
    for i in range(iterations):
        if i == iterations - 1:
            perPage = remainder
        resp = requests.get(baseUrl.format(word, perPage, i + 1))
        res = resp.json()['results']        
        if len(res) == 0:
            break
        # iterate over the responses and add a url if it's not repeated
        for j in res:
            url = j['urls']['full']
            if url not in urls:
                urls.append(url)
    
    if len(urls) > nm:
        print('urls',len(urls))
        urls = urls[:nm]
    return urls

def main(words, numberImages, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for word in words:
        print(word)
        urls = getUrls(word, numberImages)
        downloadDir = [f'{dir}/{word}'] * len(urls)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(download, urls, downloadDir)

if __name__ == '__main__':
    words = ['house indoor', 'street', 'parks']
    numberImages = 1550
    dir = 'downloads'
    main(words, numberImages, dir)