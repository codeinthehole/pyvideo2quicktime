#!/usr/bin/env python
import sys

from download import download

if __name__ == '__main__':
    youtube_url, name = sys.argv[1], sys.argv[2]
    download(youtube_url, name)
