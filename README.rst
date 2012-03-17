Hacky script for downloading videos from PyVideo and converting them to m4v 
format so they can be synced onto your apple device.  Useful if you
want to see everything that happened at PyCon while commuting.

Requirements:

* pip install requests BeautifulSoup
* youtube-dl (from https://github.com/rg3/youtube-dl/) - add this to the directory
  where this script runs and ensure its execute bit is set.  This was the only 
  YouTube downloader I found that worked.  It doesn't really have a good
  Python API so I call it through os.system.
* ffmpeg (use brew install --use-gcc ffmpeg) - used to convert from .flv to
  .m4v

Usage:

1. Fetch the videos you want and convert them:
   $ python fetch_pyvideos.py

2. Choose which videos you want to download

3. Import them into iTunes using 'File' > 'Add to Library'
