## Image downloader

## Table of contents
- [Requirements](#requirements)
- [Clone repository](#clone-repository)
- [Create a python virutal environment](#create-a-python-virutal-environment)
- [Edit main file](#edit-main-file)
- [Run](#run)


### Requirements
- python

### Clone repository
```bash
git clone https://github.com/rogerramosruiz/img-downloader.git
cd img-downloader
```
### Create a python virutal environment

Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Windows
```powershell
python -m venv venv
venv\Scripts\activate
pip3 install -r requirements.txt
```

### Edit main file
In main.py

Edit words array with the kind of images you want to downlaod

Edit number_images with the number of images to be downloaded per word

e.g: if the values are
```
words = ['street', 'parks']
number_images = 5
```
the number of images to be downloaded be 5 for streets and 5 for parks total 10 images

#### Warning
When the number_images value is too big, the number of actual images downloaded could be lower given that the image server dosen't conatain that ammount images

### Run

Linux
```bash
python3 main.py
```

Windows 
```bash
python main.py
```