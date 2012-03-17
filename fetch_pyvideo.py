import sys

from pyvideo import fetch_youtube_url
from download import download

if __name__ == '__main__':
    url, name = sys.argv[1], sys.argv[2]
    youtube_url = fetch_youtube_url(url)
    download(youtube_url, name)
