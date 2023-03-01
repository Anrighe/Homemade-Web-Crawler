import requests
import re
from urlextract import URLExtract


def acquireAddress():
    # Example addresses
    # startingAddress = 'https://www.w3schools.com/'
    # startingAddress = 'https://www.google.com/'
    startingAddress = 'https://example.com/'

    while re.search('(?P<url>https?://[^\s]+)', startingAddress) is None or re.search('^https://.*$', startingAddress) is None:
        print('Please insert a valid address with the following structure: https://websitename.topleveldomain[/etc/etc...]')
        startingAddress = input()
    print('Valid address')
    while startingAddress[-1] == '/':
        print('Cleaning..')
        startingAddress = startingAddress.removesuffix('/')
    print('Cleaned address: ' + startingAddress)
    return startingAddress


def webCrawler(startingAddress, visited, currentDepth, maxDepth):
    if currentDepth > maxDepth:
        return visited

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    try:
        r = requests.get(startingAddress, headers=headers, timeout=3)

        extractor = URLExtract()
        urls = extractor.find_urls(r.text)
        urls = list(dict.fromkeys(urls))

        matches = []  # contains urls that have more depth compared to the startingAddress

        for i in urls:
            if re.search('^https://.+$', i) is not None and 'mp4' not in i and 'mp3' not in i:
                matches.append(i)

        for i in matches:
            if i not in visited:
                visited.update({i: startingAddress})
                visited = webCrawler(i, visited, currentDepth + 1, maxDepth)

        return visited
    except requests.exceptions.RequestException:
        return visited
    except KeyboardInterrupt:
        return visited

