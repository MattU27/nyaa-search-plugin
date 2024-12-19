def prettyPrinter(torrent_info):
    """
    Formats and prints the torrent information in a way that qBittorrent can understand.

    Parameters:
    torrent_info (dict): A dictionary containing the torrent details with the following keys:
        - link: The download link (magnet or .torrent file)
        - name: The name of the torrent
        - size: The size of the torrent
        - seeds: The number of seeds
        - leech: The number of leechers
        - engine_url: The URL of the search engine
        - desc_link: The URL to the torrent's description page
        - pub_date: The publication date as a Unix timestamp
    """
    print(f"{torrent_info.get('link', '')}|{torrent_info.get('name', '')}|{torrent_info.get('size', '')}|"
          f"{torrent_info.get('seeds', '')}|{torrent_info.get('leech', '')}|{torrent_info.get('engine_url', '')}|"
          f"{torrent_info.get('desc_link', '')}|{torrent_info.get('pub_date', -1)}")