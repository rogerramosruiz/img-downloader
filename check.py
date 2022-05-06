from copyreg import constructor
import os
from PIL import Image
import concurrent.futures

def checkDownloadedFile(path):
    try:
        Image.open(path)
    except Exception:
        print(f'corrupted file {path}')

def check(downloadDir):
    dirs = os.listdir(downloadDir)
    for i in dirs:
        dir = os.path.join(downloadDir, i)
        imgs = [os.path.join(dir, img) for img in os.listdir(dir)]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(checkDownloadedFile, imgs)

if __name__ == '__main__':
    Image.MAX_IMAGE_PIXELS = None
    downloadDir = 'downloads'
    check(downloadDir)