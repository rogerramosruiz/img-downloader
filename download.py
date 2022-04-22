import requests
import os
from random import choice

useragents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'
]

def cleanString(str):
    weirdChars = ['/', '\\', ':', '?', '"', '<','>','|', '=']
    s = ''
    for i in str:
        if i in weirdChars:
            s = ''
        else:
            s += i
    return s

def getFileName(url):
    nm    = url.split('/')[-1]
    spl   = nm.split('?')
    name  = spl[0]
    name  = name[name.find('-') + 1:]
    rest  = spl[1]
    start = rest.find('fm=')
    ext   = ''
    for i in range(start + 3, len(rest)):
        if rest[i] == '&':
            break
        ext += rest[i]
    return f'{name}.{ext}'

def download(url,dir):
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
        name = getFileName(url)
        name = cleanString(name)
        fileName =  f'{dir}/{name}'
        if not os.path.exists(fileName):
            headers = {'User-Agent': choice(useragents)}
            file = requests.get(url, headers= headers).content
            with open(fileName, 'wb') as f:
                f.write(file)
            print(f'Downloaded {name}')
        else:
            print(f'Skipped {name}')
    except Exception as e:
        print(e)
        print(url, dir)
        with open('errors.txt', 'a') as f:
            f.write(f'Error:{e} URL:{url}\n')
        
def chechkDownloaded(dir, urls):
    files = os.listdir(dir) 
    nodownloaded = []
    for url in urls:
        b = True
        for i in files:
            if i in url:
                b = False
                break
        if b:
            nodownloaded.append(url)
    return nodownloaded

if __name__ == '__main__':
    url = 'https://images.unsplash.com/photo-1505322022379-7c3353ee6291?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=guille-pozzi-SHcHVFhz7-M-unsplash.jpg'
    name = getFileName(url)
    print(name)