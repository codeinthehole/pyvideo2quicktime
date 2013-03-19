from urlparse import urlparse, parse_qs
import os


def download(youtube_url, filename):
    foldername = 'quicktime'
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    notify('Downloading %s (%s)' % (youtube_url, filename))
    flv_filename = download_video(youtube_url)
    m4v_filepath = '%s/%s.m4v' % (foldername, filename)
    notify('Converting %s tp M4V format %s' % (flv_filename, m4v_filepath))
    convert_flv_to_m4v(flv_filename, m4v_filepath)
    notify('Conversion finished - cleaning up')
    os.unlink(flv_filename)
    return m4v_filepath


def download_video(url):
    # Use youtube-dl to handle the download
    os.system('./youtube-dl "%s"' % url)
    # youtube-dl will download the video to a file with
    # name matching the YouTube ID of the video.
    return '%s.flv' % extract_youtube_id(url)


def extract_youtube_id(url):
    q = urlparse(url).query
    return parse_qs(q)['v'][0]


def convert_flv_to_m4v(flv_path, m4v_path):
    # Shell out to ffmpeg to do the conversion - hide the
    # output as there's masses of it.
    os.system('ffmpeg -i %s %s > /dev/null' % (flv_path, m4v_path))


def notify(msg):
    line = '-' * len(msg)
    print "\n%s\n%s\n%s\n\n" % (line, msg, line)
