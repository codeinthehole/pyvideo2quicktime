What does this do?
------------------

It provides a few simple commands for downloading videos from the excellent
pyvideo.org site, and converting them to QuickTime format so they can be
imported into iTunes and synced to an Apple device.

For example, you can fetch all the videos from PyCon 2012 that you are
intereseted in.

How do I install it?
--------------------

After cloning the repo, do the following::

    pip install requests BeautifulSoup mock 

Next fetch ``youtube-dl`` from https://github.com/rg3/youtube-dl/ and add this
to the directory, ensuring its execute bit is set.

Ensure you have ``ffmpeg`` installed - this is used to convert from ``.flv`` to
``.m4v``.  You can install with::

    brew install --use-gcc ffmpeg

How to I use it?
----------------

Fetch a single video:

    python fetch_pyvideo.py http://pyvideo.org/video/880/stop-writing-classes some-filename

Browse all videos from PyCon 2012 and choose which to download:

    python fetch_pyvideos.py http://pyvideo.org/category/17/pycon-us-2012

Is the code high quality and well tested?
-----------------------------------------

No.  It's a quick and dirty bit of plumbing.  It's also quite brittle as it uses
screen-scraping to fetch the YouTube URLs.

How does this work?
-------------------

1.  It scrapes the pyvideo site for the relevant YouTube URLs.
2.  The ``youtube-dl`` script is used to fetch the Flash content into a ``.flv``
    file.
3.  This is converted to a ``.m4v`` file using ``ffmpeg``.
