import os
from PIL import Image
import concurrent.futures

def check_downloaded_file(path):
    """
    Check if there is a corrupted image
    """
    try:
        img = Image.open(path)
        img.verify()
    except Exception:
        print(f'corrupted file {path}')

def check(downloadDir):
    dirs = os.listdir(downloadDir)
    for i in dirs:
        dir = os.path.join(downloadDir, i)
        imgs = [os.path.join(dir, img) for img in os.listdir(dir)]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(check_downloaded_file, imgs)

if __name__ == '__main__':
    Image.MAX_IMAGE_PIXELS = None
    download_dir = 'downloads'
    check(download_dir)