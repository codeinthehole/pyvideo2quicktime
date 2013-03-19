#!/usr/bin/env python
import sys

from pyvideo import fetch_youtube_url
from download import download

def download_url(url):
    name = url.split('/').pop()
    youtube_url = fetch_youtube_url(url)
    download(youtube_url, name)

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file, 'r') as f:
        for line in f:
            url = line.strip()
            download_url(url)
