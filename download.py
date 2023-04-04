import requests
import os
from random import choice

user_agents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'
]

def clean_string(unclean_string):
    wierd_chars = ['/', '\\', ':', '?', '"', '<','>','|', '=']
    s = ''
    for i in unclean_string:
        if i in wierd_chars:
            s = ''
        else:
            s += i
    return s

def get_file_name(url):
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

def download(url:str, dir:str):
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
        name = get_file_name(url)
        name = clean_string(name)
        file_name =  f'{dir}/{name}'
        if not os.path.exists(file_name):
            headers = {'User-Agent': choice(user_agents)}
            file = requests.get(url, headers= headers).content
            with open(file_name, 'wb') as f:
                f.write(file)
            print(f'Downloaded {name}')
        else:
            print(f'Skipped {name}')
    except Exception as e:
        print(e)
        print(url, dir)
        with open('errors.txt', 'a') as f:
            f.write(f'Error:{e} URL:{url}\n')
        
def check_downloaded(dir, urls):
    files = os.listdir(dir) 
    not_downloaded = []
    for url in urls:
        b = True
        for i in files:
            if i in url:
                b = False
                break
        if b:
            not_downloaded.append(url)
    return not_downloaded