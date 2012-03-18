#!/usr/bin/env python
import sys

from pyvideo import fetch_youtube_url
from download import download

if __name__ == '__main__':
    url = sys.argv[1]
    name = url.split('/').pop()
    youtube_url = fetch_youtube_url(url)
    download(youtube_url, name)
