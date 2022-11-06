import requests
import re
from urlextract import URLExtract


def acquireAddress():
    print("Please insert a starting address: ")
    #startingAddress = input()
    startingAddress1 = "https://freebitco.in/"
    startingAddress2 = "https://www.google.com/"
    startingAddress = "https://www.w3schools.com/"
    while(re.search("(?P<url>https?://[^\s]+)", startingAddress) == None or re.search("^https://.*$", startingAddress) == None):
        print("Please insert a valid address with the following structure: https://websitename.topleveldomain[/etc/etc...]")
        startingAddress = input()
    print("Valid address")
    while (startingAddress[-1] == "/"):
        print("Cleaning..")
        startingAddress = startingAddress.removesuffix("/")
    return startingAddress


def webCrawler(startingAddress, visited):
    print("Current startingAddress: " + startingAddress) #debug
    #print("Current visited: " + str(visited)) #debug
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(startingAddress, headers=headers)
    #print("REQUEST: " + str(r.url)) #debug: check if the request is being re-addressed somewhere else

    extractor = URLExtract()
    urls = extractor.find_urls(r.text)
    urls = list(dict.fromkeys(urls))

    print(urls)

    matches = [] #contains urls that have more depth compared to the startingAddress

    for i in urls:
        #print("Checking if " + startingAddress + " is in " + i)
        if re.search(("^(.*\.)?" + startingAddress + "/.+$"), i) != None:
            #print("MATCH")
            matches.append(i)

    print(matches) #debug

    for i in matches:
        if (i not in visited):
            nextVisit = max(visited.values())+1
            visited.update({i:nextVisit})
            visited = webCrawler(startingAddress, visited) #safe??
            #visited = webCrawler(i, visited) #experimental
            print("visited: " + str(visited))






    return visited



startingAddress = acquireAddress()
visited = webCrawler(startingAddress, visited={startingAddress:1}) #key shows the visited address meanwhile the value shows the order of visit

print("Visited: ")
for key, value in visited.items():
    print(key + " ")












