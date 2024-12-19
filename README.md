# Nyaa Search Plugin for qBittorrent

This project provides a search plugin for the Nyaa website, allowing users to search for torrents directly from qBittorrent.

## Project Structure

- **engines/nyaa.py**: Contains the implementation of the search plugin for the Nyaa website. It defines the `Nyaa` class with methods for initializing the plugin, downloading torrents, and searching for torrents.
  
- **helpers.py**: Utility functions that assist the plugin, including `retrieve_url()` for fetching content from URLs and `download_file()` for downloading torrent files.
  
- **nova2.py**: The main script that manages the execution of search engine plugins and calls the search methods defined in the plugin files.
  
- **nova2dl.py**: A standalone script invoked by qBittorrent to download a torrent using a specific search plugin.
  
- **novaprinter.py**: Provides the `prettyPrinter()` function, which formats and prints the search results in a way that qBittorrent can understand.
  
- **socks.py**: A module that provides a standard socket-like interface, required by the `helpers.py` file.

## Installation

1. Download the plugin files and place them in the appropriate directory.
2. Open qBittorrent and navigate to the "Search" tab.
3. Click on "Search engines..." and then "Install a new one".
4. Select the `nyaa.py` file from your filesystem.

## Usage

Once installed, you can use the search plugin by entering your desired search terms in the qBittorrent search bar. The plugin will return results formatted for easy access and download.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!