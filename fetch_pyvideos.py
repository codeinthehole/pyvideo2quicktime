#!/usr/bin/env python
import sys

from pyvideo import fetch_youtube_urls
from download import download

if __name__ == '__main__':
    if len(sys.argv) < 2:
        pyvid_url = 'http://pyvideo.org/category/17/pycon-us-2012'
    else:
        pyvid_url = sys.argv[1]

    for youtube_url, name in fetch_youtube_urls(pyvid_url):
        download(youtube_url, name)
