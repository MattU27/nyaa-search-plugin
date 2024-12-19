import urllib.request
import os
import tempfile

def retrieve_url(url):
    print(f"Retrieving URL: {url}")  # Debug print
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def download_file(url):
    with urllib.request.urlopen(url) as response:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(response.read())
        temp_file.close()
        return temp_file.name, url