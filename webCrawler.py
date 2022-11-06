import requests
import re
from urlextract import URLExtract


def acquireAddress():
    print("Please insert a starting address: ")
    #startingAddress = input()
    startingAddress = "https://freebitco.in/"
    while(re.search("(?P<url>https?://[^\s]+)", startingAddress) == None or re.search("^https://.*$", startingAddress) == None):
        print("Please insert a valid address with the following structure: https://websitename.topleveldomain[/etc/etc...]")
        startingAddress = input()
    print("Valid address")
    while (startingAddress[-1] == "/"):
        print("Cleaning..")
        startingAddress = startingAddress.removesuffix("/")
    return startingAddress


def webCrawler(startingAddress, visited):
    r = requests.get(startingAddress)

    extractor = URLExtract()
    urls = extractor.find_urls(r.text)
    urls = list(dict.fromkeys(urls))
    print("ALL URLs:")
    print(urls)

    matches = []

    for i in urls:
        print("Controllo se " + startingAddress + " sta in " + i)
        if re.search(("^" + startingAddress + "/.+$"), i) != None:
            print("MATCH")
            matches.append(i)

    print("AFTER: ")
    print(matches)




startingAddress = acquireAddress()












