#!/usr/bin/env python
import sys

from pyvideo import fetch_youtube_url
from download import download

if __name__ == '__main__':
    url = sys.argv[1]
    name = url.split('/').pop()
    youtube_url = fetch_youtube_url(url)
    if not youtube_url:
        print "Unable to extract YouTube URL from page"
    else:
        download(youtube_url, name)
