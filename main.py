import requests
import os
from download import download
import concurrent.futures
from check import check
def get_urls(word:str, number_images:int):
    """
    word: Word to be searched
    number_images: Number of images to search

    return urls of images searched by an specific word
    """  
    nm = number_images
    baseUrl = 'https://unsplash.com/napi/search/photos?query={}&per_page={}&page={}&xp='
    urls = []
    # 100 images added just in case there are repeated urls
    number_images += 100
    per_page = 30
    # calculate the number of iterations will be needed 
    # for requesting the the images
    iterations = number_images // per_page
    remainder = number_images - iterations * per_page
    if iterations * per_page != number_images:
        iterations += 1
    # request images urls
    for i in range(iterations):
        if i == iterations - 1:
            per_page = remainder
        resp = requests.get(baseUrl.format(word, per_page, i + 1))
        res = resp.json()['results']        
        if len(res) == 0:
            break
        # iterate over the responses and add a url if it's not repeated
        for j in res:
            url = j['urls']['full']
            if url not in urls:
                urls.append(url)
    
    if len(urls) > nm:
        print('urls', len(urls))
        urls = urls[:nm]
    return urls

def main(words, number_images, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for word in words:
        print(word)
        urls = get_urls(word, number_images)
        download_dir = [f'{dir}/{word}'] * len(urls)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(download, urls, download_dir)
    # check for corrupted images
    check(dir)

if __name__ == '__main__':
    words = ['house indoor', 'street', 'parks']
    number_images = 1
    dir = 'downloads'
    main(words, number_images, dir)