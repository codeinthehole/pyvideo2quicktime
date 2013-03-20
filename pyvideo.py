import requests
from BeautifulSoup import BeautifulSoup as Soup
import re
import unittest
from mock import patch
from textwrap import wrap


def fetch_youtube_urls(category_url):
    # Scrape the pyvideo site to get titles and descriptions of
    # each video so you can choose which you want to download.
    urls = []
    for title, description, video_url in fetch_metadata_for_videos(category_url):
        if not does_user_want_to_download(title, description):
            continue
        filename = re.sub(r'\s', '-', title).lower()
        filename = re.sub(r'[^\w-]', '', filename)
        youtube_url = fetch_youtube_url(video_url)
        urls.append((youtube_url, filename))
        return urls
    return urls


def fetch_metadata_for_videos(category_url):
    """
    Return generator for the title, description and video URLs for
    each video on a given category page.
    """
    soup = Soup(requests.get(category_url).content)
    for div in soup('div', attrs={'class': 'row-fluid section'}):
        title = div.findAll('a')[1].text
        description = div.findNext('div', attrs={'class':
                                                 'span7'}).findNext('p').text
        video_path = div.findNext('a')['href']
        video_url = 'http://pyvideo.org%s' % video_path
        yield title, description, video_url


def does_user_want_to_download(title, description):
    print
    print title
    print '=' * len(title)
    print "\n".join(wrap(description, 65))
    print
    result = raw_input('Fetch this video? [y/N] ' )
    print
    return result.lower() == 'y'


def fetch_youtube_url(page_url):
    """
    Pluck the YouTube URL from a given page URL.
    """
    video_soup = Soup(requests.get(page_url).content)
    for anchor in video_soup('a'):
        if not anchor.has_key('href'):
            continue
        if 'youtube' in anchor['href']:
            return anchor['href']


class YouTubeLinkExtractionTests(unittest.TestCase):

    def test_youtube_url_extracted_correctly(self):
        page_url = 'http://pyvideo.org/video/880/stop-writing-classes'
        youtube_url = fetch_youtube_url(page_url)
        self.assertEqual('https://www.youtube.com/watch?v=o9pEzgHorH0',
                         youtube_url)


class MetadataExtractionTests(unittest.TestCase):

    def test_sensible_data_returned(self):
        with patch('__main__.does_user_want_to_download') as predicate:
            predicate.return_value = False
            pyvid_url = 'http://pyvideo.org/category/17/pycon-us-2012'
            fetch_youtube_urls(pyvid_url)
            self.assertTrue(predicate.call_count > 100)




if __name__ == '__main__':
    unittest.main()
