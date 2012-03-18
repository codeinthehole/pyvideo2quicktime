=================
pyvideo2quicktime
=================

What does this do?
------------------

It provides a few simple commands for downloading videos from the excellent
`pyvideo.org`_ site, and converting them to QuickTime format so they can be
imported into iTunes and synced to an Apple device.

.. _`pyvideo.org`: http://pyvideo.org/

Eg, you can can run::

    python fetch_pyvideo.py http://pyvideo.org/video/604/introduction-to-django

and the 'Introduction to Django' talk from PyCon 2012 will be downloaded and
converted to ``.m4v`` format so it can be imported into iTunes.

What's the point?
-----------------

It just lets you watch interesting videos when you're offline and can't watch
them directly through YouTube.

For instance, my daily commute involves around 2 hours on London's underground,
sans internet.  This is the perfect time for watching Python videos, hence why I
scratched this itch.

How do I install it?
--------------------

After cloning the repo, do the following::

    pip install requests BeautifulSoup mock 

Next download ``youtube-dl`` from https://github.com/rg3/youtube-dl/ and add this
to the directory, ensuring its execute bit is set.

Ensure you have ``ffmpeg`` installed - this is used to convert from ``.flv`` to
``.m4v``.  You can install with::

    brew install --use-gcc ffmpeg

Then you're ready to go.

How do I use it?
----------------

Fetch a single video::

    python fetch_pyvideo.py http://pyvideo.org/video/880/stop-writing-classes some-filename

Browse all videos from a category page choose which to download::

    python fetch_pyvideos.py http://pyvideo.org/category/17/pycon-us-2012

Do the videos take a long time to download and convert?
-------------------------------------------------------

Yes.

Is the code high quality and well tested?
-----------------------------------------

No.  It's a quick and dirty bit of plumbing.  It's also quite brittle as it uses
screen-scraping to fetch the YouTube URLs.
