# VERSION: 1.00
# AUTHORS: YOUR_NAME (YOUR_MAIL)
# LICENSING INFORMATION

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import urllib.parse
from helpers import retrieve_url, download_file
from novaprinter import prettyPrinter
from html.parser import HTMLParser

class Nyaa(object):
    url = 'https://nyaa.land'
    name = 'Nyaa'
    supported_categories = {
        'all': '0',
        'anime': '1_2',
        'games': '1_4',
        'movies': '1_1',
        'music': '1_3',
        'software': '1_5',
        'tv': '1_6'
    }

    def __init__(self):
        pass

    def download_torrent(self, info):
        print(download_file(info))

    def search(self, what, cat='all'):
        search_tokens = urllib.parse.quote(what)
        search_url = f"{self.url}/?f=0&c={self.supported_categories[cat]}&q={search_tokens}"
        try:
            page_content = retrieve_url(search_url)
        except Exception as e:
            print(f"Error retrieving URL: {e}", file=sys.stderr)
            return

        class MyHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.in_result = False
                self.current_data = {}
                self.results = []
                self.field_index = 0

            def handle_starttag(self, tag, attrs):
                if tag == 'tr' and ('class', 'success') in attrs:
                    self.in_result = True
                    self.current_data = {}
                    self.field_index = 0
                if self.in_result:
                    if tag == 'a':
                        for attr in attrs:
                            if attr[0] == 'href' and 'magnet' in attr[1]:
                                self.current_data['link'] = attr[1]

            def handle_endtag(self, tag):
                if tag == 'tr' and self.in_result:
                    self.in_result = False
                    if self.current_data:
                        self.results.append(self.current_data)
                        self.current_data = {}

            def handle_data(self, data):
                if self.in_result:
                    data = data.strip()
                    if data:
                        if self.field_index == 0:
                            self.current_data['name'] = data
                        elif self.field_index == 1:
                            self.current_data['size'] = data
                        elif self.field_index == 2:
                            self.current_data['seeds'] = data
                        elif self.field_index == 3:
                            self.current_data['leech'] = data
                        self.field_index += 1

        parser = MyHTMLParser()
        parser.feed(page_content)

        for result in parser.results:
            result['engine_url'] = self.url
            result['desc_link'] = search_url
            result['pub_date'] = -1  # Set to -1 if not available
            prettyPrinter(result)

if __name__ == "__main__":
    n = Nyaa()
    n.search("Ubuntu Linux")