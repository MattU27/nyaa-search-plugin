# VERSION: 1.00
# AUTHORS: YOUR_NAME (YOUR_MAIL)
# LICENSING INFORMATION

import sys
from engines.nyaa import Nyaa

def main():
    if len(sys.argv) < 3:
        print("Usage: nova2.py <engine_name> <category> <search_tokens>")
        return

    engine_name = sys.argv[1]
    category = sys.argv[2]
    search_tokens = ' '.join(sys.argv[3:])

    if engine_name.lower() == 'nyaa':
        nyaa_engine = Nyaa()
        nyaa_engine.search(search_tokens, category)
    else:
        print(f"Engine '{engine_name}' not found.")

if __name__ == "__main__":
    main()